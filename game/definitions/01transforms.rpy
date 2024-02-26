default persistent.gaussian_blur = False

python early:
    def Flatten(child, drawable_resolution=True):
        return Transform(child, mesh=True, gl_drawable_resolution=drawable_resolution)

# do it before anything is created
# to make sure it's inherited
# and in case displayables are created during init phase
python early hide:
    for s in renpy.style.styles.values():
        s.subpixel = True
    # i think styles are created at init time
    # so this block is useless :tardlilly:

# also do it at the end of init phase
# style inheritance should take care of it
# but you never know
init 1500 python hide:
    for s in renpy.style.styles.values():
        s.subpixel = True
        
# should cover about everything

python early in override_transform_shit_idk_how_to_name_this:
    from renpy.store import store
    from renpy.display.render import Render, BLIT, DISSOLVE, IMAGEDISSOLVE, PIXELLATE, FLATTEN
    from math import log, sqrt

    renpy.display.transform.TransformState.subpixel = True

    render_functions = [ ]

    def new_transform_render(self, w, h, st, at):
        state = self.state
        rv = self.default_render(w, h, st, at)

        for f in render_functions:
            rv = f(state, rv)

        return rv

    if not hasattr(renpy.display.transform.Transform, "default_render"):
        renpy.display.transform.Transform.default_render = renpy.display.transform.Transform.render
        renpy.display.transform.Transform.render = new_transform_render

    ###########

    def apply_default_blur(render, blur):
        rv = Render(*render.get_size())
        rv.blit(render, (0.0, 0.0))
        rv.mesh = True
        rv.add_shader("shaders.renpy_blur")

        rv.add_uniform("u_renpy_blur_log2", log(blur, 2))
        rv.add_uniform("u_lod_bias", 0.5)
        return rv

    def apply_gaussian_blur(render, blur, direction):
        rv = Render(*render.get_size())
        rv.blit(render, (0.0, 0.0))
        rv.mesh = True
        rv.add_shader("shaders.gaussian_blur")

        sigma = blur / 2.0
        rv.add_uniform("u_radius", blur)
        rv.add_uniform("u_lod_bias", 0.5)
        rv.add_uniform("u_sigma", sigma)
        rv.add_uniform("u_sqr_sigma", sigma * sigma)
        rv.add_uniform("u_direction", direction)
        return rv

    def blur_render(state, render):
        blur = state.blur
        if not blur: return render

        if store.persistent.gaussian_blur:
            blurred_vertically = apply_gaussian_blur(render, blur, (0.0, 1.0))
            rv = apply_gaussian_blur(blurred_vertically, blur, (1.0, 0.0))
        else:
            blur = sqrt(blur) * 6
            rv = apply_default_blur(render, blur)
    
        return rv

    render_functions.append(blur_render)

    renpy.register_shader("renpy.blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_renpy_blur_log2;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        gl_FragColor = texture2D(tex0, v_tex_coord);
    """)

    renpy.register_shader("shaders.renpy_blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_renpy_blur_log2;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        gl_FragColor = vec4(0.0);
        float renpy_blur_norm = 0.0;

        for (float i = -5.0; i < 1.0; i += 1.0) {
            float renpy_blur_weight = exp(-0.5 * pow(u_renpy_blur_log2 - i, 2.0));
            renpy_blur_norm += renpy_blur_weight;
        }

        gl_FragColor += renpy_blur_norm * texture2D(tex0, v_tex_coord.xy, 0.0);

        for (float i = 1.0; i < 14.0; i += 1.0) {

            if (i >= u_renpy_blur_log2 + 5.0) {
                break;
            }

            float renpy_blur_weight = exp(-0.5 * pow(u_renpy_blur_log2 - i, 2.0));
            gl_FragColor += renpy_blur_weight * texture2D(tex0, v_tex_coord.xy, i);
            renpy_blur_norm += renpy_blur_weight;
        }

        if (renpy_blur_norm > 0.0) {
            gl_FragColor /= renpy_blur_norm;
        } else {
            gl_FragColor = texture2D(tex0, v_tex_coord.xy, 0.0);
        }
    """)

    # gaussian blur from WM
    renpy.register_shader("shaders.gaussian_blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform float u_lod_bias;
        uniform float u_radius;
        uniform float u_sigma;
        uniform float u_sqr_sigma;
        uniform vec2 u_direction;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec4 col = texture2D(tex0, v_tex_coord, u_lod_bias);

        float sum = 1.0;

        for (float i=1.0; i <= u_radius; i++) {
            float weight = exp(-i * i / (2.0 * u_sqr_sigma));
            col += texture2D(tex0, v_tex_coord + u_direction * i / res0.xy, u_lod_bias) * weight;
            col += texture2D(tex0, v_tex_coord - u_direction * i / res0.xy, u_lod_bias) * weight;
            sum += weight * 2.0;
        }

        gl_FragColor = col / sum;
    """)

    ###########

    renpy.display.transform.add_property("pixellate", float, None)

    def pixellate_render(state, render):
        p = state.pixellate
        if not p: return render

        rv = Render(*render.get_size())
        rv.blit(render, (0, 0))

        rv.mesh = True
        rv.add_shader("renpy.texture")
        rv.add_property("texture_scaling", "nearest_mipmap_nearest")
        rv.add_property("anisotropic", False)
        rv.add_uniform("u_lod_bias", p + 1)

        rv.operation = PIXELLATE
        rv.operation_parameter = 2 ** p
        return rv

    render_functions.append(pixellate_render)
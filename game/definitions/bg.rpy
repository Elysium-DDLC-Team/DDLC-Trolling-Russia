## Backgrounds
# This section declares the backgrounds available to be shown in the mod.
# To define a new color background, declare a new image statement like in this example:
#     image blue = "X" where X is your color hex i.e. '#158353'
# To define a new background, declare a new image statement like this instead:
#     image bg bathroom = "mod_assets/bathroom.png" 

image sky:
    paths.bg("sky", "sky_bg")
    xoffset 0
    xtile 3 subpixel True

    block:
        xoffset 0
        linear 380 xoffset -3840
        repeat
image sky_rain:
    paths.bg("sky", "sky_bg_rain")

    xoffset 0
    xtile 3 subpixel True
    block:
        xoffset 0
        linear 380 xoffset -3840
        repeat
    
image bg residential_day = Fixed("sky",  paths.bg("street", "residential_day")) # Start of DDLC BG
image bg house = Fixed("sky", paths.bg("street", "house")) # Meiji House BG
image bg house rain = Fixed("sky_rain", paths.bg("street", "house_rain"))
image bg school_gate = Fixed("sky", paths.bg("school", "school_gate_day")) # school gate BG
image bg courtyard = Fixed("sky",  paths.bg("school", "courtyard_day")) # school courtyard BG
image bg street day:
    Fixed("sky",  paths.bg("street", "street_day")) # school courtyard BG


image bg besedka = Fixed("sky", paths.bg("bath", "bga"))
image bg test:
    Fixed("sky", paths.bg("street", "house"))
    pause 0.001
    Fixed("sky_rain", paths.bg("street", "house_rain")) with Dissolve(22.0)


# Statc background
init python:
    def capture_images(prefix, filt):
        for file in filter(filt, renpy.list_files()):
            renpy.image(" ".join([prefix, os.path.splitext(os.path.split(file)[1])[0]]), file)

    capture_images("bg", lambda x: x.startswith("mod_assets/images/bg/"))
    
    print(renpy.display.image.list_images())








# mod background's
image cg movie ricardo flexing = Movie(play="mod_assets/videos/cg_flex1.webm", loops=-1)
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"


image bg notebook = "bg/notebook.png" # Poem Game Notebook Scene
image bg notebook_glitch = "bg/notebook-glitch.png" # Glitched Poem Game BG

# This image shows a glitched screen during Act 2 poem sharing with Yuri.
image bg glitch = LiveTile("bg/glitch.jpg")

# This image transform shows a glitched scene effect
# during Act 3 when we delete Monika.
image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0

# This image transform shows another glitched scene effect
# during Act 3 when we delete Monika.
image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0

image cringe = "images/cringe.png"

# This image transform causes a noise animation to play out.
image noise:
    noise_alpha
    zoom 1.5
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    
    repeat
image post_effects:
    "noise"
# This transform causes the noise effect to appear 25% transparent.
transform noise_alpha:
    alpha 0.023

# This transform causes the noise effect to appear for a bit then disappear.
transform noisefade(t=0):
    alpha 0.0
    t
    linear 5.0 alpha 0.40

init python:
    renpy.register_shader("gl.pyramid", variables="""
        uniform vec2 res0;
        uniform float u_time;
        uniform sampler2D tex0;
    """, vertex_500="""
        v_tex_coord = a_tex_coord;
    """, fragment_500="""


        vec4 DRAWN;
        vec2 v = v_tex_coord * res0;

        vec2 a = vec2(1,-1);
        vec2 b,c = res0.xy;
        vec2 u = (2.0*v-c)/c.y;
        vec2 r = sin(u_time - 0.8*a);

        r += a * r.yx;
        b=c= vec2(r.x,-1)/(4.+r.y);
        DRAWN+= 3e-3 / length( clamp( dot(u-a,v=b-a)/dot(v,v), 0.,1.) *v - u+a );
        b=vec2(0,.4);
        DRAWN+= 3e-3 / length( clamp( dot(u-a,v=b-a)/dot(v,v), 0.,1.) *v - u+a );
        a=c;
        r*= -mat2(.5,.87,-.87,.5);
        DRAWN -= DRAWN;
        b=c= vec2(r.x,-1)/(4.+r.y);
        DRAWN+= 3e-3 / length( clamp( dot(u-a,v=b-a)/dot(v,v), 0.,1.) *v - u+a );
        b=vec2(0,.4);
        DRAWN+= 3e-3 / length( clamp( dot(u-a,v=b-a)/dot(v,v), 0.,1.) *v - u+a );
        a=c;
        r*= -mat2(.5,.87,-.87,.5);
        b=c= vec2(r.x,-1)/(4.+r.y);
        DRAWN+= 3e-3 / length( clamp( dot(u-a,v=b-a)/dot(v,v), 0.,1.) *v - u+a );
        b=vec2(0,.4);
        DRAWN+= 3e-3 / length( clamp( dot(u-a,v=b-a)/dot(v,v), 0.,1.) *v - u+a );
        a=c;
        r*= -mat2(.5,.87,-.87,.5);
        b=c= vec2(r.x,-1)/(4.+r.y);
        DRAWN+= 3e-3 / length( clamp( dot(u-a,v=b-a)/dot(v,v), 0.,1.) *v - u+a );
        b=vec2(0,.4);
        DRAWN+= 3e-3 / length( clamp( dot(u-a,v=b-a)/dot(v,v), 0.,1.) *v - u+a );
        a=c;
        r*= -mat2(.5,.87,-.87,.5);

        vec4 final = texture2D(tex0, v_tex_coord);
        final += DRAWN;

        gl_FragColor = final;
    """)
image pyramid:
    Solid("#000")
    blend "add"
    mesh True
    shader "gl.pyramid"
    0.0
    repeat

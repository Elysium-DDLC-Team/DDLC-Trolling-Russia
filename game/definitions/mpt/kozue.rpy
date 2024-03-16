 #image LayeredImageProxy("natsuki turned", booba_n)
layeredimage kozue base:
    #at [renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="kozue base")]
    always paths.kozue("bases", "base", "face")
    always paths.kozue("bases", "base", "uniform_left_back")
    always paths.kozue("bases", "base", "uniform_right_back")
    always paths.kozue("brows", "b0")
    always paths.kozue("eyes", "e4")
    always paths.kozue("mounth", "m2")
    always paths.kozue("nose", "bm") 

    group autofocus_coloring:
        attribute day default null
        attribute dawn null
        attribute sunset null
        attribute night null
        attribute evening null
        attribute rain null


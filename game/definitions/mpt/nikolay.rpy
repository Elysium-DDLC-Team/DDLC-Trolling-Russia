layeredimage nikolay base:
    group outfit:
        attribute coat default null

    group mood:
        attribute neut default null #neutral

    group base if_any(["coat"]):
        attribute base default:
            paths.nikolay("base", "coat", "base")

    group mouth:
        attribute cm default if_any(["neut"]):
            paths.nikolay("mouth", "m1")

    group brows:
        attribute brow default if_any(["neut"]):
            paths.nikolay("brows", "b1")

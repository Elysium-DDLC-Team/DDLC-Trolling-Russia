layeredimage monika ns:
    at renpy.partial(Flatten, drawable_resolution=False)

    always paths.nsmonika("bases", "face")

    group outfit:
        attribute uniform default null



    group mood: 
        attribute neut default null #neutral
    group left:
        attribute ldown default if_any(["uniform"]):
            paths.nsmonika("bases", "1l")
        attribute lpoint if_any(["uniform"]):
            paths.nsmonika("bases", "2l")
    
    
    group right:
        attribute rdown default if_any(["uniform"]):
            paths.nsmonika("bases", "1r")
        attribute rhip if_any(["uniform"]):
            paths.nsmonika("bases", "2r")

    group blush:
        attribute nobl default null #Default, no blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n


    group nose:
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            paths.nsmonika("nose", "n1")
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            paths.nsmonika("nose", "n2")
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            paths.nsmonika("nose", "n3")
        
        
        attribute n1:
            paths.nsmonika("nose", "n1")
        attribute n2:
            paths.nsmonika("nose", "n2")
        attribute n3:
            paths.nsmonika("nose", "n3")

    group mouth:
        attribute m1 default if_any(["neut"]):
            paths.nsmonika("mouth", "m1")
        attribute m2:
            paths.nsmonika("mouth", "m2")
        attribute m3:
            paths.nsmonika("mouth", "m3")
        attribute m4:
            paths.nsmonika("mouth", "m4")

    group eyes:
    
        attribute e1 default if_any(["neut"]):
            paths.nsmonika("eyes", "e1")
        attribute e2:
            paths.nsmonika("eyes", "e2")
        attribute e3:
            paths.nsmonika("eyes", "e3")
        attribute e4:
            paths.nsmonika("eyes", "e4")
        attribute e5:
            paths.nsmonika("eyes", "e5")
        attribute e6:
            paths.nsmonika("eyes", "e6")

    group brows:
        attribute b1 default if_any(["neut"]):
            paths.nsmonika("brows", "b1")
        attribute b2:
            paths.nsmonika("brows", "b2")
        attribute b3:
            paths.nsmonika("brows", "b3")


    
    
    
# Sayori
image _say_blink_a:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        paths.sayori("blink", "blink_am")
        0.015
        paths.sayori("blink", "blink_af")
        0.035
        paths.sayori("blink", "blink_am")
        0.015
    choice:
        alpha 1.0
        paths.sayori("blink", "blink_am")
        0.015
        paths.sayori("blink", "blink_af")
        0.065
        paths.sayori("blink", "blink_am")
        0.015
    choice:
        alpha 1.0
        paths.sayori("blink", "blink_am")
        0.015
        paths.sayori("blink", "blink_af")
        0.095
        paths.sayori("blink", "blink_am")
        0.015
    choice:
        alpha 1.0
        paths.sayori("blink", "blink_am")
        0.015
        paths.sayori("blink", "blink_af")
        0.035
        paths.sayori("blink", "blink_am")
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        paths.sayori("blink", "blink_am")
        0.015
        paths.sayori("blink", "blink_af")
        0.035
        paths.sayori("blink", "blink_am")
        0.015
    repeat

image _say_blink_t_a:
    alpha 0.0
    renpy.random.randint(30, 60)*0.1
    choice:
        alpha 1.0
        paths.sayori("blink", "blink_t_am")
        0.015
        paths.sayori("blink", "blink_t_af")
        0.035
        paths.sayori("blink", "blink_t_am")
        0.015
    choice:
        alpha 1.0
        paths.sayori("blink", "blink_t_am")
        0.015
        paths.sayori("blink", "blink_t_af")
        0.065
        paths.sayori("blink", "blink_t_am")
        0.015
    choice:
        alpha 1.0
        paths.sayori("blink", "blink_t_am")
        0.015
        paths.sayori("blink", "blink_t_af")
        0.095
        paths.sayori("blink", "blink_t_am")
        0.015
    choice:
        alpha 1.0
        paths.sayori("blink", "blink_t_am")
        0.015
        paths.sayori("blink", "blink_t_af")
        0.035
        paths.sayori("blink", "blink_t_am")
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        paths.sayori("blink", "blink_t_am")
        0.015
        paths.sayori("blink", "blink_t_af")
        0.035
        paths.sayori("blink", "blink_t_am")
        0.015
    repeat

# Monika
image _mon_blink_a:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        paths.monika("blink", "blink_am")
        0.015
        paths.monika("eyes", "forward","e4a")
        0.035
        paths.monika("blink", "blink_am")
        0.015
    choice:
        alpha 1.0
        paths.monika("blink", "blink_am")
        0.015
        paths.monika("eyes", "forward","e4a")
        0.065
        paths.monika("blink", "blink_am")
        0.015
    choice:
        alpha 1.0
        paths.monika("blink", "blink_am")
        0.015
        paths.monika("eyes", "forward","e4a")
        0.095
        paths.monika("blink", "blink_am")
        0.015
    choice:
        alpha 1.0
        paths.monika("blink", "blink_am")
        0.015
        paths.monika("eyes", "forward","e4a")
        0.035
        paths.monika("blink", "blink_am")
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        paths.monika("blink", "blink_am")
        0.015
        paths.monika("eyes", "forward","e4a")
        0.035
        paths.monika("blink", "blink_am")
        0.015
    repeat

image _mon_blink_l_a:
    alpha 0.0
    renpy.random.randint(30, 60)*0.1
    choice:
        alpha 1.0
        paths.monika("blink", "blink_l_am")
        0.015
        paths.monika("blink", "blink_l_af")
        0.035
        paths.monika("blink", "blink_l_am")
        0.015
    choice:
        alpha 1.0
        paths.monika("blink", "blink_l_am")
        0.015
        paths.monika("blink", "blink_l_af")
        0.065
        paths.monika("blink", "blink_l_am")
        0.015
    choice:
        alpha 1.0
        paths.monika("blink", "blink_l_am")
        0.015
        paths.monika("blink", "blink_l_af")
        0.095
        paths.monika("blink", "blink_l_am")
        0.015
    choice:
        alpha 1.0
        paths.monika("blink", "blink_l_am")
        0.015
        paths.monika("blink", "blink_l_af")
        0.035
        paths.monika("blink", "blink_l_am")
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        paths.monika("blink", "blink_l_am")
        0.015
        paths.monika("blink", "blink_l_af")
        0.035
        paths.monika("blink", "blink_l_am")
        0.015
    repeat

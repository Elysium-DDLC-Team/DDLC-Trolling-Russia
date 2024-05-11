# Модифицированные Ренпая методы(нормальные нихуя не работают).
# Короче я хотел сменить папку GUI. А он без него сам ренпай не работает так как пути фиксированные.
# Короче здесь я напихал переделанные методы. Вышло то что я короче движок переписал.
# Ну я не лох какой-то решил даже ему имя дать - IceEngine.
# И чтобы свою версию движка везде не таскать решил некоторые методы лучше перенести в проект где надо.

import store

button_image_extension = ".png"

def button_properties(kind, path="gui"):

        g = globals()

        def get(prop):
            if kind + "_" + prop in g:
                return g[kind + "_" + prop]

            return None

        borders = get("borders")

        tile = get("tile")
        if tile is None:
            tile = store.gui.button_tile

        backgrounds = [ ]

        if kind != "button":
            backgrounds.append(path +"/Buttons/" + kind[:-7] + "_[prefix_]background" + button_image_extension)

        backgrounds.append(path + "/Buttons/[prefix_]background" + button_image_extension)

        if store.renpy.variant("small"):
            backgrounds = [ i.replace(path + "/Buttons", path + "/phone/Buttons") for i in backgrounds ] + backgrounds

        rv = {
            "background" : store.Frame(backgrounds, borders or store.gui.button_borders, tile=tile),
        }

        if borders is not None:
            rv["padding"] = store.gui.borders.padding

        width = get("width")
        height = get("height")

        if width is not None:
            rv["xsize"] = width

        if height is not None:
            rv["ysize"] = height

        return rv

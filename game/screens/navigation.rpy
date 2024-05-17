## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

init python:
    def FinishEnterName(launchGame=True):
        if not player: return
        persistent.playername = player
        renpy.save_persistent()
        renpy.hide_screen("name_input")
        if launchGame:
            renpy.jump_out_of_context("start")

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.8

        spacing gui.navigation_spacing

        if not persistent.autoload or not main_menu:

            if main_menu:

                if persistent.playthrough == 1:
                    textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
                else:
                    textbutton _("New Game") hovered Show('hover1') unhovered Hide('hover1') action Start() at move
            else:

                textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

                textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

            textbutton _("Load Game")  hovered Show('hover2') unhovered Hide('hover2') action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)] at move

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:
                if persistent.playthrough != 3:
                    textbutton _("Main Menu") action MainMenu()
                else:
                    textbutton _("Main Menu") action NullAction()

            textbutton _("Settings")  hovered Show('hover3') unhovered Hide('hover3')  action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)] at move

            if not enable_extras_menu:
                textbutton _("Credits") action ShowMenu("about")

            if renpy.variant("pc"):

                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("Help") action [Help("README.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))] at move

                ## The quit button is banned on iOS and unnecessary on Android.
                textbutton _("Quit") action Quit(confirm=not main_menu) at move
        else:
            timer 1.75 action Start("autoload_yurikill")


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/RifficFree-Bold.ttf"
    color "#31709E"
    #outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
    outlines [(4, "#d9d9d9", 0, 0), (2, "#f3f3f3", 2, 2)]
    hover_outlines [(4, "#aadeff", 0, 0), (2, "#aadeff", 2, 2)]
    insensitive_outlines [(4, "#aadeff", 0, 0), (2, "#aadeff", 2, 2)]

screen hover1:
    text "{color=#0095FF}Click this button and you'll begin the unforgettable story of three friends!" align(.75, .05) at show_clicks
    on "show" action [Hide("hover2"), Hide("hover3"), Hide("hover4")]
    
screen hover2:
    text "{color=#0095FF}Ты сможешь загрузится с того места, где закончил в прошлый раз." align(.75, .05) at show_clicks
    on "show" action [Hide("hover1"), Hide("hover3"), Hide("hover4")]

screen hover3:
    text "{color=#0095FF}Настрой свои ботинки, надень топовую красную бандану Рико,\nтрусы с флагом США и вперёд флексить!" align(.75, .05) at show_clicks
    on "show" action [Hide("hover1"), Hide("hover2"), Hide("hover4")]

screen hover4:
    text "{color=#0095FF}Открытые треки." align(.75, .05) at show_clicks
    on "show" action [Hide("hover1"), Hide("hover2"), Hide("hover3")]

transform show_clicks:
    zoom 1.00
    easein .25 alpha 1.00 zoom 1.05
    zoom 1.05
    easein .25 zoom 1.00
    repeat
    on hide:
        alpha 1.00
        easein .25 alpha 0.00
        
transform move:
    alpha 0.00
    xoffset -100
    easein_bounce 1.35 xoffset 0 alpha 1.00
    on hover:
        zoom 1.00
        easein .25 zoom 1.10
        zoom 1.10
        easein .25 zoom 1.00
        repeat
    on idle:
        zoom 1.10
        easein .25 zoom 1.00
        
transform move2:
    #on hover:
    #    zoom 1.00
    #    easein .25 zoom 1.05
    on idle:
        zoom 1.05
        easein .25 zoom 1.00
        
transform show_window:
    alpha 0.00
    zoom .90
    easein_bounce .55 alpha 1.00 zoom 1.00
    on hide:
        alpha 1.00
        zoom 1.00
        easein .25 alpha 0.00 zoom 0.90
        
transform show_choice:
    alpha 0.00
    yoffset -50
    easein_quint 1.09 alpha 1.00 yoffset 0
    on hide:
        alpha 1.00
        xoffset 0
        easein_quint 1.09 alpha 0.00 yoffset -50

## Экран главного меню ##################################################
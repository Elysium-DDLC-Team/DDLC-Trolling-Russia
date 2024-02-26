## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        window:
            xoffset 35
            has fixed:
                yfit True

            vbox:
                label "[config.name!t]" xalign .5
                text _("Version [config.version!t]\n") xalign .5

                ## gui.about is usually set in options.rpy.
                if gui.about:
                    text "[gui.about!t]\n"

                ## Do not touch/remove these unless the © or – symbol isn't available in your font.
                ## You may add things above or below it.
                ## If you are not going with a splashscreen option, this first line MUST stay in the mod.
                text "Made with GanstaKingofSA's {a=https://github.com/GanstaKingofSA/DDLCModTemplate2.0}DDLC Mod Template 2.0{/a}\nCopyright © 2019-" + str(datetime.date.today().year) + " Azariel Del Carmen (GanstaKingofSA). All rights reserved.\n"
                text "Doki Doki Literature Club. Copyright © 2017 Team Salvato. All rights reserved.\n"
                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""

style about_window is empty
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    color "#000"
    outlines []
    text_align 0.5
    size gui.label_text_size

style about_text:
    color "#000"
    outlines []
    size gui.text_size
    text_align 0.5
    layout "subtitle"

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    idle_color gui.idle_color
    hover_color gui.hover_color
    hover_underline True
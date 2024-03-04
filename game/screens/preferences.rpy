## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    default ddlc_settings = True

    use game_menu(_("Settings"), scroll="viewport"):

        vbox:
            xoffset 175

            hbox:
                style_prefix "navigation"
                xoffset 225
                spacing 5
                textbutton _("DDLC Settings") action [SetScreenVariable("ddlc_settings", True), SensitiveIf(not ddlc_settings)]
                textbutton _("Template Settings") action [SetScreenVariable("ddlc_settings", False), SensitiveIf(ddlc_settings)]
            
            null height 10

            if ddlc_settings:
                use ddlc_preferences
            else:
                use template_preferences
                            
    text "v[config.version]":
                xalign 1.0 yalign 1.0
                xoffset -10 yoffset -10
                style "main_menu_version"

screen ddlc_preferences():
    hbox:
        box_wrap True

        if renpy.variant("pc"):

            vbox:
                style_prefix "radio"
                label _("Display")
                textbutton _("  Windowed") action Preference("display", "window")
                textbutton _("  Fullscreen") action Preference("display", "fullscreen")
                # textbutton _("More") action Show("display_options")

        if config.developer:
            vbox:
                style_prefix "radio"
                label _("Rollback Side")
                textbutton _("  Disable") action Preference("rollback side", "disable")
                textbutton _("  Left") action Preference("rollback side", "left")
                textbutton _("  Right") action Preference("rollback side", "right")

        vbox:
            style_prefix "check"
            label _("Skip")
            textbutton _("  Unseen Text") action Preference("skip", "toggle")
            textbutton _("  After Choices") action Preference("after choices", "toggle")
            # textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
    
    null height (4 * gui.pref_spacing)

    hbox:
        style_prefix "slider"
        box_wrap True

        vbox:
            
            hbox:
                label _("Text Speed")
                
                null width 5

                text str(preferences.text_cps) style "value_text"

            #bar value Preference("text speed")
            bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

            hbox:
                label _("Auto-Forward Time")
                
                null width 5
                
                text str(round(preferences.afm_time)) style "value_text"

            bar value Preference("auto-forward time")

        vbox:
            
            if config.has_music:
                hbox:
                    label _("Music Volume")
                    
                    null width 5
                
                    text str(round(preferences.get_volume("music") * 100)) style "value_text"

                hbox:
                    bar value Preference("music volume")

            if config.has_sound:

                hbox:
                    label _("Sound Volume")
                    
                    null width 5
                
                    text str(round(preferences.get_volume("sfx") * 100)) style "value_text"

                hbox:
                    bar value Preference("sound volume")

                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)

            if config.has_voice:
                hbox:
                    label _("Voice Volume")
                    
                    null width 5
                
                    text str(round(preferences.get_volume("voice") * 100)) style "value_text"

                hbox:
                    bar value Preference("voice volume")

                    if config.sample_voice:
                        textbutton _("Test") action Play("voice", config.sample_voice)

            if config.has_music or config.has_sound or config.has_voice:
                null height gui.pref_spacing

                textbutton _("Mute All"):
                    action Preference("all mute", "toggle")
                    style "mute_all_button"

screen template_preferences():
    hbox:
        box_wrap True

        if extra_settings:
            vbox:
                style_prefix "check"
                label _("Game Modes")
                textbutton _("Uncensored Mode") action If(persistent.uncensored_mode, 
                    ToggleField(persistent, "uncensored_mode"), 
                    Show("confirm", message="Are you sure you want to turn on Uncensored Mode?\nDoing so will enable more adult/sensitive\ncontent in your playthrough.\n\nThis setting will be dependent on the modder if\nthey programmed these checks in their story.", 
                        yes_action=[Hide("confirm"), ToggleField(persistent, "uncensored_mode")],
                        no_action=Hide("confirm")
                    ))
                textbutton _("Let's Play Mode") action If(persistent.lets_play, 
                    ToggleField(persistent, "lets_play"),
                    [ToggleField(persistent, "lets_play"), Show("dialog", 
                        message="You have enabled Let's Play Mode.\nThis mode allows you to skip content that\ncontains sensitive information or apply alternative\nstory options.\n\nThis setting will be dependent on the modder\nif they programmed these checks in their story.", 
                        ok_action=Hide("dialog")
                    )])
        
        python:
            has_discord_module = True
            try:
                RPC
            except NameError:
                has_discord_module = False

        if not renpy.android and has_discord_module:
            vbox:
                style_prefix "name"
                label _("Discord RPC")

                python:
                    connect_status = _("Disconnected")
                    if not persistent.enable_discord:
                        connect_status = _("Disabled")
                    if RPC.rpc_connected:
                        connect_status = _("Connected")
                
                null height 3

                text "[connect_status]" xalign 0.5

                python:
                    enable_text = _("Enable")
                    if persistent.enable_discord:
                        enable_text = _("Disable")

                textbutton enable_text action [ToggleField(persistent, "enable_discord"), 
                    If(persistent.enable_discord, Function(RPC.close), Function(RPC.connect, reset=True))]:
                        text_style "navigation_button_text"
                if persistent.enable_discord and not RPC.rpc_connected:
                    textbutton _("Reconnect") action Function(RPC.connect, reset=True):
                        text_style "navigation_button_text"

    null height (4 * gui.pref_spacing)

    hbox:
        box_wrap True

        if enable_languages and translations:
            vbox:
                style_prefix "radio"
                label _("Language")
                hbox:
                    viewport:
                        mousewheel True
                        scrollbars "vertical"
                        ysize 120
                        has vbox

                        for tran in translations:
                            vbox:
                                for tlid, tlname in tran:
                                    textbutton tlname:
                                        action Language(tlid)


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font "gui/font/SourceSansPro-Black.ttf"
    size 36
    color "#31709E"
    outlines [(3, "#d9d9d9", 0, 0), (1, "#d9d9d9", 1, 1)]
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/Aller_Ru.ttf"
    outlines []

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/Aller_Ru.ttf"
    outlines []

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

style name_label is pref_label
style name_label_text is pref_label_text

style name_text:
    font "gui/font/Aller_Ru.ttf"
    size 36
    color gui.idle_color
    outlines []

style value_text:
    size 27
    color "#000"
    outlines []
    yalign 0.65
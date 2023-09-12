# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os

mod = "mod4"
terminal = guess_terminal()
backgroud_color = "#282a36"
predertminate_font = "arial"
predertimante_fontsize = 14
bar_size = 24
active_color = "#f1fa8c"
icon_size = 15
foreground_color = "#ffffff"
bg_color = "#282a36"
inactive_color = "#6272a4"
dark_color = "#44475a"
text_color = "#bd93f9"
update_color = "#bc0000" #red
red_network = "enp0s1" #in terminal ip address and second option
fgroup_color = "#ff7f00" #orange
sgroup_color = "#d600f7" #dark pink
tgroup_color = "#007bff" #blue
frgroup_color = "#c60000" #red

#Separator function
def fc_separator():
    return widget.Sep(
        linewidth = 0,
        padding = 6,
        foreground = foreground_color,
        background = backgroud_color
    )

#Recangle function 
def fc_rectangle(vColor, type):
    if type == 0:
        #icon = "󱎕 "
        icon = "󱎕"
        #icon = ""
    else:
        icon = ""
    return widget.TextBox(
        text = icon,
        fontsize = bar_size,
        padding= -6,
        foreground = vColor,
        backgroud_color = backgroud_color
    )

#GroupBody function
def fc_body(icon, group_color):
    return widget.TextBox(
        text = icon,
        foreground = foreground_color,
        background = group_color,
        fontsize = icon_size
    )



keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    #Volume control
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SKIN@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SKIN@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SKIN@ toggle")),
    #Screen Brigthness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

groups = [Group(i) for i in [ 
    "","󰖟","","󰉋","",
]]

for i, group in enumerate(groups):
    desktopNumber = str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                desktopNumber,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                desktopNumber,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=predertminate_font,
    fontsize=predertimante_fontsize,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active = active_color,
                    border_width = 1,
                    disable_drag = True,
                    fontsize = icon_size,
                    foreground = foreground_color,
                    highlight_method = "block",
                    inactive = inactive_color,
                    other_current_screen_border = dark_color,
                    other_screen_border = dark_color,
                    padding_x = 7,
                    padding_y = 10,
                ),
                fc_separator(),
                widget.Prompt(),
                widget.WindowName(
                    foreground = text_color,
                    background = backgroud_color
                ),
                widget.Systray(
                    icon_size = icon_size,
                    background = backgroud_color
                ),
                fc_separator(),
                #Group 1
                fc_rectangle(fgroup_color, 0),
                fc_body("",fgroup_color),
                widget.ThermalSensor(
                    foreground = foreground_color,
                    background = fgroup_color,
                    threshold = 50,
                    tag_sensor = "Core 0",
                    fmt = "T1:{}"
                ),
                fc_body("", fgroup_color),
                widget.Memory(
                    foreground = foreground_color,
                    background = fgroup_color,
                ),

                #Group 2
                #--discoment in case of remodel#fc_rectangle(sgroup_color, 0),
                #fc_body("󰑐", sgroup_color),
                #widget.CheckUpdates(
                #    background = sgroup_color,
                #    colour_have_updates = update_color,
                #    colour_no_updates = foreground_color,
                #    no_update_string = '0',
                #    display_format = '{updates}',
                #    update_interval = 1800,
                #    distro = 'Ubuntu_checkupdates'
                #),
                fc_body(" ",sgroup_color),
                fc_body("󰓅", sgroup_color),
                widget.Net (
                    foreground = foreground_color,
                    background = sgroup_color,
                    format = ' {down} 󰳡 {up}',
                    interface = red_network,
                    use_bits = 'true'
                ),
                fc_body(" ",sgroup_color),

                # Group 3
                ##--discoment in case of remode#fc_rectangle(tgroup_color, 0),
                fc_body(' ', tgroup_color),
                widget.Clock(
                    background = tgroup_color,
                    foreground = foreground_color,
                    format="%d/%m/%Y %A %H:%M %p"
                ),
                fc_body('󰕾', tgroup_color),
                widget.PulseVolume(
                    foreground = foreground_color,
                    background = tgroup_color,
                    limit_max_volume = True,
                    fontsize = predertimante_fontsize
                ),
                fc_body(' ', tgroup_color),


                #Group 4
                ##--discoment in case of remode#fc_rectangle(frgroup_color, 0),
                widget.CurrentLayoutIcon(
                    background = frgroup_color,
                    scale = 0.7
                ),
                widget.CurrentLayout(
                    background = frgroup_color,
                ),
            ],
            bar_size,
            background=backgroud_color

            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart = [
        "feh --bg-fill Downloads/wallpaper_at2.jpg",
        "picom --no-vsync &",
        ]

for x in autostart:
    os.system(x)



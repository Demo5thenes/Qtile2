import os

from libqtile import qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from . import defaults


def parseWidgets(leftWidgets, middleWidgets, rightWidgets):
    allWidgets = [leftWidgets, middleWidgets, rightWidgets]

    for widgets in allWidgets:
        i = 1
        for _ in range(len(widgets) - 1):
            if not hasattr(widgets[i], "insertSeparator"):
                widgets.insert(
                    i,
                    widget.Sep(
                        padding=defaults.separator,
                        linewidth=0,
                        background=defaults.colors["transparent"],
                    ),
                )
                i += 2
                continue
            i += 1
    return (
        leftWidgets
        + [widget.Spacer()]
        + middleWidgets
        + [widget.Spacer()]
        + rightWidgets
    )


# Decoration standard for widgets
def decoration(color=defaults.colors["dark"], foreground=defaults.colors["light"], left=False, right=False):
    radius = 4
    if left:
        radius = [5, 0, 0, 5]
    elif right:
        radius = [0, 5, 5, 0]

    return {
        "decorations": [RectDecoration(colour=color, foreground=foreground, radius=radius, filled=True)],
    }


leftWidgets = [
    widget.Clock(
        **decoration(defaults.colors["orange"]),
        foreground=defaults.colors["light"],
        format="%d/%m-%Y ",
    ),
    widget.Clock(
        **decoration(defaults.colors["yellow"]),
        foreground=defaults.colors["light"],
        format="%H:%M ",
    ),
    widget.CheckUpdates(
        **decoration(defaults.colors["aqua"]),
        update_interval=90,
        custom_command="(checkupdates ; paru -Qua) | cat",
        display_format="{updates} ",
        no_update_string="0 ",
        colour_have_updates=defaults.colors["light"],
        colour_no_updates=defaults.colors["light"],
        restart_indicator="ﰇ",
    ),
]


middleWidgets = [
    widget.GroupBox(
        **decoration(),
        highlight_method="text",
        this_screen_border=defaults.colors["blue"],
        this_current_screen_border=defaults.colors["blue"],
        active=defaults.colors["white"],
        inactive=defaults.colors["grey"],
        padding=defaults.padding,
        margin_x=0,
        urgent_alert_method="text",
        urgent_text=defaults.colors["red"],
    ),
]


rightWidgets = [
    widget.DF(
        **decoration(defaults.colors["purple"]),
        format=" {f}{m}B",
        foreground=defaults.colors["light"],
        visible_on_warn=False,
    ),
    widget.Memory(
        **decoration(defaults.colors["blue"]),
        format=" {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
        foreground=defaults.colors["light"],
        measure_mem="G",
    ),
    widget.CPU(
        **decoration(defaults.colors["aqua"]),
        foreground=defaults.colors["light"],
        fomat=" {load_percent:0>2.0f}%",
    ),
    widget.ThermalSensor(
        **decoration(defaults.colors["yellow"]),
        format=" {temp:.0f}°C",
        foreground=defaults.colors["light"],
        foreground_alert=defaults.colors["light"],
        tag_sensor="Package id 0",
    ),
    widget.Battery(
        **decoration(defaults.colors["orange"]),
        foreground=defaults.colors["light"],
        this_screen_border=defaults.colors["blue"],
        this_current_screen_border=defaults.colors["blue"],
        format=" {percent:1.0%}",
        full_char="",
    ),
]

barWidgets = parseWidgets(leftWidgets, middleWidgets, rightWidgets)

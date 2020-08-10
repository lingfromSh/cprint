"""
Color Print
Author: Stephen Ling
"""

# Constraint
COLOR_BLACK = "black"
COLOR_RED = "red"
COLOR_GREEN = "green"
COLOR_YELLOW = "yellow"
COLOR_BLUE = "blue"
COLOR_PURPLE = "purple"
COLOR_CYAN = "cyan"
COLOR_WHITE = "white"

BACKGROUND_FOREGROUND_DIFF = 10
COLOR_MAP = {
    COLOR_BLACK: 30,
    COLOR_RED: 31,
    COLOR_GREEN: 32,
    COLOR_YELLOW: 33,
    COLOR_BLUE: 34,
    COLOR_PURPLE: 35,
    COLOR_CYAN: 36,
    COLOR_WHITE: 37
}

COLOR_PREFIX = "\033[{0}m"
COLOR_SUFFIX = "\033[0m"

DISPLAY_TYPE_DEFAULT = "default"
DISPLAY_TYPE_HIGHLIGHT = "highlight"
DISPLAY_TYPE_UNDERLINE = "underline"
DISPLAY_TYPE_FLASH = "flash"
DISPLAY_TYPE_REVERSE = "reverse"
DISPLAY_TYPE_VISIBLE = "visible"

DISPLAY_TYPE_MAP = {
    DISPLAY_TYPE_DEFAULT: 0,
    DISPLAY_TYPE_HIGHLIGHT: 1,
    DISPLAY_TYPE_UNDERLINE: 4,
    DISPLAY_TYPE_FLASH: 5,
    DISPLAY_TYPE_REVERSE: 7,
    DISPLAY_TYPE_VISIBLE: 8
}


def colorize(text, foreground=None, background=None, display_type=None):
    if foreground:
        foreground = COLOR_MAP.get(foreground)
    if background:
        background = COLOR_MAP.get(background) + BACKGROUND_FOREGROUND_DIFF
    display_type = DISPLAY_TYPE_MAP.get(
        display_type,
        DISPLAY_TYPE_MAP[DISPLAY_TYPE_DEFAULT]
    )
    s = ""
    if foreground:
        s += f"{foreground}"

    if background:
        s += f";{background}"

    if display_type:
        s += f";{display_type}"

    prefix = COLOR_PREFIX.format(s)
    return prefix + text + COLOR_SUFFIX


def cprint(text, *args):
    colored = colorize(text, *args)
    print(colored)


if __name__ == "__main__":
    cprint("Hello World", "red", "green")

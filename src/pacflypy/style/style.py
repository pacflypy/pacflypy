from ..exceptions import ColorNotFound, StyleNotFound
class _COLOR:
    """
    This is My Private Class Color
    """
    GREEN = "\033[92m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    BLACK = "\033[90m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

class _STYLE:
    """
    This is My Private Class Style
    """
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    STRIKE = "\033[9m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    RESET = "\033[0m"

class _dicts:
    color_dict = {
        "0": _COLOR.RESET,
        "1": _COLOR.GREEN,
        "2": _COLOR.RED,
        "3": _COLOR.BLUE,
        "4": _COLOR.YELLOW,
        "5": _COLOR.BLACK,
        "6": _COLOR.CYAN,
        "7": _COLOR.MAGENTA,
        "8": _COLOR.WHITE,
    }
    style_dict = {
        "0": _STYLE.RESET,
        "1": _STYLE.BOLD,
        "2": _STYLE.ITALIC,
        "3": _STYLE.UNDERLINE,
        "4": _STYLE.STRIKE,
        "5": _STYLE.REVERSE,
        "6": _STYLE.HIDDEN,
    }






class styling:
    """
    Class for Get Colors and Pair Colors to a New Color
    """
    @staticmethod
    def color(color: int = 0) -> str:
        """
        Get Color By Code
        Codes:
        0 - Reset
        1 - Green
        2 - Red
        3 - Blue
        4 - Yellow
        5 - Black
        6 - Cyan
        7 - Magenta
        8 - White
        """
        if color not in _dicts.color_dict:
            raise ColorNotFound(color=color, message="Color not found")
        return _dicts.color_dict[color]
    
    @staticmethod
    def style(style: int = 0) -> str:
        """
        Get Style By Code
        Codes:
        0 - Reset
        1 - Bold
        2 - Italic
        3 - Underline
        4 - Strike
        5 - Reverse
        6 - Hidden
        """
        if style not in _dicts.style_dict:
            raise StyleNotFound(style=style, message="Style not found")
        return _dicts.style_dict[style]
    
    @staticmethod
    def pair(color: int = 0, style: int = 0) -> str:
        """
        Pair Style and Color
        """
        if color not in _dicts.color_dict:
            raise ColorNotFound(color=color, message="Color not found")
        if style not in _dicts.style_dict:
            raise StyleNotFound(style=style, message="Style not found")
        return _dicts.color_dict[color] + _dicts.style_dict[style]
    
    @staticmethod
    def print(text: str, color: int = 0, style: int = 0) -> None:
        """
        Print A Message With Color and Style
        Color Codes:
        0 - Reset
        1 - Green
        2 - Red
        3 - Blue
        4 - Yellow
        5 - Black
        6 - Cyan
        7 - Magenta
        8 - White
        Style Codes:
        0 - Reset
        1 - Bold
        2 - Italic
        3 - Underline
        4 - Strike
        5 - Reverse
        6 - Hidden
        """
        print(styling.pair(color=color, style=style) + text + styling.color(color=0) + styling.style(style=0))
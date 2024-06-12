import random
class work:
    """
    Work with string, list, dictionary
    """

    @staticmethod
    def string_to_list(string: str) -> list:
        """
        Convert a string to a list
        """
        return string.split(" ")

    @staticmethod
    def list_to_string(liste: list) -> str:
        """
        Convert a list to a string
        """
        return " ".join(liste)

    @staticmethod
    def get_letter(position: int, word: str) -> str:
        """
        Get a letter from a given position in a word
        """
        if position < len(word):
            return word[position]
        else:
            return ""  # Return empty string if position is out of bounds

    @staticmethod
    def get_letter_position(letter: str, word: str) -> dict:
        """
        Get positions of a letter in a word as a dictionary
        """
        positions = [str(i) for i, char in enumerate(word) if char == letter]
        return {'position': positions}
    
    @staticmethod
    def get_all_letter_position(letter: str, word: str) -> dict:
        """
        Get all Positions from a Letter
        """
        liste = []
        for i in range(word):
            if word[i] == letter:
                liste.append(str(i))
        dicti = {}
        dicti['positions'] = liste
        return dicti
    
    @staticmethod
    def replace_letter_position(word: str, position: int, letter: str) -> str:
        """
        Replace a position to given letter
        """
        word[position] = letter
        return word
    
    @staticmethod
    def replace_letter(word: str, old_letter: str, new_letter: str):
        """
        Replace all old_letter to the new_letter
        """
        for i in range(len(word)):
            if word[i] == old_letter:
                word[i] = new_letter
        return word
    
    @staticmethod
    def generate_random_word(length: int) -> str:
        """
        Generate a random word
        """
        word = ""
        dicti = {
            1: {
                "small": "a",
                "big": "A"
            },
            2: {
                "small": "b",
                "big": "B"
            },
            3: {
                "small": "c",
                "big": "C"
            },
            4: {
                "small": "d",
                "big": "D"
            },
            5: {
                "small": "e",
                "big": "E"
            },
            6: {
                "small": "f",
                "big": "F"
            },
            7: {
                "small": "g",
                "big": "G"
            },
            8: {
                "small": "h",
                "big": "H"
            },
            9: {
                "small": "i",
                "big": "I"
            },
            10: {
                "small": "j",
                "big": "J"
            },
            11: {
                "small": "k",
                "big": "K"
            },
            12: {
                "small": "l",
                "big": "L"
            },
            13: {
                "small": "m",
                "big": "M"
            },
            14: {
                "small": "n",
                "big": "N"
            },
            15: {
                "small": "o",
                "big": "O"
            },
            16: {
                "small": "p",
                "big": "P"
            },
            17: {
                "small": "q",
                "big": "Q"
            },
            18: {
                "small": "r",
                "big": "R"
            },
            19: {
                "small": "s",
                "big": "S"
            },
            20: {
                "small": "t",
                "big": "T"
            },
            21: {
                "small": "u",
                "big": "U"
            },
            22: {
                "small": "v",
                "big": "V"
            },
            23: {
                "small": "w",
                "big": "W"
            },
            24: {
                "small": "x",
                "big": "X"
            },
            25: {
                "small": "y",
                "big": "Y"
            },
            26: {
                "small": "z",
                "big": "Z"
            }
        }

        keys = {
            0: "small",
            1: "big"
        }

        for i in range(length):
            key = random.randint(0, 1)
            letter_nr = random.randint(1, 26)
            letter = dicti[letter_nr][keys[key]]
            word[i] = letter
        return word
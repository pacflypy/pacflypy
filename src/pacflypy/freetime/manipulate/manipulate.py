class work:
    """
    Work with string, list, dictionary
    """
    def __init__(self, content):
        """
        Init the Class with the content
        Args:
           content:
           Can be string, List or Directory
        """
        self.content = content
    @staticmethode
    def string_to_list(string: str) -> list:
        """
        Make a String to a List
        """
        return string.split(" ")
    @staticmethode
    def list_to_string(liste: list) -> str:
        """
        Make a List to a String
        """
        return " ".join(liste)
    @staticmethode
    def get_letter(position: int, word: str) -> str:
        """
        Get a Letter from Given Position
        """
        word_split = word.split("")
        return word_split[position]
    @staticmethode
    def get_letter_position(letter: str, word: str) -> dict:
        """
        Get Letter Position as Dictionary
        """
        dicti = {}
        dicti['position'] = []
        word_split = word.split("")
        max_length = len(word_split)
        for i in range(max_length):
            if word_split[1] == letter:
                liste = dicti['position']
                liste.append(str(i))
                dicti['position'] = liste
        return dicti


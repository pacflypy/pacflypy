import random
class work:
    """
    Arbeit mit Strings, Listen und Wörterbüchern
    """

    @staticmethod
    def string_to_list(string: str) -> list:
        """
        Konvertiert einen String in eine Liste
        """
        return string.split(" ")

    @staticmethod
    def list_to_string(liste: list) -> str:
        """
        Konvertiert eine Liste in einen String
        """
        return " ".join(liste)

    @staticmethod
    def get_letter(position: int, word: str) -> str:
        """
        Holt einen Buchstaben von einer gegebenen Position in einem Wort
        """
        if position < len(word):
            return word[position]
        else:
            return ""  # Gibt leeren String zurück, wenn die Position außerhalb der Grenzen liegt

    @staticmethod
    def get_letter_position(letter: str, word: str) -> dict:
        """
        Holt Positionen eines Buchstabens in einem Wort als Wörterbuch
        """
        positions = [str(i) for i, char in enumerate(word) if char == letter]
        return {'position': positions}
    
    @staticmethod
    def get_all_letter_position(letter: str, word: str) -> dict:
        """
        Holt alle Positionen eines Buchstabens in einem Wort
        """
        positions = [str(i) for i, char in enumerate(word) if char == letter]
        return {'positions': positions}
    
    @staticmethod
    def replace_letter_position(word: str, position: int, letter: str) -> str:
        """
        Ersetzt einen Buchstaben an einer gegebenen Position
        """
        if position < len(word):
            word = word[:position] + letter + word[position+1:]
        return word
    
    @staticmethod
    def replace_letter(word: str, old_letter: str, new_letter: str) -> str:
        """
        Ersetzt alle Vorkommen eines Buchstabens durch einen anderen
        """
        return word.replace(old_letter, new_letter)
    
    @staticmethod
    def generate_random_word(length: int) -> str:
        """
        Generiert ein zufälliges Wort
        """
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return ''.join(random.choice(letters) for _ in range(length))
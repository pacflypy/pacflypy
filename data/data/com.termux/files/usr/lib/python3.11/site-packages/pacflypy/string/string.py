class string:
    """
    Class To Work with Strings
    """
    def __init__(self, accept_integral: bool = False, type: str = "dictionary"):
        """
        Initialize the String and Give an Type and an Accept Integral Bool
        """
        self.accept_integral = accept_integral
        self.type = type
        if self.type == "dictionary":
            self.string = {}
        elif self.type == "list":
            self.string = []
        elif self.type == "string":
            self.string = ""
        else:
            raise ValueError("Invalid type")
    
    def dictadd(self, key: str, value: str = None):
        """
        Add a Key and a Value to the Dictionary
        """
        self.string[key] = value

    def listadd(self, value: str):
        """
        Add a Value to the List
        """
        self.string.append(value)

    def stringadd(self, value: str):
        """
        Add a Value to the String
        """
        self.string += value

    def dictaddint(self, key: str, value: int):
        """
        Add a Key and a Value to the Dictionary
        """
        if not self.accept_integral:
            raise ValueError("This String Doesn't Accept Integral")
        # Make value to String
        value = str(value)
        self.string[key] = value

    def listaddint(self, value: int):
        """
        Add a Value to the List
        """
        if not self.accept_integral:
            raise ValueError("This String Doesn't Accept Integral")
        # Make value to String
        value = str(value)
        self.string.append(value)

    def stringaddint(self, value: int):
        """
        Add a Value to the String
        """
        if not self.accept_integral:
            raise ValueError("This String Doesn't Accept Integral")
        # Make value to String
        value = str(value)
        self.string += value
    
    def dictremove(self, key: str, value: bool = False):
        """
        Remove key from dictionary or an Value from key
        """
        if value:
            self.string[key] = None
        else:
            self.string.pop(key)

    def listremove(self, value: str):
        """
        Remove a Value from the List
        """
        self.string.remove(value)

    def stringremove(self, value: str):
        """
        Remove a Value from the String
        """
        self.string.remove(value)

    def dictreplace(self, key: str, value: str):
        """
        Replace a Value from the Dictionary
        """
        self.string[key] = value

    def listreplace(self, value: str):
        """
        Replace a Value from the List
        """
        self.string.replace(value)

    def stringreplace(self, value: str):
        """
        Replace a Value from the String
        """
        self.string.replace(value)

    def get(self):
        """
        Get the String
        """
        return self.string
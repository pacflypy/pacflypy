class CommandFailedExecute(Exception):
    """
    Exception Class For Command Failed to Execute Error
    """
    def __init__(self, command: str, message="Failed to Execute Command"):
        self.command = command
        self.message = message
        super().__init__(self.message)

class CommandNotFound(Exception):
    """
    Exception Class For Command Not Found Error
    """
    def __init__(self, command: str, message="Command Not Found"):
        self.command = command
        self.message = message
        super().__init__(self.message)

class ColorNotFound(Exception):
    """
    Exception Class For Color Not Found Error
    """
    def __init__(self, color: str, message="Color Not Found"):
        self.color = color
        self.message = message
        super().__init__(self.message)

class StyleNotFound(Exception):
    """
    Exception Class For Style Not Found Error
    """
    def __init__(self, style: str, message="Style Not Found"):
        self.style = style
        self.message = message
        super().__init__(self.message)

class ActionWasExecuted(Exception):
    """
    Exception Class For Action Was Executed Error
    """
    def __init__(self, action: str, message="Action Was Executed"):
        self.action = action
        self.message = message
        super().__init__(self.message)

class ControlFileInvalid(Exception):
    """
    Exception Class For Control File Invalid Error
    """
    def __init__(self, file: str, message="Control File Invalid"):
        self.file = file
        self.message = message
        super().__init__(self.message)

class FileInvalid(Exception):
    """
    Exception Class For File Invalid Error
    """
    def __init__(self, file: str, message="File Invalid"):
        self.file = file
        self.message = message
        super().__init__(self.message)
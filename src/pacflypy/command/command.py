from pacflypy.exceptions import CommandFailedExecute, CommandNotFound, ActionWasExecuted

class command:
    """
    Class To Create Commands safe and easy with Much Features
    """
    def __init__(self, programm: str, safe_output: bool = False, shell: bool = False):
        """
        Initialize The Command Class with Given Main Programm and the Option for safe output or Not
        Args:
            programm (str): The Main Programm Name. e.g. "apt"
            safe_output (bool): Option to Safe output or Not
        """
        self.programm = programm
        self.safe_output = safe_output
        self.shell = shell
        self.command = []
        self.arguments = []
        self.command.append(self.programm)
        self.executed = False
        self.stdout = None
        self.stderr = None
        self.returncode = None

    def get_programm(self):
        """
        Get the Name from the Main Programm
        Returns:
            str: The Name of the Main Programm
        """
        return self.programm
    
    def get_arguments(self):
        """
        Get the Arguments from the Command
        Returns:
            list: The Arguments of the Command
        """
        return self.arguments
    
    def get_command(self):
        """
        Get the Command from the Command
        Returns:
            list: The Command of the Command
        """
        command = " ".join(self.command)
        return command
    
    def get_executed(self):
        """
        Get the Executed Status from the Command
        Returns:
            bool: The Executed Status of the Command
        """
        return self.executed
    
    def stdout(self):
        """
        Get the Stdout from the Command
        Returns:
            str: The Stdout of the Command
        """
        return self.stdout
    
    def stderr(self):
        """
        Get the Stderr from the Command
        Returns:
            str: The Stderr of the Command
        """
        return self.stderr
    
    def returncode(self):
        """
        Get the Returncode from the Command
        Returns:
            int: The Returncode of the Command
        """
        return self.returncode
    
    def arg(self, argument: str):
        """
        Add an Argument to the Command
        Args:
            argument (str): The Argument to add to the Command
        """
        if self.executed:
            raise ActionWasExecuted(action="arg", message="You can't add an Argument to an Executed Command")
        else:
            self.command.append(argument)
            self.arguments.append(argument)
    
    def args(self, arguments: list):
        """
        Add an List of Arguments to the Command
        Args:
            arguments (list): The List of Arguments to add to the Command
        """
        if self.executed:
            raise ActionWasExecuted(action="args", message="You can't add an List of Arguments to an Executed Command")
        else:
            self.command.extend(arguments)
            self.arguments.extend(arguments)

    def remove(self, argument: str):
        """
        Remove an Argument from the Command
        Args:
            argument (str): The Argument to remove from the Command
        """
        if self.executed:
            raise ActionWasExecuted(action="remove", message="You can't remove an Argument from an Executed Command")
        else:
            self.command.remove(argument)
            self.arguments.remove(argument)

    def replace(self, old_argument: str, new_argument: str):
        """
        Replace an Argument from the Command
        Args:
            old_argument (str): The Old Argument to replace from the Command
            new_argument (str): The New Argument to replace the Old Argument with
        """
        if self.executed:
            raise ActionWasExecuted(action="replace", message="You can't replace an Argument from an Executed Command")
        else:
            self.command[self.command.index(old_argument)] = new_argument

    def reset(self):
        """
        Reset the Command to the Initial State
        """
        self.command = [self.programm]
        self.arguments = []
        self.executed = False
        self.stdout = None
        self.stderr = None
        self.returncode = None

    def run(self):
        """
        Run the Command
        """
        if self.executed:
            raise ActionWasExecuted(action="run", message="You can't run an Executed Command")
        else:
            if self.safe_output:
                if self.shell:
                    import subprocess
                    result = subprocess.run(self.command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                    self.stdout = result.stdout
                    self.stderr = result.stderr
                else:
                    import subprocess
                    result = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                    self.stdout = result.stdout
                    self.stderr = result.stderr
            else:
                if self.shell:
                    import os
                    command = self.get_command()
                    os.system(command=command)
                else:
                    import subprocess
                    subprocess.run(self.command)
    
    
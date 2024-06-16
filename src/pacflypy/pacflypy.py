import os as _os
import subprocess as _sp
import sys as _sys

class _process:
    """
    Works with the Process Safe and Fast
    """
    class Command:
        """
        Class to Work Specific with Commands
        """
        def __init__(self, program: str, safe_output: bool = False):
            """
            Init the Class and Given an Special Program
            Args:
                program (str): The Main Programm, e.g python3
                safe_output (bool): Want you safe Output or not
            """
            self._command = []
            self._command.append(program)
            self._program = program
            self._safe_output = safe_output
            self._arguments = []
            self._int = 1
            self._runned = False
            self._output = None
            self._error = None

        def reset(self, program = None, safe_output: bool = False):
            """
            Reset the Class but with the Option to Change Init Values
            Args:
                program (str): The new Main Program, default, the Old
                safe_output (bool): The New Bool, default the Old
            """
            if program is None:
                program = self._program
            self._command = []
            self._command.append(program)
            self._program = program
            self._safe_output = safe_output
            self._arguments = []
            self._int = 1
            self._runned = False
            self._output = None
            self._error = None

        def arg(self, arg: str):
            """
            Add an Argument to Given Command
            """
            self._command.append(arg)

        def args(self, args: list, append: bool = True):
            """
            Add an List of Arguments to the Command
            Args:
                args (list): A List with all args in the correct form.
                append (bool): Add Directly
            """
            if self._runned:
                raise Exception("Command already runned")
            if append:
                self._command.extend(args)
            else:
                for i in range(len(args)):
                    self._command.append(args[i])
                    if i == len(args):
                        self._int = self._int + i + 1

        def remove(self, arg: str):
            """
            Remove an Argument from Command
            Args:
                arg (str): The Argument to delete
            """
            if self._runned:
                raise Exception("Command already runned")
            self._command.remove(arg)

        def replace(self, old_arg: str = "", new_arg: str = "", position: bool = False):
            """
            Replace an Argument.
            Default will all old_args replaced to the new arg
            By position true add an Number as string
            Args:
                old_arg (str): The old Argument
                new_arg (str): The new Argument
                position (bool): Add a Number as String
            """
            if self._runned:
                raise Exception("Command already runned")
            if position:
                old_arg_position = int(old_arg)
                self._command[old_arg_position] = new_arg
            else:
                for i in range(len(self._command)):
                    if self._command[i] == old_arg:
                        self._command[i] = new_arg
        
        def get_command(self, typ: str = "string"):
            """
            Get the Command in the Given typ
            Args:
                typ (str): The type ['string', 'list', 'dict']
            """
            if typ == 'string':
                return " ".join(self._command)
            elif typ == 'dict':
                self._dicti = {}
                # Erstelle dict aus list
                for i in range(self._command):
                    self._dicti[str(i)] = self._command[i]
                return self._dicti
            elif typ == 'list':
                return self._command
            
        def run(self, shell: bool = False, use_child: bool = False, use_os: bool = False):
            """
            Run the Command
            Args:
                shell (bool): Use Shell
                use_child (bool): Use Child Process
                use_os (bool): Use os.system
            Warning, shell and use_child can not mixed
            """
            if self._runned:
                raise Exception("Command Already Runned")
            if shell and use_child:
                raise Exception("Can not use shell and use_child at the same time")
            if shell:
                if self._safe_output:
                    result = _sp.run(self._command, shell=True, capture_output=True, stdout=_sp.PIPE, stderr=_sp.PIPE, text=True)
                    self._output = result.stdout
                    self._error = result.stderr
                else:
                    _sp.run(self._command, shell=True)
            else:
                if self._safe_output:
                    result = _sp.Popen(self._command, shell=False, stdout=_sp.PIPE, stderr=_sp.PIPE, text=True)
                    self._output, self._error = result.communicate()
                else:
                    if use_os:
                        _os.system(self.get_command(typ="string"))
                    else:
                        _sp.run(self._command, shell=False)
            if use_child:
                pid = _os.fork()
                if pid == 0:
                    _os.execvp(self._command[0], self._arguments)
                elif pid < 0:
                    raise Exception("Failed to execute command")
                else:
                    _os.waitpid(pid, 0)
            self._runned = True
        
        def stdout(self):
            """
            Get Explict the stdout
            """
            return self._output
            
        def stderr(self):
            """
            Get Explict the stderr
            """
            return self._error
    
    @staticmethod
    def exit(code: int = 0, message: str = ""):
        """
        Exit the Programm with a Message
        Args:
            code (int): The Exit Code
            message (str): The Message to show
        """
        if message != "":
            print(message)
            print("Exiting with Status: " + str(code))
        _sys.exit(code)

    @staticmethod
    def _string_to_list(string: str) -> list:
        """
        Convert a String to a List
        Args:
            string (str): The String to convert
        Returns:
            list: The List
        """
        return string.split(" ")
    
    @staticmethod
    def _list_to_string(list: list) -> str:
        """
        Convert a List to a String
        Args:
            list (list): The List to convert
        Returns:
            str: The String
        """
        return " ".join(list)

    @staticmethod
    def system(command: str, safe_output: bool = False, shell: bool = False, use_child: bool = False, use_os: bool = False) -> tuple[str, str]:
        """
        Run a Command and Optional get the Output
        Args:
            command (str): The Command to run
            safe_output (bool): Want you safe Output or not
            shell (bool): Use Shell
            use_child (bool): Use Child Process
        Warning:
            shell and use_child can not mixed
        Returns:
            tuple[str, str]: The stdout and stderr
        """
        command_list = _process._string_to_list(command)
        main_programm = command_list[0]
        cmd = _process.Command(program=main_programm, safe_output=safe_output)
        for i in range(1, len(command_list)):
            cmd.arg(command_list[i])
        cmd.run(shell=shell, use_child=use_child, use_os=use_os)
        return cmd.stdout(), cmd.stderr()
    
    @staticmethod
    def mkdir(path: str, exist_ok: bool = False):
        """
        Create a Directory
        Args:
            path (str): The Path to the Directory
            exist_ok (bool): Raise an Error if the Directory already exists
        """
        cmd = _process.Command(program="mkdir")
        if exist_ok:
            cmd.arg("-p")
        cmd.arg(path)
        cmd.run()

    @staticmethod
    def remove(path: str, file: bool = False, dir: bool = False):
        """
        Remove a File or Directory
        Args:
            path (str): The Path to the File or Directory
            file (bool): Remove a File
            dir (bool): Remove a Directory
        """
        cmd = _process.Command(program="rm")
        if file:
            cmd.arg("-f")
        elif dir:
            cmd.arg("-r")
        cmd.arg(path)
        cmd.run()

    @staticmethod
    def chmod(path: str, mode: int):
        """
        Change the Mode of a File or Directory
        Args:
            path (str): The Path to the File or Directory
            mode (int): The Mode to change to
        """
        cmd = _process.Command(program="chmod")
        cmd.arg(str(mode))
        cmd.arg(path)
        cmd.run()

    @staticmethod
    def chown(path: str, user: str, group: str = None, recursive: bool = False):
        """
        Change the Owner of a File or Directory
        Args:
            path (str): The Path to the File or Directory
            user (str): The User to change to
            group (str): The Group to change to
        """
        if group is None:
            group = user
        cmd = _process.Command(program="chown")
        if recursive:
            cmd.arg("-R")
        cmd.arg(user + ":" + group)
        cmd.arg(path)
        cmd.run()

    @staticmethod
    def sudo(command: str, user: str = "root", password: str = None, safe_output: bool = False, shell: bool = False, use_child: bool = False, use_os: bool = False) -> tuple[str, str]:
        """
        Run a Command as sudo
        Args:
            command (str): The Command to run
            user (str): The User to run the Command as
            password (str): The Password to run the Command as
        """
        cmd = _process.Command(program="sudo", safe_output=safe_output)
        cmd.arg("-u")
        cmd.arg(user)
        if password is not None:
            cmd.arg("-p")
            cmd.arg(password)
        cmd.args(_process._string_to_list(command))
        cmd.run(shell=shell, use_child=use_child, use_os=use_os)
        return cmd.stdout(), cmd.stderr()
    
    @staticmethod
    def symlink(original: str, link: str, dir: bool = False, file: bool = False) -> bool:
        """
        Create a Symlink to a File or Directory
        Args:
            original (str): The Original File or Directory
            link (str): The Link to the Original File or Directory
            dir (bool): Create a Directory Link
        """
        cmd = _process.Command(program="ln")
        if file:
            cmd.arg("-s")
            cmd.arg("-f")
        if dir:
            cmd.arg("-d")
        cmd.arg(original)
        cmd.arg(link)
        try:
            cmd.run()
            return True
        except:
            return False
    
def _PathLike(path: str) -> str:
    """
    Convert a Path to a Path like
    Args:
        path (str): The Path to convert
    Returns:
        str: The Path like
    """
    path = path.replace("\\", "/")
    path = path.replace("//", "/")
    path = path.replace("\\\\", "\\")
    path = path.replace("\\\\\\", "\\")
    path = path.replace("\\\\\\\\", "\\")
    path = path.replace("\\\\\\\\\\", "\\")
    path = path.replace("\\\\\\\\\\\\", "\\")
    path = path.replace("\\\\\\\\\\\\\\", "\\")
    if path.endswith("/"):
        path = path[:-1]
    return str(path)
    
class _path:
    """
    Class to Work with Paths
    """
    @staticmethod
    def PathLike(path: str) -> str:
        """
        Convert a Path to a Path like
        Args:
            path (str): The Path to convert
        Returns:
            str: The Path like
        """
        return _PathLike(path)

    @staticmethod
    def join(*args) -> str:
        """
        Join a Path
        Args:
            *args (str): The Paths to join
        Returns:
            str: The Joined Path
        """
        raw = "/".join(args)
        return _path.PathLike(raw)
    
    @staticmethod
    def exists(path: str) -> bool:
        """
        Check if path exists and return bool
        """
        # Versuche es ohne os zu validieren
        # Und ohne Externe Programme
        path = _path.PathLike(path)
        try:
            _os.stat(path)
            return True
        except:
            return False
        
    @staticmethod
    def url(path: str, domain: str, https: bool = False) -> str:
        """
        Convert a Path to a URL
        """
        path = _path.PathLike(path)
        if https:
            url_begin = "https://"
        else:
            url_begin = "http://"
        urlr = url_begin + domain + path
        return urlr
    
    @staticmethod
    def create(path: str) -> bool:
        """
        Create a Path
        Args:
            path (str): The Path to create
        Returns:
            bool: The Path created
        """
        path = _path.PathLike(path)
        if _path.exists(path):
            raise Exception("Path: " + path + " already exists")
        try:
            _process.mkdir(path, exist_ok=True)
            return True
        except:
            return False
        
    @staticmethod
    def basename(path: str) -> str:
        """
        Get the Base Name from the Path
        Args:
            path (str): The Path to get the Base Name from
        Returns:
            str: The Base Name
        """
        path = _path.PathLike(path)
        path_list = path.split("/")
        name = path_list[-1]
        return name
    
    @staticmethod
    def splitpath(path: str) -> tuple[str, str]:
        """
        Split the Full Extension from Name
        Args:
            path (str): The Path to split
        Returns:
            tuple[str, str]: The Name and the Extension
        """
        path = _path.PathLike(path)
        basename = _path.basename(path)
        name = basename.split(".")[0]
        extension = basename.split(name)[1:]
        return name, extension
    
class _styling:
    """
    Class for Styling
    """
    def __init__(self):
        """
        Initial the Class Correctly
        """
        self.color = _styling._color()
        self.style = _styling._style()
        self.reset = "\033[0m"
    class _color:
        """
        Class for Coloring
        """
        def __init__(self):
            """
            Initial the Class Correctly
            """
            self.background = _styling._color._background()
            self.foreground = _styling._color._foreground()
        class _background:
            """
            Class for Background Coloring
            """
            @staticmethod
            def red() -> str:
                """
                Get Red Color for Background
                """
                return "\033[41m"
            
            @staticmethod
            def green() -> str:
                """
                Get Green Color for Background
                """
                return "\033[42m"
            
            @staticmethod
            def yellow() -> str:
                """
                Get Yellow Color for Background
                """
                return "\033[43m"
            
            @staticmethod
            def blue() -> str:
                """
                Get Blue Color for Background
                """
                return "\033[44m"
            
            @staticmethod
            def magenta() -> str:
                """
                Get Magenta Color for Background
                """
                return "\033[45m"
            
            @staticmethod
            def cyan() -> str:
                """
                Get Cyan Color for Background
                """
                return "\033[46m"
            
            @staticmethod
            def white() -> str:
                """
                Get White Color for Background
                """
                return "\033[47m"
        
        class _foreground:
            """
            Class for Foreground Coloring
            """
            @staticmethod
            def red() -> str:
                """
                Get Red Color for Foreground
                """
                return "\033[31m"
            
            @staticmethod
            def green() -> str:
                """
                Get Green Color for Foreground
                """
                return "\033[32m"
            
            @staticmethod
            def yellow() -> str:
                """
                Get Yellow Color for Foreground
                """
                return "\033[33m"
            
            @staticmethod
            def blue() -> str:
                """
                Get Blue Color for Foreground
                """
                return "\033[34m"
            
            @staticmethod
            def magenta() -> str:
                """
                Get Magenta Color for Foreground
                """
                return "\033[35m"
            
            @staticmethod
            def cyan() -> str:
                """
                Get Cyan Color for Foreground
                """
                return "\033[36m"
            
            @staticmethod
            def white() -> str:
                """
                Get White Color for Foreground
                """
                return "\033[37m"
            
        
    class _style:
        """
        Class for Styling
        """
        @staticmethod
        def bold() -> str:
            """
            Get the Bold Style
            """
            return "\033[1m"
        
        @staticmethod
        def italic() -> str:
            """
            Get the Italic Style
            """
            return "\033[2m"
        
        @staticmethod
        def underline() -> str:
            """
            Get the Underline Style
            """
            return "\033[4m"
        
        @staticmethod
        def strikethrough() -> str:
            """
            Get the Strikethrough Style
            """
            return "\033[9m"
        
        @staticmethod
        def blink() -> str:
            """
            Get the Blink Style
            """
            return "\033[5m"
        
        @staticmethod
        def reverse() -> str:
            """
            Get the Reverse Style
            """
            return "\033[7m"
        
        @staticmethod
        def invisible() -> str:
            """
            Get the Invisible Style
            """
            return "\033[8m"
        
class _archive:
    """
    Class for work with Archives
    """
    def __init__(self):
        """
        Initial the Class without an Argument
        """
        self._type = None
        self._name = None
        self._extension = None
        self._path = None
        self._mode = None
        self._opened = False
        self._instance = None

    def open(self, file_path: str, mode: str = "r") -> bool:
        """
        Open an Archive, automatically detect the type
        Args:
            file_path (str): The Path to the Archive
            mode (str): The Mode to open the Archive
        Returns:
            bool: The Archive opened
        """
        basename = _path.basename(file_path)
        if basename.endswith(".zip"):
            import zipfile
            self._type = "zip"
            self._name, self._extension = _path.splitpath(file_path)
            self._path = file_path
            self._mode = mode
            try:
                self._instance = zipfile.ZipFile(file=file_path, mode=mode)
                self._opened = True
            except:
                self._instance = None
                self._opened = False
            return self._opened
        elif basename.endswith(".tar"):
            import tarfile
            self._type = "tar"
            self._name, self._extension = _path.splitpath(file_path)
            self._path = file_path
            self._mode = mode
            try:
                self._instance = tarfile.open(file_path, mode)
                self._opened = True
            except:
                self._instance = None
                self._opened = False
            return self._opened
        elif basename.endswith(".tar.xz"):
            import tarfile
            import lzma
            self._type = "tar.xz"
            self._name, self._extension = _path.splitpath(file_path)
            self._path = file_path
            self._mode = mode
            try:
                self._instance = tarfile.open(file_path, mode)
                self._opened = True
            except:
                self._instance = None
                self._opened = False
            return self._opened
        elif basename.endswith(".tar.gz"):
            import tarfile
            import gzip
            self._type = "tar.gz"
            self._name, self._extension = _path.splitpath(file_path)
            self._path = file_path
            self._mode = mode
            try:
                self._instance = tarfile.open(file_path, mode)
                self._opened = True
            except:
                self._instance = None
                self._opened = False
            return self._opened
        elif basename.endswith(".tar.bz2"):
            import tarfile
            import bz2
            self._type = "tar.bz2"
            self._name, self._extension = _path.splitpath(file_path)
            self._path = file_path
            self._mode = mode
            try:
                self._instance = tarfile.open(file_path, mode)
                self._opened = True
            except:
                self._instance = None
                self._opened = False
            return self._opened
        else:
            raise Exception("Unsupported Archive Type")
        
    def add(self, path: str, instance: any = None):
        """
        Add a File or Directory to the Archive
        Args:
            path (str): The Path to the File or Directory
            instance (any): The Instance to add the File or Directory to
        """
        if instance is None:
            instance = self._instance
        try:
            if self._type == "zip":
                instance.write(path)
                check = True
            elif self._type == "tar":
                instance.add(path)
                check = True
            elif self._type == "tar.xz":
                instance.add(path)
                check = True
            elif self._type == "tar.gz":
                instance.add(path)
                check = True
            elif self._type == "tar.bz2":
                instance.add(path)
                check = True
            else:
                raise Exception("Unsupported Archive Type")
        except:
            raise Exception("Failed to add File or Directory to Archive")
        return check
    
    def remove(self, path: str, instance: any = None) -> bool:
        """
        Remove a File or Directory from the Archive
        Args:
            path (str): The Path to the File or Directory
            instance (any): The Instance to remove the File or Directory from
        Returns:
            bool: The File or Directory removed
        """
        try:
            if self._type == "zip":
                instance.remove(path)
                check = True
            elif self._type == "tar":
                instance.remove(path)
                check = True
            elif self._type == "tar.xz":
                instance.remove(path)
                check = True
            elif self._type == "tar.gz":
                instance.remove(path)
                check = True
            elif self._type == "tar.bz2":
                instance.remove(path)
                check = True
            else:
                raise Exception("Unsupported Archive Type")
        except:
            raise Exception("Failed to remove File or Directory from Archive")
        return check
    
    def extract(self, path: str, instance: any = None) -> bool:
        """
        Extract a File or Directory from the Archive
        Args:
            path (str): The Path to the File or Directory
            instance (any): The Instance to extract the File or Directory from
        """
        if instance is None:
            instance = self._instance
        try:
            if self._type == "zip":
                instance.extract(path)
                check = True
            elif self._type == "tar":
                instance.extract(path)
                check = True
            elif self._type == "tar.xz":
                instance.extract(path)
                check = True
            elif self._type == "tar.gz":
                instance.extract(path)
                check = True
            elif self._type == "tar.bz2":
                instance.extract(path)
                check = True
            else:
                raise Exception("Unsupported Archive Type")
        except:
            raise Exception("Failed to extract File or Directory from Archive")
        return check
    
    def list(self, instance: any = None) -> list:
        """
        List the Files and Directories in the Archive
        """
        if instance is None:
            instance = self._instance
        try:
            if self._type == "zip":
                return instance.namelist()
            elif self._type == "tar":
                return instance.getnames()
            elif self._type == "tar.xz":
                return instance.getnames()
            elif self._type == "tar.gz":
                return instance.getnames()
            elif self._type == "tar.bz2":
                return instance.getnames()
            else:
                raise Exception("Unsupported Archive Type")
        except:
            raise Exception("Failed to list Files and Directories in Archive")
        
    def close(self):
        """
        Close the Archive
        """
        self._instance.close()
        self._opened = False
        self._instance = None

    def get_type(self) -> str:
        """
        Get the Type of the Archive
        """
        return self._type
    
    def get_name(self) -> str:
        """
        Get the Name of the Archive
        """
        return self._name
    
    def get_extension(self) -> str:
        """
        Get the Extension of the Archive
        """
        return self._extension
    
    def get_path(self) -> str:
        """
        Get the Path of the Archive
        """
        return self._path
    
    def get_mode(self) -> str:
        """
        Get the Mode of the Archive
        """
        return self._mode
    
    def close(self):
        """
        Close the Archive
        """
        self._instance.close()
        self._opened = False
        self._instance = None

class _environ:
    """
    Class to Work with Environment Variables
    """
    @staticmethod
    def get(name: str) -> str:
        """
        Get the Environment Variable
        """
        # Ohne Os Modul
        path = '/proc/self/environ'
        path = _path.PathLike(path)
        with open(path, 'r') as file:
            content = file.read()
            file.close()
        content_split = content.split('\x00')
        for i in content_split:
            if i.split("=")[0] == name:
                return i.split("=")[1]
        return None
    
    @staticmethod
    def set(name: str, value: str) -> bool:
        """
        Set an Environment Variable
        """
        path = '/proc/self/environ'
        path = _path.PathLike(path)
        try:
            with open(path, 'a') as file:
                file.write(name + "=" + value)
                file.close()
            return True
        except:
            return False
        
    @staticmethod
    def from_file(path: str, name: str) -> str:
        """
        Get an Environment Variable from a .env File
        """
        path = _path.PathLike(path)
        with open(path, 'r') as file:
            content = file.read()
            file.close()
        content_split = content.split('\n')
        for i in content_split:
            if i.split("=")[0] == name:
                return i.split("=")[1]
        return None
    
    @staticmethod
    def print(name: str) -> None:
        """
        Print a Environment Variable
        """
        print(_environ.get(name))

class _math:
    """
    Class to Work with Math Operations
    """

    @staticmethod
    def add(*args: int) -> int:
        """
        Add Numbers
        """
        result = 0
        for i in args:
            result += i
        return result

    @staticmethod
    def sub(*args: int) -> int:
        """
        Subtract Numbers
        """
        result = args[0]
        for i in args[1:]:
            result -= i
        return result

    @staticmethod
    def mul(*args: int) -> int:
        """
        Multiply Numbers
        """
        result = 1
        for i in args:
            result *= i
        return result

    @staticmethod
    def div(*args: int) -> float:
        """
        Divide Numbers
        """
        result = args[0]
        for i in args[1:]:
            result /= i
        return result

    @staticmethod
    def exp(x: int = 0, exponent: int = 2) -> int:
        """
        Get an Exponent
        """
        return x ** exponent

    @staticmethod
    def pq(p: int, q: int) -> tuple[float, float]:
        """
        Use the pq Formula to get x1 and x2
        For equations of the form x^2 + px + q = 0
        """
        x1 = -(p / 2) + (((p / 2) ** 2) - q) ** 0.5
        x2 = -(p / 2) - (((p / 2) ** 2) - q) ** 0.5
        return x1, x2

    @staticmethod
    def quadratic(a: int, b: int, c: int) -> tuple[float, float]:
        """
        Use the Quadratic Formula to get x1 and x2
        For equations of the form ax^2 + bx + c = 0
        """
        discriminant = b ** 2 - 4 * a * c
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return x1, x2

    @staticmethod
    def factorial(x: int) -> int:
        """
        Get the Factorial of a Number
        """
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

    @staticmethod
    def permutation(n: int, r: int) -> int:
        """
        Get the Permutation of a Number
        """
        return _math.factorial(n) / _math.factorial(n - r)

    @staticmethod
    def logarithm(base: int = 10, x: int = 1, n: int = 1000000) -> float:
        """
        Get the Logarithm of a Number
        """
        if x <= 0 or base <= 1:
            raise ValueError("x must be greater than 0 and base must be greater than 1")
        e_approx = (1 + 1 / n) ** n

        ln_x = 0
        while x >= e_approx:
            x /= e_approx
            ln_x += 1

        while x > 1:
            x /= e_approx ** (1 / n)
            ln_x += 1 / n

        ln_base = 0
        temp_base = base
        while temp_base >= e_approx:
            temp_base /= e_approx
            ln_base += 1

        while temp_base > 1:
            temp_base /= e_approx ** (1 / n)
            ln_base += 1 / n

        return ln_x / ln_base

    @staticmethod
    def speed_up(a: float, b: float, c: float) -> float:
        """
        Get a Better target Value based on 3 Values from the same Formula
        """
        numerator = (a * c - b ** 2)
        denominator = (a + c - 2 * b)
        return numerator / denominator

    @staticmethod
    def switch(x: float) -> float:
        """
        Get the Reciprocal of a Number
        """
        return 1 / x

    @staticmethod
    def arctan(x: float, n: int = 1000000) -> float:
        """
        Get the Arcus Tangens Value using Taylor series
        """
        result = 0
        for i in range(n):
            term = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
            result += term
        return result

    @staticmethod
    def arctan2(x: float, n: int = 1000000) -> float:
        """
        Get a Better Value with Splitting
        """
        if x >= 1:
            return _math.arctan(x, n)
        else:
            raw = _math.switch(x)
            a = _math.switch(raw + 1)
            b = (x - a) / (1 + a * x)
            return _math.arctan(a, n) + _math.arctan(b, n)

    @staticmethod
    def arctan3(x: float, n: int = 1000000) -> float:
        """
        Get a Better Value with the Speed Up Formula
        """
        na = n - 1
        nb = n
        nc = n + 1
        y1 = _math.arctan(x, na)
        y2 = _math.arctan(x, nb)
        y3 = _math.arctan(x, nc)
        return _math.speed_up(y1, y2, y3)
    
    @staticmethod
    def get_pi(n: int = 1000000) -> float:
        """
        Get the Value from PI
        """
        pi = 4 * (_math.arctan2(x=(1/2), n=n) + _math.arctan2(x=(1/3), n=n))
        return pi
    
    @staticmethod
    def fakultaet(x: int) -> int:
        """
        Get the Fakultaet of a Number
        """
        if x == 0:
            return 1
        else:
            return x * _math.fakultaet(x - 1)


Path = _path()
Styling = _styling()
Process = _process()
Archive = _archive()
Environ = _environ()
Math = _math()
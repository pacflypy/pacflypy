import pacflypy.command as command
import pacflypy.string as string
import pacflypy.system as system
import platform

if platform.system().lower() == 'windows':
    raise Exception('Windows is not supported')

class open:
    """
    Connect you to A Tar Archive
    """
    def __init__(self, path: str, mode: str = 'r') -> None:
        import os
        """
        Open Tar Archive and Works with Him
        Modes:
        'w' - Write
        'w:xz' - Write XZ
        'w:gz' - Write GZ
        'r' - Read
        'r:xz' - Read XZ
        'r:gz' - Read GZ
        """
        name, suffix = os.path.splitext(path)
        self.path = path
        self.mode = mode
        self.cmd = command.command(programm='tar')
        if self.mode == 'w':
            self.cmd.arg('-cf')
        elif self.mode == 'w:xz':
            self.cmd.arg('-cJf')
        elif self.mode == 'w:gz':
            self.cmd.arg('-cZf')
        elif self.mode == 'r':
            self.cmd.arg('-xf')
        elif self.mode == 'r:xz':
            self.cmd.arg('-xJf')
        elif self.mode == 'r:gz':
            self.cmd.arg('-xZf')
        self.cmd.arg(self.path)
        self.cmd.arg(f'--suffix={suffix}')


    def add(self, path: str) -> None:
        """
        Add File to Archive
        """
        self.cmd.arg(path)

    def remove(self, path: str) -> None:
        """
        Remove File From Archive
        """
        self.cmd.remove(path)

    def extract(self, path: str) -> None:
        """
        Extract File From Archive
        """
        self.cmd.arg('-C')
        self.cmd.arg(path)

    def close(self) -> None:
        """
        Close Tar Archive
        """
        import sys
        sys.exit(1)
import tarfile as _tarfile
import os as _os

class open:
    """
    A class that provides an interface to work with tar archives.
    """
    def __init__(self, path: str, mode: str = 'r'):
        """
        Opens a tar archive in the specified mode.
        Supported modes are: 'r', 'w', 'x' (read, write, exclusive write).
        """
        self.path = path
        self.mode = mode
        self.tar = None

    def open(self):
        """
        Opens the tar archive.
        """
        if self.mode in ['r', 'w', 'x']:
            self.tar = _tarfile.open(self.path, self.mode + '|')
        else:
            raise ValueError("Invalid mode: Only 'r', 'w', 'x' are allowed.")

    def add(self, path: str):
        """
        Adds a file or directory to the tar archive.
        """
        if self.tar:
            self.tar.add(path, arcname=_os.path.basename(path))
        else:
            raise Exception("Tar archive is not opened.")

    def extract(self, member, path=""):
        """
        Extracts a member from the tar archive.
        """
        if self.tar:
            self.tar.extract(member, path)
        else:
            raise Exception("Tar archive is not opened.")

    def list(self):
        """
        Lists all members of the tar archive.
        """
        if self.tar:
            return self.tar.getmembers()
        else:
            raise Exception("Tar archive is not opened.")

    def close(self):
        """
        Closes the tar archive.
        """
        if self.tar:
            self.tar.close()
        else:
            raise Exception("Tar archive is not opened.")

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
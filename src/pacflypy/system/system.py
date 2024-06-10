from pacflypy.command import command
import pacflypy.command as comd
from pacflypy.exceptions import FileInvalid

def mkdir(path: str, exist_ok: bool = False) -> bool:
    if exist_ok:
        try:
            cmd = command(programm='mkdir')
            cmd.arg('-p')
            cmd.arg(path)
            cmd.run()
            status = True
        except comd.ActionWasExecuted:
            status = False
    else:
        try:
            cmd = command(programm='mkdir')
            cmd.arg(path)
            cmd.run()
            status = True
        except comd.ActionWasExecuted:
            status = False
    return status

def run(run_command: str, safe_output: bool = False, shell: bool = False) -> tuple[str, str]:
    command_parts = run_command.split(' ')
    cmd = command(programm=command_parts[0], safe_output=safe_output, shell=shell)
    for i in range(1, len(command_parts)):
        cmd.arg(command_parts[i])
    cmd.run()
    stdout = cmd.stdout()
    stderr = cmd.stderr()
    return stdout, stderr

def remove(path: str, dir: bool = False) -> bool:
    if dir:
        cmd = command(programm='rm')
        cmd.arg('-rf')
        cmd.arg(path)
        cmd.run()
        status = True
    else:
        cmd = command(programm='rm')
        cmd.arg(path)
        cmd.run()
        status = True

class path:
    """
    Class for Working with Paths
    """
    @staticmethod
    def exists(path: str) -> bool:
        import platform
        if platform.system().lower() == 'Windows':
            cmd = command(programm='dir', safe_output=True)
            cmd.arg(path)
            cmd.run()
            stdout = cmd.stdout()
            stderr = cmd.stderr()
            if stdout == '' and stderr == '':
                return False
            else:
                return True
        else:
            cmd = command(programm='ls', safe_output=True)
            cmd.arg(path)
            cmd.run()
            stdout = cmd.stdout()
            stderr = cmd.stderr()
            if stdout == '' and stderr == '':
                return False
            else:
                return True
    
    @staticmethod
    def join(*paths: str) -> str:
        string = '/' + '/'.join(paths)
        string = string.replace('\\', '/')
        string = string.replace('//', '/')
        return string
    
    @staticmethod
    def split(path: str) -> tuple[str, str]:
        path = path.replace('\\', '/')
        path = path.replace('//', '/')
        path = path.split('/')
        return path
    

class environ:
    """
    Class to Work with Environment Variables
    """
    @staticmethod
    def get(key: str) -> str:
        import platform
        if platform.system().lower() == 'Windows':
            cmd = command(programm='set', safe_output=True)
            cmd.arg(key)
            cmd.run()
            stdout = cmd.stdout()
            stderr = cmd.stderr()
            if stdout == '' and stderr == '':
                return ''
            else:
                return stdout
        else:
            cmd = command(programm='printenv', safe_output=True)
            cmd.arg(key)
            cmd.run()
            stdout = cmd.stdout()
            stderr = cmd.stderr()
            if stdout == '' and stderr == '':
                return ''
            else:
                return stdout
    
    @staticmethod
    def file(path: str, key: str) -> str:
        if not path.endswith('.env') or path.endswith('.sh') or path.endswith('.bash') or path.endswith('.pacfly'):
            raise FileInvalid(file=path, message='File Invalid')
        with open(path, 'r') as file:
            data = file.read()
            dictionary = {}
        for line in data.split('\n'):
            if line:
                rkey, rvalue = line.split('=')
                dictionary[rkey] = rvalue
        return dictionary[key]
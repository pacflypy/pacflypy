import tarfile
import gzip
import lzma
import json
import os
import time
import shutil
import tempfile

_yaml_support = False
_toml_support = False
_json_support = True
_defualt_support = _json_support

try:
    import ruamel.yaml
    _yaml_support = True
except ModuleNotFoundError:
    _yaml_support = False

try:
    import toml
    _toml_support = True
except ModuleNotFoundError:
    _toml_support = False

_open = tarfile.open

class _Time:
    """
    Class To Work with times
    """
    def __init__(self):
        """
        Nothin to Do
        """
        import datetime
        self.date_time = datetime.datetime.now()
    def time(self):
        """
        Get Time
        """
        return self.date_time.time()
    def date(self):
        """
        Get Date
        """
        return self.date_time.date()
    
def _check_output(command: list):
    """
    Check Output from Command
    """
    import subprocess
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    stdout = stdout.strip()
    stderr = stderr.strip()
    if stdout:
        return stdout
    elif stderr:
        return stderr
    else:
        return None
    
def _string_to_list(string: str) -> list:
    """
    Convert String to List
    """
    return string.split(" ")

def _list_to_string(liste: list) -> str:
    """
    Convert List to String
    """
    return " ".join(liste)

class _SupportNotAvailable(Exception):
    """
    Exception Class for Unsupported Meta File Types
    """
    def __init__(self, *args):
        self.args = args
        super().__init__(self.args)

def _dump_log(file_instance, data: dict):
    """
    Dump Log File
    """
    for key, value in data.items():
        file_instance.write(f"{key}: {value}\n")

def Instance(name: str, mode: str = 'r', bufsize: int = 10240):
    """
    Open an Flypy Tar Archive and Create an Instance
    """
    _open(name=name, mode=mode, bufsize=bufsize)

def _create_meta(filepath: str, typ: str = 'json'):
    """
    Create Meta Data File for flypy Tar
    """
    start_time_1 = time.time()
    meta = {}
    if typ != 'json':
        if typ == 'yaml' or typ == 'yml':
            if not _yaml_support:
                raise _SupportNotAvailable("Ruamel.yaml not Found")
        elif typ == 'toml':
            if not _toml_support:
                raise _SupportNotAvailable("Toml not Found")
        else:
            raise _SupportNotAvailable(f"{typ} is Invalid")
    file_name = os.path.basename(filepath)
    name, ext = os.path.splitext(file_name)
    meta['init']['start'] = [_Time().date(), _Time().time()]
    meta['init']['name'] = name
    meta[name]['file'] = file_name
    meta[name]['basename'] = name
    meta[name]['extension'] = ext
    end_time_1 = time.time()
    meta[name]['FileScanTime'] = end_time_1 - start_time_1
    start_time_2 = time.time()
    if typ == 'json':
        output_file = f"{name}.json"
    elif typ == 'yaml' or typ == 'yml':
        output_file = f"{name}.yml"
    elif typ == 'toml':
        output_file = f"{name}.toml"
    command_str_mb = f"du -sh {filepath} | awk '{{print $1}}'"
    command_str_kb = f"du -sk {filepath} | awk '{{print $1}}'"
    command_str_b = f"du -sb {filepath} | awk '{{print $1}}'"
    meta[name]['FileSize_MB'] = _check_output(_string_to_list(command_str_mb))
    meta[name]['FileSize_KB'] = _check_output(_string_to_list(command_str_kb))
    meta[name]['FileSize_B'] = _check_output(_string_to_list(command_str_b))
    end_time_2 = time.time()
    meta[name]['FileSizeTime'] = end_time_2 - start_time_2
    meta['init']['end_time'] = end_time_2 - start_time_1
    meta['init']['end'] = [_Time().date(), _Time().time()]
    with open(output_file, 'w') as file:
        if typ == 'json':
            json.dump(meta, file, indent=4)
        elif typ == 'yaml' or typ == 'yml':
            ruamel.yaml.dump(meta, file)
        elif typ == 'toml':
            toml.dump(meta, file)
    return meta

def add(tar_instance, filepath: str, typ: str = 'json'):
    """
    Add a File to flytar Archive
    """
    meta = _create_meta(filepath=filepath, typ=typ)
    name = meta['init']['name']
    if typ == 'json':
        output_file = f"{name}.json"
    elif typ == 'yaml' or typ == 'yml':
        output_file = f"{name}.yml"
    elif typ == 'toml':
        output_file = f"{name}.toml"
    tar_instance.add(filepath)
    tar_instance.add(output_file)
    os.remove(output_file)

def remove(tar_instance, filename: str, typ: str = 'json'):
    """
    Remove a File from flytar Archive
    """
    tar_instance.remove(filename)
    if typ == 'json':
        tar_instance.remove(f"{filename}.json")
    elif typ == 'yaml' or typ == 'yml':
        tar_instance.remove(f"{filename}.yml")
    elif typ == 'toml':
        tar_instance.remove(f"{filename}.toml")


def extract(tar_instance, path: str):
    """
    Extract all Files from Archive
    """
    name = tar_instance.name
    start_time_1 = time.time()
    data = {}
    data['init'] = {}
    data['init']['start'] = [_Time().date(), _Time().time()]
    data['init']['name'] = tar_instance.name
    data['init']['end_time'] = 0
    data['init']['end'] = [0, 0]
    tempdir = tempfile.TemporaryDirectory()
    tdir = tempdir.name
    cdir = os.getcwd()
    log_file = os.path.join(cdir, f'{tar_instance.name}.log')
    output_path = os.path.join(path, tar_instance.name)
    os.makedirs(output_path, exist_ok=True)
    data['target'] = output_path
    os.makedirs(output_path, exist_ok=True)
    meta_path = os.path.join(tdir, 'meta')
    content_path = os.path.join(tdir, 'content')
    tar_instance.extractall(tdir)
    files = os.listdir(tdir)
    for file in files:
        if file:
            if file == 'meta' or file == 'content':
                continue
            elif file.endswith('.yml') or file.endswith('.json') or file.endswith('.toml'):
                end_path = os.path.join(meta_path, file)
                shutil.copy(os.path.join(tdir, file), end_path)
                data[file.split('.')[0]] = end_path
                os.remove(os.path.join(tdir, file))
            else:
                end_path = os.path.join(content_path, file)
                shutil.copy(os.path.join(tdir, file), end_path)
                data[file] = end_path
                os.remove(os.path.join(tdir, file))
    end_time_1 = time.time()
    data[name]['SortTime'] = end_time_1 - start_time_1
    start_time_2 = time.time()
    files = os.listdir(meta_path)
    for file in files:
        if file:
            file_path = os.path.join(meta_path, file)
            if file.endswith('.json'):
                with open(file_path, 'r') as f:
                    file_content = json.load(f)
                file_name = os.path.basename(file_path)
                n, e = os.path.splitext(file_name)
                data[n]['file'] = file_name
                data[n]['content'] = file_content
                data[n]['type'] = 'json'
            elif file.endswith('.yaml') or file.endswith('.yml'):
                if not _yaml_support:
                    raise _SupportNotAvailable("Ruamel.yaml not Found")
                with open(file_path, 'r') as f:
                    file_content = ruamel.yaml.load(f)
                file_name = os.path.basename(file_path)
                n, e = os.path.splitext(file_name)
                data[n]['file'] = file_name
                data[n]['content'] = file_content
                data[n]['type'] = 'yaml'
            elif file.endswith('.toml'):
                if not _toml_support:
                    raise _SupportNotAvailable("Toml not Found")
                with open(file_path, 'r') as f:
                    file_content = toml.load(f)
                file_name = os.path.basename(file_path)
                n, e = os.path.splitext(file_name)
                data[n]['file'] = file_name
                data[n]['content'] = file_content
                data[n]['type'] = 'toml'
    end_time_2 = time.time()
    data[name]['ReadTime'] = end_time_2 - start_time_2
    data['init']['end_time'] = end_time_2 - start_time_1
    data['init']['end'] = [_Time().date(), _Time().time()]
    with open(log_file, 'w') as file:
        _dump_log(file, data)
    shutil.copy(content_path, output_path)
    tempdir.cleanup()
    return data
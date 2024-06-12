import tarfile
import json
import os
import time
import shutil
import tempfile
from datetime import datetime

# Unterstützung für verschiedene Formate prüfen
_yaml_support, _toml_support = False, False
try:
    import ruamel.yaml
    _yaml_support = True
except ModuleNotFoundError:
    pass

try:
    import toml
    _toml_support = True
except ModuleNotFoundError:
    pass

def get_current_time():
    now = datetime.now()
    return now.date(), now.time()

class SupportNotAvailable(Exception):
    pass

def create_meta(filepath: str, typ: str = 'json'):
    start_time = time.time()
    date, current_time = get_current_time()
    file_name = os.path.basename(filepath)
    name, ext = os.path.splitext(file_name)
    meta = {
        'init': {'start': [date, current_time], 'name': name},
        name: {
            'file': file_name,
            'basename': name,
            'extension': ext,
            'FileScanTime': time.time() - start_time
        }
    }

    if typ not in ['json', 'yaml', 'yml', 'toml']:
        raise ValueError(f"{typ} is an invalid type")

    if typ == 'yaml' and not _yaml_support:
        raise SupportNotAvailable("Ruamel.yaml not found")
    if typ == 'toml' and not _toml_support:
        raise SupportNotAvailable("Toml not found")

    output_file = f"{name}.{typ if typ != 'yml' else 'yaml'}"
    with open(output_file, 'w') as file:
        if typ == 'json':
            json.dump(meta, file, indent=4)
        elif typ in ['yaml', 'yml']:
            ruamel.yaml.dump(meta, file)
        elif typ == 'toml':
            toml.dump(meta, file)

    return meta

def add(tar_instance, filepath: str, typ: str = 'json'):
    meta = create_meta(filepath, typ)
    name = meta['init']['name']
    output_file = f"{name}.{typ if typ != 'yml' else 'yaml'}"
    tar_instance.add(filepath)
    tar_instance.add(output_file)
    os.remove(output_file)

def remove(tar_instance, filename: str, typ: str = 'json'):
    tar_instance.remove(filename)
    meta_file = f"{filename}.{typ if typ != 'yml' else 'yaml'}"
    tar_instance.remove(meta_file)

def extract(tar_instance, path: str):
    start_time = time.time()
    date, current_time = get_current_time()
    data = {
        'init': {
            'start': [date, current_time],
            'name': tar_instance.name,
            'end_time': 0,
            'end': [0, 0]
        }
    }
    tempdir = tempfile.TemporaryDirectory()
    tdir = tempdir.name
    output_path = os.path.join(path, tar_instance.name)
    os.makedirs(output_path, exist_ok=True)
    tar_instance.extractall(tdir)
    meta_path = os.path.join(tdir, 'meta')
    content_path = os.path.join(tdir, 'content')
    os.makedirs(meta_path, exist_ok=True)
    os.makedirs(content_path, exist_ok=True)

    for file in os.listdir(tdir):
        if file.endswith(('.yml', '.json', '.toml')):
            shutil.move(os.path.join(tdir, file), os.path.join(meta_path, file))
        else:
            shutil.move(os.path.join(tdir, file), os.path.join(content_path, file))

    # Metadaten und Inhalte verarbeiten
    for file in os.listdir(meta_path):
        file_path = os.path.join(meta_path, file)
        if file.endswith('.json'):
            with open(file_path, 'r') as f:
                file_content = json.load(f)
            data[file.split('.')[0]] = {'content': file_content, 'type': 'json'}
        elif file.endswith('.yaml') or file.endswith('.yml'):
            with open(file_path, 'r') as f:
                file_content = ruamel.yaml.load(f)
            data[file.split('.')[0]] = {'content': file_content, 'type': 'yaml'}
        elif file.endswith('.toml'):
            with open(file_path, 'r') as f:
                file_content = toml.load(f)
            data[file.split('.')[0]] = {'content': file_content, 'type': 'toml'}

    tempdir.cleanup()
    data['init']['end_time'] = time.time() - start_time
    data['init']['end'] = get_current_time()
    return data
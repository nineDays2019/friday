import json
import os

DEFAULT_CLOUD_DIR = 'media/upload/'


def cloud_dir():
    config_file_path = 'cloud/config.json'
    if not os.path.exists(config_file_path):
        return DEFAULT_CLOUD_DIR
    with open(config_file_path, 'r') as file:
        path = json.load(file)['cloud_dir']
        if path == '':
            return DEFAULT_CLOUD_DIR
        return path

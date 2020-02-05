import json
import os

CLOUD_DIR = ''
DEFAULT_CLOUD_DIR = 'media/upload/'


def cloud_dir():
    global CLOUD_DIR
    if CLOUD_DIR == '':
        config_file_path = 'config.json'
        if not os.path.exists(config_file_path):
            CLOUD_DIR = DEFAULT_CLOUD_DIR
            return CLOUD_DIR
        with open(config_file_path, 'r') as file:
            CLOUD_DIR = json.load(file.read())['cloud_dir']
            if CLOUD_DIR == '':
                CLOUD_DIR = DEFAULT_CLOUD_DIR
            return CLOUD_DIR
    else:
        return CLOUD_DIR

import os
import configparser
from config.constants import WEAVIATE


def get_settings():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config = configparser.ConfigParser()
    config.read(dir_path + "\local_config.ini")
    return config


settings_config = get_settings()
weaviate_config = settings_config[WEAVIATE]


if __name__ == '__main__':
    pass

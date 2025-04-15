import configparser
import os

def read_config(section, key):
    config = configparser.ConfigParser()
    config.read(os.path.join("Configuration", "config.ini"))
    return config.get(section, key)

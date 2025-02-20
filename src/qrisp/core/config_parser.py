import configparser
import os

def load_config():
    
    config = configparser.ConfigParser()
    #path of the config.ini
    config_path = os.path.join(os.path.dirname(__file__),'config.ini')

    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")
    
    config.read(config_path)
    
    return config, config_path


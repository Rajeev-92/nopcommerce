import configparser
import os

config = configparser.RawConfigParser()
config.read('.\\configuration\\config.ini')

class read_config:
    @staticmethod
    def get_admin_page_url():
        url=config.get('admin login info','admin_page_url')
        return url
    @staticmethod
    def get_username():
        username=config.get('admin login info','username')
        return username
    @staticmethod
    def get_password():
        password=config.get('admin login info', 'password')
        return password
    @staticmethod
    def get_invalid_username():
        invalid_username=config.get('admin login info', 'invalid_username')
        return invalid_username
    @staticmethod
    def get_invalid_password():
        invalid_password=config.get('admin login info', 'invalid_password')
        return invalid_password
    @staticmethod
    def get_blank_username():
        blank_username=config.get('admin login info', 'blank_username')
        return blank_username
    @staticmethod
    def get_blank_password():
        blank_password=config.get('admin login info', 'blank_password')
        return blank_password

import configparser
import os

config = configparser.ConfigParser()

# Build absolute path to config.ini
config_path = os.path.join(os.path.dirname(__file__), '..', 'configuration', 'config.ini')
config.read(config_path)

def get_admin_page_url():
    return config.get('admin login info', 'admin_page_url')

def get_username():
    return config.get('admin login info', 'username')

def get_password():
    return config.get('admin login info', 'password')

def get_invalid_username():
    return config.get('admin login info', 'invalid_username')

def get_invalid_password():
    return config.get('admin login info', 'invalid_password')

def get_blank_username():
    return config.get('admin login info', 'blank_username')

def get_blank_password():
    return config.get('admin login info', 'blank_password')
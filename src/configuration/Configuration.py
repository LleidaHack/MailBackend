import os
import types
import yaml


class Configuration:
    _FILE = None
    __CONFIG_PATH = os.path.join('src', 'configuration')
    __CONFIG_FILES = None

    @staticmethod
    def __get_yaml_files():
        yaml_files = []
        for file in os.listdir(Configuration.__CONFIG_PATH):
            if file.endswith('.yaml'):
                yaml_files.append(file)
        return yaml_files

    def __init__(self, file=None) -> None:
        '''Resets the configuration and loads the config file'''
        # Reset class state for every instance creation
        self.reset()

        if Configuration._FILE is None:
            Configuration.__CONFIG_FILES = Configuration.__get_yaml_files()
            if file is None:
                if len(Configuration.__CONFIG_FILES) > 1:
                    raise Exception(
                        'Please select a configuration file to load')
                file = Configuration.__CONFIG_FILES[0]
            Configuration._FILE = os.path.join(Configuration.__CONFIG_PATH,
                                               file)
            self.__instanciate__()

    @staticmethod
    def __instanciate_nested(k, v, c):
        setattr(c, k, types.SimpleNamespace())
        for kk, vv in v.items():
            if type(vv) == dict:
                Configuration.__instanciate_nested(kk, vv, getattr(c, k))
            else:
                setattr(getattr(c, k), kk, vv)

    def __instanciate__(self):
        with open(Configuration._FILE) as f:
            data = yaml.safe_load(f)
            for k, v in data.items():
                if type(v) == dict:
                    self.__instanciate_nested(k, v, Configuration)
                else:
                    setattr(Configuration, k, v)

    @staticmethod
    def reset():
        '''Resets the class-level configuration state'''
        Configuration._FILE = None
        Configuration.__CONFIG_FILES = None
        # Clear dynamically created attributes
        for key in list(Configuration.__dict__.keys()):
            if not key.startswith('_'):  # Don't delete protected/private attributes
                delattr(Configuration, key)

Configuration()
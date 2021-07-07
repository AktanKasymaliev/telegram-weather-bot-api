from configparser import ConfigParser, NoOptionError, NoSectionError

TOKEN = "TOKEN"

def load_config(section, name, default=None):
    try:
        conf = ConfigParser()
        conf.read("settings.ini")
        return conf.get(section, name)

    except (NoOptionError, NoSectionError):
        return default

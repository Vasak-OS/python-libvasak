import configparser
import os

class VSKConfigManager:
  def __init__(self):
    self.configParser = configparser.ConfigParser()
    userDir = os.path.expanduser('~')
    self.configFilePath = f'{userDir}/.config/vasak/vasak.conf'
    self.configParser.read(self.configFilePath)

  def get(self, section, key):
    return self.configParser.get(section, key)
  
  def set(self, section, key, value):
    self.configParser.set(section, key, value)
    with open(self.configFilePath, 'w') as configfile:
      self.configParser.write(configfile)
    
  def remove(self, section, key):
    self.configParser.remove_option(section, key)
    with open(self.configFilePath, 'w') as configfile:
      self.configParser.write(configfile)

  def sections(self):
    return self.configParser.sections()
  
  def keys(self, section):
    return self.configParser.options(section)
  
  def items(self, section):
    return self.configParser.items(section)

  def reload(self):
    self.configParser.read(self.configFilePath)
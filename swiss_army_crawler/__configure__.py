import json
import os
from pathlib import Path
from swiss_army_crawler import LOGLEVELS

config_file_path = os.path.join(os.path.expanduser("~"), ".swiss_army_crawler_config.json")

def configure(is_default = True):
    config_file_exists = Path(config_file_path).is_file()
    if is_default and not config_file_exists: 
      settings = {
        "log_dir": os.path.join(os.path.expanduser("~"), "swiss_army_crawler/swiss_army_crawler_config.json"),
        "log_level": LOGLEVELS.DEBUG.name,
        "target_dir": os.path.join(os.path.expanduser("~"), "swiss_army_crawler_output"), 
      }

      # Save the settings to a config file
      with open(config_file_path, 'w') as config_file:
          json.dump(settings, config_file, indent=4)
      
      print(f"Configuration saved to {config_file_path}")
      print('\nconfigurations:\n{}'.format('\n'.join([f'{key} : {value}' for key, value in settings.items()])))

    elif not is_default:
      settings = {}
      while True:
        output_dir = input("Output folder (absolute path): ")
        if not output_dir or output_dir is None:
          print("Output folder path cannot be empty.")
        elif not Path(settings['target_dir']).is_dir:
          print("Output folder path is invalid, please try again.")
        else:
          settings['target_dir'] = output_dir
          break 

      while True:
        log_dir = input("Logs folder (absolute path): ")
        if not log_dir or log_dir is None:
          print("Logs folder path cannot be empty.")
        elif not Path(settings['target_dir']).is_dir:
          print("Logs folder path is invalid, please try again.")
        else:
          settings['log_dir'] = log_dir
          break 

      while True:
        log_level = input("Log level (DEBUG, CRITICAL, ERROR, WARNING or INFO): ")
        if not log_level or log_level is None:
           print('log level path cannot be empty.')
        elif log_level.upper() not in [level.name for level in LOGLEVELS]:
           print("Invalid log level, please try again.\npossible values are DEBUG, CRITICAL, ERROR, WARNING, INFO.")
        else:
          settings['log_level'] = log_level
          break 
          # Save the settings to a config file
      with open(config_file_path, 'w') as config_file:
          json.dump(settings, config_file, indent=4)
      
      print(f"Configuration saved to {config_file_path}")
      print('\nconfigurations:\n{}'.format('\n'.join([f'{key} : {value}' for key, value in settings.items()])))

  
if __name__ == "__main__":
  configure()
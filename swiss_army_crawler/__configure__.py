import json
import os
from pathlib import Path
from swiss_army_crawler import LOGLEVELS, Logger
from swiss_army_crawler.utils import parse_config_arguments

logger = Logger(LOGLEVELS.DEBUG, log_to_file=True)

# Path to config file
config_file_path = Path(os.path.join(os.path.expanduser("~"), ".swiss_army_crawler/config.json"))

def configure():
  
    # Create the directory if it doesn't exist
    config_file_path.parent.mkdir(parents=True, exist_ok=True)

    args = parse_config_arguments()
    log_folder, log_level,  output_folder = args._get_kwargs()

    settings = {
      log_folder[0]: log_folder[1], 
      log_level[0]: log_level[1],
      output_folder[0]: output_folder[1]
    }

    write_into_configs(settings)
    
    logger.info('Application configured')
    print(f"Configuration saved to {config_file_path}")

def check_configs_or_set_defaults() :
    """
    check_configs_or_set_defaults() 
    checks if config file exists or not, create config file and fill it with default values if not
    """
    if config_file_path.exists():
        return
    
    # create file path
    config_file_path.parent.mkdir(parents=True, exist_ok=True)

    # create configs with default values
    settings = {
        'log_folder': os.path.join(os.path.expanduser("~"), ".swiss_army_crawler/logs/"),
        'log_level': "DEBUG",
        'output_folder': os.path.join(os.path.expanduser("~"), ".swiss_army_crawler/output/")
    }

    # write configs into the configs file
    write_into_configs(settings)

def write_into_configs (settings: dict):
  """
  write_into_configs(settings)
  Writes settings into configs file
  """
  with open(config_file_path, 'w') as config_file:
      json.dump(settings, config_file, indent=4)

  
if __name__ == "__main__":
  configure()
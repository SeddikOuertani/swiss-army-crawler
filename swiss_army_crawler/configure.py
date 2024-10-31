import json
import os
from swiss_army_crawler import LOGLEVELS

config_file_path = os.path.join(os.path.expanduser("~"), ".swiss_army_crawler_config.json")

def configure():
    settings = {
       "log_path": os.path.join(os.path.expanduser("~"), "swiss_army_crawler/swiss_army_crawler_config.json"),
       "log_level": LOGLEVELS.DEBUG,
       "target_dir": os.path.join(os.path.expanduser("~"), "swiss_army_crawler_output"), 
    }
    
    isConfigure = False
    while not isConfigure:
      isConfigureInp = input("Configure swiss_army_crawler ? (Y/N) :").strip()
      if len(isConfigureInp) == 0 and isConfigureInp[0].capitalize() != 'Y' and isConfigureInp[0].capitalize() != 'N':
        print('Invalid input')
        continue
      
      isConfigure = isConfigureInp.startswith('y') or isConfigureInp.startswith('Y')
      break
    
    if isConfigure:
      
      settings['api_key'] = input("Enter your API key: ").strip()
      settings['save_path'] = input("Enter the default save path: ").strip()
      settings['log_level'] = input("Enter log level (e.g., DEBUG, INFO, WARNING): ").strip()

    # Save the settings to a config file
    with open(config_file_path, 'w') as config_file:
        json.dump(settings, config_file, indent=4)
    
    print(f"Configuration saved to {config_file_path}")
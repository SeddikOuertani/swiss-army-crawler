import argparse
import os

module_name = "logging_module"

def parse_main_arguments () -> argparse.Namespace:
  """
  parse_main_arguments () -> Namespace
  
  Returns a `Namespace` object containing arguments and their values

  Returns
    Namespace: 
  """

  parser = argparse.ArgumentParser(description="this tool helps you navigate metadata for files in a folder tree")
  
  # defines the path of the search
  parser.add_argument(
    "-p",
    "--path", 
    type=str,
    required=True,
    help="path of folder to inspect"
  )

  # defines if the scan is recursive or not
  parser.add_argument(
    "-r", 
    "--recursive",
    action="store_true",
    default=False,
    help="inspect folder recursively"
  )

  # defines depth of search tree
  parser.add_argument(
    "-d", 
    "--depth",
    type=int,
    default=-1,
    help="files or folders to exclude, requires --path",
    required=False
  )

  # defines folders to exclude from scan
  parser.add_argument(
    "-x", 
    "--exclude",
    nargs='+',
    default=[],
    help="files or folders to exclude, requires --path",
    required=False
  )

  args = parser.parse_args()  
  return args

def parse_config_arguments () -> argparse.Namespace:
  """
  parse_config_arguments () -> Namespace
  
  Returns a `Namespace` object containing config's arguments and their values

  Returns
    Namespace: 
  """

  parser = argparse.ArgumentParser(description="this tool helps you navigate metadata for files in a folder tree")

  # defines the logs folder
  parser.add_argument(
    "-lf",
    "--log_folder", 
    type=str,
    default=os.path.join(os.path.expanduser("~"), ".swiss_army_crawler/logs/"),
    help="path of logs folder"
  )

  # defines the log level
  parser.add_argument(
    "-ll",
    "--log_level", 
    type=str,
    default="DEBUG",
    help="log level"
  )

  # defines the log level
  parser.add_argument(
    "-of",
    "--output_folder", 
    type=str,
    default=os.path.join(os.path.expanduser("~"), ".swiss_army_crawler/output/"),
    help="log level"
  )

  args = parser.parse_args()  
  return args
  
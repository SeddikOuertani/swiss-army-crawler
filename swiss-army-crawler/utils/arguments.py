import argparse
from .. import Logger, LOGLEVELS

module_name = "logging_module"
logger = Logger(LOGLEVELS.DEBUG, log_to_file=True)

def parse_arguments () -> argparse.Namespace:
  """
  parse_arguments () -> Namespace
  
  Returns a `Namespace` object containing arguments and their values

  Returns
    Namespace: 
  """

  logger.info('Parsing arguments')

  parser = argparse.ArgumentParser(description="this tool helps you navigate metadata for files in a folder tree")
  
  # defins the path of the search
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

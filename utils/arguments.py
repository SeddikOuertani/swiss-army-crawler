import argparse
def parse_arguments () -> argparse.Namespace:
  """
  parse_arguments () -> Namespace
  
  Returns a `Namespace` object containing arguments and their values

  Returns
    Namespace: 
  """

  parser = argparse.ArgumentParser(description="this tool helps you navigate metadata for files in a folder tree")

  parser.add_argument(
    "-p",
    "--path", 
    type=str,
    required=True,
    help="path of folder to inspect"
  )

  parser.add_argument(
    "-r", 
    "--recursive",
    action="store_true",
    default=False,
    help="inspect folder recursively"
  )

  
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

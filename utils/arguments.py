import argparse
def parse_arguments ():
  parser = argparse.ArgumentParser(description="this tool helps you navigate metadata for files in a folder tree")

  parser.add_argument(
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

  args = parser.parse_args()  
  return args

import csv
from . import Logger, LOGLEVELS, parse_arguments, get_all_files_metadata, export_metadata
# Initialize the singleton logger
logger = Logger(level=LOGLEVELS.DEBUG, log_to_file=True)

# Example usage
logger.info("Application started.")

def main():
  args = parse_arguments ()
  files_metadata = get_all_files_metadata(args.path, args.recursive, args.depth, args.exclude)
  export_metadata(files_metadata)

if __name__ == "__main__":
  main()
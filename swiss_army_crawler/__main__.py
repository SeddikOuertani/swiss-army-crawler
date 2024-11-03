from swiss_army_crawler.utils import *

# Initialize the singleton logger
logger = Logger(level=LOGLEVELS.DEBUG, log_to_file=True)

# Example usage


def main():

  args = parse_arguments ()
  files_metadata = get_all_files_metadata(args.path, args.recursive, args.depth, args.exclude)
  export_metadata(files_metadata)
  
  logger.info('Scan finished.')
  
if __name__ == "__main__":
  main()
from swiss_army_crawler import Logger, LOGLEVELS, parse_main_arguments, get_all_files_metadata, export_metadata, check_configs_or_set_defaults
# Initialize the singleton logger
logger = Logger(level=LOGLEVELS.DEBUG, log_to_file=True)

def main():
  check_configs_or_set_defaults()
  args = parse_main_arguments()
  files_metadata = get_all_files_metadata(args.path, args.recursive, args.depth, args.exclude)
  export_metadata(files_metadata)
  
  logger.info('Scan finished.')
  
if __name__ == "__main__":
  main()
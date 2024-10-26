import csv
from utils.arguments import parse_arguments
from utils.scantools import get_all_files_metadata
from utils.loggintools import Logger, LOGLEVELS

# Initialize the singleton logger
logger = Logger(level=LOGLEVELS.DEBUG, log_to_file=True)

# Example usage
logger.info("Application started.")

def main():
  args = parse_arguments ()
  files_metadada = get_all_files_metadata(args.path, args.recursive, args.depth, args.exclude)
  field_names = list(set([key for file_metadata in files_metadada for key in file_metadata.keys()]))

  with open('./targets/output.csv',  mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()    
    writer.writerows(files_metadada)

if __name__ == "__main__":
  main()
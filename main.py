
from utils.arguments import parse_arguments
from utils.filetools import get_all_files_metadata, get_file_count_by_type
from utils.searchtools import get_folders_in_path
    

def main():

  args = parse_arguments ()
  files_metadada = get_all_files_metadata(args.path, True, 4, ['venv'])
  # files_count_by_types = get_file_count_by_type(args.path, args.recursive)

  # print ("Files metadata ({}):\r\n\t".format(files_metadada))
  # print ("Files count by types ({}):\r\n\t".format(files_count_by_types))
  folders = get_folders_in_path(args.path, True, 4)
  print(files_metadada)

if __name__ == "__main__":
  main()
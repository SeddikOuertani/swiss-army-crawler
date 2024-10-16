
from utils.arguments import parse_arguments
from utils.searchtools import get_folders_in_path, get_files_in_path
from utils.filetools import get_all_files_metadata, get_file_count_by_type 
    

def main():

  args = parse_arguments ()
  files_metadada = get_all_files_metadata(args.path, args.recursive)

  print ("Files metadata ({}):\r\n\t".format(files_metadada))

if __name__ == "__main__":
  main()
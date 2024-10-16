
from utils.arguments import parse_arguments
from utils.filestools import get_folder_paths_in_path, get_file_count_by_type, get_file_paths_in_paths
    
args = parse_arguments ()
folder_paths = get_folder_paths_in_path(args.path, args.recursive)
file_paths = get_file_paths_in_paths(args.path, args.recursive)
file_counts_by_type = get_file_count_by_type(file_paths)

# print("arguments:\r\n\tpath: {}\r\n\trecursive: {}\n".format(args.path, args.recursive))
# print ("Folders to scan ({}):\r\n\t{}\n".format(len(folder_paths),'\r\n\t'.join(folder_paths)))
# print ("Files to scan ({}):\r\n\t{}\n".format(len(file_paths),'\r\n\t'.join(file_paths)))
# print ("file_counts_by_type :\r\n\t{}".format(file_counts_by_type))
print ("Folders to scan ({}):\r\n\t".format(len(folder_paths)))
print ("Files to scan ({}):\r\n\t".format(len(file_paths)))
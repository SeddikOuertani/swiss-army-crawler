from pathlib import Path
from .misctools import check_starting_parameters_validity 
from .loggingtools import Logger, LOGLEVELS

module_name = 'probing_module'
logger = Logger(LOGLEVELS.DEBUG, log_to_file=True)

def get_folders_in_path (dir_path: str, is_recursive: bool = False, depth: int= -1, excluded_directories: list[str] = []) -> list[str] :
  """
  get_folders_in_path(dir_path, is_recursive) -> str

  returns all folder paths inside provided folder's path

  ### Args:
    path (str): the path of the folder to start the scan from.
    is_recursive (bool): choose if the scan should be recursive or should stop at the surface level folder path.
    depth (int): specifies the scan path's depth
    excluded_directories(list[str]): contains list of folder names to exclude

  ### Returns:
    list of str: A list containing the paths of all the folders found 
  """
  logger.info('Scanning all folder paths ...')

  check_starting_parameters_validity(dir_path, depth)
  
  p = Path(dir_path).resolve()
  folder_paths = [p.as_posix()]

  if is_recursive == False: 
    return [folder.as_posix() for folder in p.iterdir() if folder.is_dir()]

  for file_path in [fp for fp in p.rglob('*') if fp.is_dir()]:

    # Skip paths that exceed the specified depth, unless no depth is specified
    current_depth = len(file_path.relative_to(p.as_posix()).parts) - 1
    if depth != -1 and current_depth > depth:
      continue

    # skips paths that are in the exclusion list
    if len(excluded_directories) > 0 and any(excluded_dir in file_path.parts for excluded_dir in excluded_directories):
      continue

    # adds folder to list
    folder_paths.append(file_path.as_posix())
      
  return folder_paths

def get_files_paths_in_directory (dir_path: str) -> list[str]:
  """
  get_files_paths_in_directory(dir_path) -> list[str]

  Returns all file paths for provided path 

  Args:
    dir_path (str): the path of the folder to scan from.

  Returns:
    list[str]: A list containing the paths of all the files found 
  """

  if (dir_path.startswith("/") == False):
    dir_path = Path(dir_path).resolve()
  p = Path(dir_path)
  return [file.as_posix() for file in p.iterdir() if file.is_file()]

def get_files_in_path (dir_path: str, is_recursive: bool = False, depth: int = - 1, excluded_directories: list[str] = []) -> list[str]:
  """
  get_files_in_path (dir_path, is_recursive) -> list

  Returns all file paths for the provided path 

  Args:
    dir_path (str): the path of the folder to start the scan from.
    is_recursive (bool): decides or not if the scan should be recursive.
    depth (int): specifies the scan path's depth
    excluded_directories(list[str]): contains list of folder names to exclude
  Returns:
    list[str]: A list containing the paths of all the files found 
  """
  logger.info('Getting all file paths to scan ...')
  check_starting_parameters_validity(dir_path, depth, excluded_directories)

  folder_paths = get_folders_in_path(dir_path, is_recursive, depth, excluded_directories)
  file_paths = []
  for folder_path in folder_paths:
    file_paths.extend(get_files_paths_in_directory(folder_path))
  return file_paths



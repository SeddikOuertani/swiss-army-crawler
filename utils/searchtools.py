from pathlib import Path
import magic

def get_folders_in_path (dir_path: str, is_recursive: bool) -> list :
  """
  get_folders_in_path(dir_path, is_recursive) -> str

  returns all folder paths inside provided folder's path

  Args:
    path (str): the path of the folder to start the scan from.
    is_recursive (bool): choose if the scan should be recursive or should stop at the surface level folder path.

  Returns:
    list of str: A list containing the paths of all the folders found 
  """

  p = Path(dir_path).resolve()
  file_list = p.rglob('*') if is_recursive else p.iterdir()
  return [file.as_posix() for file in file_list if file.is_dir()]

def get_files_paths_in_directory (dir_path: str) -> list[str]:
  """
  get_files_paths_in_directory(dir_path) -> list[str]

  Returns all file paths for provided path 

  Args:
    dir_path (str): the path of the folder to scan from.

  Returns:
    list of str: A list containing the paths of all the files found 
  """

  if (dir_path.startswith("/") == False):
    dir_path = Path(dir_path).resolve()
  p = Path(dir_path)
  return [file.as_posix() for file in p.iterdir() if file.is_file()]

def get_files_in_path (dir_path: str, is_recursive: bool) -> list:
  """
  get_files_in_path (dir_path, is_recursive) -> list

  Returns all file paths for the provided path 

  Args:
    dir_path (str): the path of the folder to start the scan from.
    is_recursive (bool): decides or not if the scan should be recursive.
  Returns:
    list of str: A list containing the paths of all the files found 
  """

  folder_paths = [dir_path]
  folder_paths.extend(get_folders_in_path(dir_path, is_recursive))
  file_paths = []
  for folder_path in folder_paths:
    file_paths.extend(get_files_paths_in_directory(folder_path))
  return file_paths

def get_file_format (file_path: str) -> str:
  """
  get_file_format (file_path) -> str

  Returns the format of file in `file_path`

  Args:
    file_path (str): the path of the file to scan.

  Returns:
    str: the MIME type of the file
  """

  return magic.from_file(file_path).split(',')[0]
  


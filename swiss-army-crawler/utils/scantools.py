import pwd
import grp
import os
import magic
from pathlib import Path 
from .. import get_text_file_metadata,  get_file_format, get_files_in_path, check_starting_parameters_validity,  get_image_file_metadata,  get_video_file_metadata

module_name  = 'scantools'

def get_file_count_by_type (dir_path: str, is_recursive: bool = False, depth: int = -1, excluded_directories: list[str] = []) -> str:
  """
  get_file_count_by_type (str, bool) -> str
  
  Returns the number of files for each type of file found in the provided directory

  ### Args:
    dir_path (str): the path of the folder to scan.
    is_recursive (bool): specifies weather or not the scan should be recursive
    depth (int): specifies the scan path's depth
    excluded_directories(list[str]): contains list of folder names to exclude

  ### Returns:
    str: the MIME type of the file
  """

  check_starting_parameters_validity(dir_path, depth, excluded_directories)

  file_paths = get_files_in_path(dir_path, is_recursive, depth, excluded_directories)
  types = {}
  for file in file_paths:
    format = get_file_format(file)
    if format not in types:
      types[format] = 1
    else:
      types[format] += 1
  return types

def get_file_metadata (file_path: Path) -> dict:
  """
  get_file_metadata(file_path) -> dict

  Returns metadata for file passed in parameters

  ### Args:
    file_path (Path): the path of the file to scan (type *Path* from **pathlib**)

  ### Returns:
    dict: contains file info (name, size, last update date, creation date, etc...) 
  """

  metadata = {}
  
  file_general_info = get_file_general_info(file_path)
  metadata = {**metadata, **file_general_info}
  
  if metadata['type'].startswith('ASCII') or metadata['type'].__contains__('text'):
    file_stats = get_text_file_metadata(file_path)
    metadata = {**metadata, **file_stats}

  # If the file is an image
  if metadata['type'].startswith('image'):
    image_info = get_image_file_metadata(file_path)
    metadata = {**metadata, **image_info}
  
  # If the file is an video
  if metadata['type'].startswith('video'):
    video_info = get_video_file_metadata(file_path)
    metadata = {**metadata, **video_info}

  return metadata

def get_all_files_metadata(dir_path: str, is_recursive: bool = False, depth: int = -1, excluded_directories: list[str] = []) -> list[dict]:
  """
  get_all_files_metadata(dir_path, is_recursive) -> list[dict]

  Returns metadata for files in folder path in `dir_path`

  ### ### Args:
    path (Path): the path of the file to scan (type *Path* from **pathlib**)
    is_recursive (bool): specifies if scan is recursive or not
    depth (int): specifies the scan path's depth
    excluded_directories(list[str]): contains list of folder names to exclude
  ### Returns:
    dict: contains file info (name, size, last update date, creation date, etc...) 
  """
  
  all_files = get_files_in_path(dir_path, is_recursive, depth, excluded_directories)
  all_metadata = []

  for file_path in all_files:
    file = Path(file_path)
    file_metadata = get_file_metadata(file)
    all_metadata.append(file_metadata)

  return all_metadata

def get_file_general_info(file_path: Path) -> dict:
  """
  get_file_general_info(Path) -> dict
  
  Returns file's general metadata
  
  ### Args:
    file_path (Path): file's path
  ### Returns: 
    dict: a dictionary containing file's metadata name value pairss
  """

  metadata = {}
  metadata['full_path'] = file_path.as_posix()  # absolute path to file
  metadata['name'] = file_path.name  # file name
  metadata['size'] = file_path.stat().st_size  # File size in bytes
  metadata['last_modified'] = os.path.getmtime(file_path.as_posix())  # Last modified time
  metadata['creation_time'] = os.path.getctime(file_path.as_posix())  # Creation time
  mime = magic.Magic(mime=True)
  metadata['type'] = mime.from_file(str(file_path))  # File type  
  
  # Get file status
  file_stat = os.stat(file_path.as_posix())
  metadata["owner_id"] = file_stat.st_uid  # User ID of the owner
  metadata["group_id"] = file_stat.st_gid  # Group ID of the owner
  metadata["owner_name"] = pwd.getpwuid(file_stat.st_uid).pw_name  # Owner's username
  metadata["group_name"] = grp.getgrgid(file_stat.st_gid).gr_name  # Group name
  metadata["permissions"] = oct(file_stat.st_mode)[-3:]  # Permissions in octal format (e.g., '644')
  return metadata
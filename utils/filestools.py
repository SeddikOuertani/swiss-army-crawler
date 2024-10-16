import os
from pathlib import Path
import magic
from PIL import Image
import exifread

def get_folder_paths_in_path (dir_path, is_recursive) :
  """
  get all folder paths inside provided folder's path

  Args:
      path (str): the path of the folder to start the scan from.
      is_recursive (bool): choose if the scan should be recursive or should stop at the surface level folder path.

  Returns:
      list of str: A list containing the paths of all the folders found 
  """
  path = dir_path
  if (dir_path.startswith("/") == False):
    path = Path(dir_path).resolve()
  p = Path(path)
  file_list = p.rglob('*') if is_recursive else p.iterdir()
  return [file.as_posix() for file in file_list if file.is_dir()]

def get_files_paths (path):
  """
  get all file paths from provided path 

  Args:
      path (str): the path of the folder to scan from.

  Returns:
      list of str: A list containing the paths of all the files found 
  """
  if (path.startswith("/") == False):
    path = Path(path).resolve()
  p = Path(path)
  return [file.as_posix() for file in p.iterdir() if file.is_dir() == False]

def get_file_paths_in_paths (dir_path, is_recursive):
  """
  get all file paths in the provided path  

  Args:
      path (str): the path of the folder to scan from.

  Returns:
      list of str: A list containing the paths of all the files found 
  """
  folder_paths = [dir_path]
  folder_paths.extend(get_folder_paths_in_path(dir_path, is_recursive))
  file_paths = []
  for folder_path in folder_paths:
    file_paths.extend(get_files_paths(folder_path))
  return file_paths

def get_file_format (path):
  """
  get provided file path name's format

  Args:
      path (str): the path of the file to scan.

  Returns:
      str: the MIME type of the file
  """
  return magic.from_file(path).split(',')[0]

def get_file_count_by_type (paths):
  """
  get 

  Args:
      path (str): the path of the file to scan.

  Returns:
      str: the MIME type of the file
  """
  types = {}
  for file in paths:
    format = get_file_format(file)
    if format not in types:
      types[format] = dict()
      types[format]["count"] = 1
      types[format]["files"] = [file]
    else:
      types[format]["count"] += 1
      types[format]["files"].append(file)
  return types

def get_file_metadata (file_path):

  
  metadata = {}

  # Get basic file info
  metadata['name'] = file_path.name
  metadata['size'] = file_path.stat().st_size  # File size in bytes
  metadata['last_modified'] = file_path.stat().st_mtime  # Last modified time
  metadata['creation_time'] = file_path.stat().st_ctime  # Creation time
  metadata['type'] = magic.from_file(str(file_path))  # File type

  # If the file is an image, extract additional metadata
  if metadata['type'].startswith('image'):
      try:
          with Image.open(file_path) as img:
              metadata['format'] = img.format
              metadata['mode'] = img.mode
              metadata['dimensions'] = img.size  # Image dimensions (width, height)
              metadata['info'] = img.info  # Additional image info
      except Exception as e:
          metadata['image_error'] = str(e)

      # Extract EXIF data
      try:
          with open(file_path, 'rb') as f:
              tags = exifread.process_file(f)
              metadata['exif'] = {tag: str(tags[tag]) for tag in tags.keys() if tag.startswith('EXIF')}
      except Exception as e:
          metadata['exif_error'] = str(e)

  return metadata

def get_all_files_metadata(dir_path):
  dir_path = Path(dir_path)
  all_metadata = []

  for file_path in dir_path.rglob('*'):  # Recursively get all files
      if file_path.is_file():
          file_metadata = get_file_metadata(file_path)
          all_metadata.append(file_metadata)

  return all_metadata
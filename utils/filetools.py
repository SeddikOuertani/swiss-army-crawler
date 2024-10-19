import os
import magic
from pathlib import Path 
from PIL import Image
import exifread

from .searchtools import get_file_format, get_files_in_path 

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
    path (Path): the path of the file to scan (type *Path* from **pathlib**)

  ### Returns:
    dict: contains file info (name, size, last update date, creation date, etc...) 
  """

  metadata = {}
  
  file_general_info = get_file_general_info(file_path)
  for key in file_general_info.keys():
    metadata[key] = file_general_info[key]
  
  if metadata['type'].__contains__('ASCII') or metadata['type'].__contains__('text'):
    file_stats = get_text_file_content_stats(file_path)
    for key in file_stats.keys():
      metadata[key] = file_stats[key]


  # If the file is an image, extract additional metadata
  if metadata['type'].__contains__('image'):
    image_info = get_image_file_content_info(file_path)
    for key in image_info.keys():
      metadata[key] = image_info[key]

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
  info = {}
  info['name'] = file_path.name
  info['size'] = file_path.stat().st_size  # File size in bytes
  info['last_modified'] = os.path.getmtime(file_path.as_posix())  # Last modified time
  info['creation_time'] = os.path.getctime(file_path.as_posix())  # Creation time
  info['type'] = magic.from_file(str(file_path))  # File type
  return info
  
def get_text_file_content_stats(file_path: Path) -> dict:
  """
  get_text_file_content_stats(Path) -> dict
  
  Returns text file's metadata
  
  ### Args:
    file_path (Path): text file's path
  ### Returns: 
    dict: a dictionary containing text file's metadata name value pairss
  """
  try:
    with open(file_path.as_posix()) as file:
      text = file.read()
      stats = {}
      stats["line_count"] = len(text.splitlines())
      stats["word_count"] = len(text.split())
      stats["char_count"] = len(text)
  except Exception as e:
    stats['text_file_error'] = str(e)
  return stats
  
def get_image_file_content_info(file_path: Path) -> dict:
  """
  get_image_file_content_info(Path) -> dict
  
  Returns image file's metadata
  
  ### Args:
    file_path (Path): text file's path
  ### Returns: 
    dict: a dictionary containing image file's metadata name value pairss
  """
  try:
    info = {}
    with Image.open(file_path.as_posix()) as img:
      info['format'] = img.format
      info['mode'] = img.mode
      info['dimensions'] = img.size  # Image dimensions (width, height)
      info['info'] = img.info  # Additional image info
  except Exception as e:
    info['image_error'] = str(e)

  try:
    with open(file_path, 'rb') as f:
      tags = exifread.process_file(f)
      info['exif'] = {tag: str(tags[tag]) for tag in tags.keys() if tag.startswith('EXIF')}
  except Exception as e:
    info['exif_error'] = str(e)

  return info

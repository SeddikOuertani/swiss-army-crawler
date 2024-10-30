from PIL import Image
import exifread
from pathlib import Path

def get_image_file_metadata(file_path: Path) -> dict:
  """
  get_image_file_metadata(Path) -> dict
  
  Returns image file's metadata
  
  ### Args:
    file_path (Path): image file's path
  ### Returns: 
    dict: a dictionary containing image file's metadata name value pairss
  """
  metadata = {}
  try:
    with Image.open(file_path.as_posix()) as img:
      metadata['format'] = img.format
      metadata['mode'] = img.mode
      metadata['dimensions'] = img.size  # Image dimensions (width, height)
      metadata['info'] = img.info  # Additional image info
  except Exception as e:
    metadata['image_error'] = str(e)

  try:
    with open(file_path, 'rb') as f:
      tags = exifread.process_file(f)
      metadata['exif'] = {tag: str(tags[tag]) for tag in tags.keys() if tag.startswith('EXIF')}
  except Exception as e:
    metadata['exif_error'] = str(e)

  return metadata

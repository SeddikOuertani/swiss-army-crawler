import csv
from .loggingtools import Logger, LOGLEVELS

module_name = "output_module"
logger = Logger(LOGLEVELS.DEBUG, log_to_file=True)

def export_metadata (files_metadata: list[dict]) -> None:

  
  field_names = list(set([key for file_metadata in files_metadata for key in file_metadata.keys()]))
  text_files_metadata = [file for file in files_metadata if file['type'].startswith('text')]
  image_files_metadata = [file for file in files_metadata if file['type'].startswith('image')]
  video_files_metadata = [file for file in files_metadata if file['type'].startswith('video')]
  text_field_names = list(set([key for file_metadata in text_files_metadata for key in file_metadata.keys()]))
  image_field_names = list(set([key for file_metadata in image_files_metadata for key in file_metadata.keys()]))
  video_field_names = list(set([key for file_metadata in video_files_metadata for key in file_metadata.keys()]))
  try:
    with open('./targets/text_md.csv',  mode='w', newline='') as file:
      writer = csv.DictWriter(file, fieldnames=text_field_names)
      writer.writeheader()    
      writer.writerows(text_files_metadata)
    with open('./targets/image_md.csv',  mode='w', newline='') as file:
      writer = csv.DictWriter(file, fieldnames=image_field_names)
      writer.writeheader()    
      writer.writerows(image_files_metadata)
    with open('./targets/video_md.csv',  mode='w', newline='') as file:
      writer = csv.DictWriter(file, fieldnames=video_field_names)
      writer.writeheader()    
      writer.writerows(video_files_metadata)
    with open('./targets/all_files_md.csv',  mode='w', newline='') as file:
      writer = csv.DictWriter(file, fieldnames=field_names)
      writer.writeheader()    
      writer.writerows(files_metadata)
  
  except Exception as e:
    logger.error("Error while writing to file")
from pathlib import Path
import ffmpeg
from .. import Logger, get_current_function_info

logger = Logger()


def get_video_file_metadata(file_path: Path) -> dict:
  """
  get_video_file_metadata(Path) -> dict
  
  Returns video file's metadata
  
  ### Args:
    file_path (Path): video file's path
  ### Returns: 
    dict: a dictionary containing video file's metadata name value pairss
  """
  metadata = {}
  try:
    probe = ffmpeg.probe(filename=file_path.as_posix(), cmd="azeaze")
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    metadata = {
        'width': video_stream['width'],
        'height': video_stream['height'],
        'duration': float(probe['format']['duration']), 
        'bit_rate': int(probe['format']['bit_rate']), # indicates video quality
        'frame_rate': eval(video_stream['r_frame_rate'])  # might return a string like "30/1"
    }
    return metadata
  except BaseException as e:
    module_name, function_name = get_current_function_info()
    logger.error(e, module_name=module_name, function_name=function_name, err_file=file_path.as_posix())
    return {}
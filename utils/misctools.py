import threading
from pathlib import Path
import inspect

def get_current_function_info():
  # Get the current frame and the caller's frame
  frame = inspect.currentframe().f_back
  
  # Get the file name of the caller
  file_name = frame.f_code.co_filename
  
  # Get the function name of the caller
  function_name = frame.f_code.co_name
  
  return file_name, function_name


def check_starting_parameters_validity (dir_path: str, depth: int= -1, excluded_directories: list[str] = []) -> bool:
  if depth < -1:
    raise Exception("Please make sure depth is 0 or higher")

  p = Path(dir_path).resolve()
  if p.is_dir() == False:
    raise Exception("Please make sure that you provide a valid directory path")

  if isinstance(excluded_directories, list) == False: 
    raise Exception("Please make sure that the excluded directories is a list of strings")
  
class SingletonMeta(type):
  _instances = {}
  _lock = threading.Lock()  # Ensures thread-safety

  def __call__(cls, *args, **kwargs):
    with cls._lock:
      if cls not in cls._instances:
        instance = super().__call__(*args, **kwargs)
        cls._instances[cls] = instance
    return cls._instances[cls]

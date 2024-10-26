from dotenv import load_dotenv
import os
import enum
import datetime
from .misctools import SingletonMeta

load_dotenv()

log_file = os.getenv('LOG_DIR')

# loggin
class LOGLEVELS(enum.Enum):
    DEBUG = 1
    CRITICAL = 2
    ERROR = 3
    WARNING = 4
    INFO = 5
class Logger(metaclass=SingletonMeta):

  def __init__(self, level : LOGLEVELS = LOGLEVELS.ERROR, log_to_file: bool = True, file_path: str = log_file):
    self.level = level
    self.log_to_file = log_to_file
    self.file_path = file_path
  
  def log(self, error_message: str, level: LOGLEVELS, module_name: str = None, function_name: str = None, err_file: str = None):
    if level.value >= self.level.value:  # Only log if level is sufficient
        formatted_message = self._format_message(error_message, level, module_name, function_name, err_file)
        self._output(formatted_message)

  def _format_message(self, message: str, level: LOGLEVELS,  module_name: str = None, function_name: str = None, err_file: str = None) -> str:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return  f"[{timestamp}] [{level.name}] {message}{' at module {}.'.format(module_name) if module_name else ''}{ 'at function {}.'.format(function_name) if function_name else ''}{' while scanning {}.'.format(err_file) if err_file else ''}"

  def _output(self, formatted_message: str):
    if self.log_to_file:
      with open(self.file_path, "a") as log_file:
        log_file.write(formatted_message + "\n")
    else:
      print(formatted_message)

    # Helper methods for specific log levels
  def debug(self, message: str, module_name: str = None, function_name: str = None, err_file: str = None):
    self.log(message, LOGLEVELS.DEBUG, module_name, function_name, err_file)

  def info(self, message: str, module_name: str = None, function_name: str = None, err_file: str = None):
    self.log(message, LOGLEVELS.INFO, module_name, function_name, err_file)

  def warning(self, message: str, module_name: str = None, function_name: str = None, err_file: str = None):
    self.log(message, LOGLEVELS.WARNING, module_name, function_name, err_file)

  def error(self, message: str, module_name: str = None, function_name: str = None, err_file: str = None):
    self.log(message, LOGLEVELS.ERROR, module_name, function_name, err_file)

  def critical(self, message: str, module_name: str = None, function_name: str = None, err_file: str = None):
    self.log(message, LOGLEVELS.CRITICAL, module_name, function_name, err_file)
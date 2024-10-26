from pathlib import Path
from langdetect import detect
from collections import Counter
import re

module_name = 'texttools'

def detect_languages (file_path: Path) -> list[str]:
  """
  detect_language(file_path) -> list[ste]
  
  Returns list of languages used in a text file
  ### Args:
    file_path (Path): contains file path in the pathlib.Path format
  ### Returns:
    list[str]: List of abreviated language names
  """
  with open(file_path.as_posix()) as file:
    try:
      text = file.read()
      lines = text.splitlines()
      return list(set([detect(line) for line in lines]))
    except Exception as e:
      return []
    
def get_word_frequency (file_path: Path, frequency_type: int = 1, word_count: int = -1) -> dict:
  """
  get_word_frequency(file_path, frequency_type, word_count) -> list[str]
  
  Returns a dictionary of words and their respective frequency from a file
  ### Args:
    file_path (Path): contains file path in the pathlib.Path format
    frequency_type(int): either search for most frequent or least frequent values can be `1` or `0` respectively
    word_count(int): number of words to get depending their frequency

  ### Returns:
    dict: contains files unique words and their frequency
  """
  with open(file_path.as_posix()) as file:
    
    if frequency_type not in [1, 0]:
      raise Exception("Invalid frequency_type value, can only be 1 or 0, for most frequent and least frequent respectively")
    
    if word_count < -1 or word_count == 0:
      raise Exception("Invalid word count can only inter positive values, 1+")
    
    try:
      text = file.read()
      # Filter words and count occurrences using Counter
      word_counts = Counter(word for word in text.split() if len(word) > 2)

      # Sort the word counts based on frequency
      sorted_word_count_pairs = sorted(word_counts.items(), key=lambda item: item[1], reverse=(frequency_type == 1))

      # Return sorted pairs based on word_count
      return sorted_word_count_pairs if word_count == -1 else sorted_word_count_pairs[:word_count + 1]

    except Exception as e:
      return []
    
def get_line_distribution (file_path: Path) -> dict:
  """
  get_line_dtribution(file_path) -> dict

  Returns max, min and average length the lines in a file

  ### Args: 
    file_path (Path): file's path
  ### Returns: 
    dict: a dictionnary containing the file's line distribution info
  """
  try:
    with open(file_path.as_posix()) as file:
      text = file.read()

      lines = text.splitlines()

      max_line_length = max(len(line) for line in lines) if lines else 0
      min_line_length = min(len(line) for line in lines) if lines else 0
      avg_line_length = int(sum(len(line) for line in lines) / len(lines)) if lines else 0

      line_distribution = {
          "max_line_length": max_line_length,
          "min_line_length": min_line_length,
          "avg_line_length": avg_line_length
      }

      return line_distribution
  except Exception as e:
    return {}
  
def get_word_distribution (file_path: Path) -> dict:
  """
  get_word_distribution(file_path) -> dict

  Returns max, min and average length the words in a file

  ### Args: 
    file_path (Path): file's path
  ### Returns: 
    dict: a dictionnary containing the file's words distribution info
  """
  try:
    with open(file_path.as_posix()) as file:
      text = file.read()

      lines = text.splitlines()
      words = [word for line in lines for word in line.split()]

      max_word_length = max(len(word) for word in words) if words else 0
      min_word_length = min(len(word) for word in words) if words else 0
      avg_word_length = sum(len(word) for word in words) / len(words) if words else 0

      word_distribution = {
          "max_word_length": max_word_length,
          "min_word_length": min_word_length,
          "avg_word_length": avg_word_length
      }

      return word_distribution
  except Exception as e:
    return {}

def detect_hyperlinks (file_path: Path) -> list[str]:
  """
  detect_hyperlinks(file_path) -> list[str]

  Return a list of all hyper links found in the file

  ### Args:
    file_path (Path): file's path
  ### Returns: 
    list[str]: list of hyperlinks 
  """
  with open(file_path.as_posix()) as file:
    try:
      text = file.read()
      
      url_pattern = r'https?://[^\s]+|www\.[^\s]+'
      hyperlinks = re.findall(url_pattern, text)
      return hyperlinks
    except Exception as e:
      return []
    
def get_text_file_metadata(file_path: Path) -> dict:
  """
  get_text_file_metadata(Path) -> dict
  
  Returns text file's metadata
  
  ### Args:
    file_path (Path): text file's path
  ### Returns: 
    dict: a dictionary containing text file's metadata name value pairss
  """
  metadata = {}
  try:
    with open(file_path.as_posix()) as file:
      text = file.read()
      metadata["languages"] = detect_languages(file_path)
      metadata["line_count"] = len(text.splitlines())
      metadata["word_count"] = len(text.split())
      metadata["char_count"] = len(text)
      metadata["word_frequency"] = get_word_frequency(file_path, word_count=3)
      metadata["whitespace_count"] = text.count(' ')
      line_distribution_data = get_line_distribution(file_path)
      word_distribution_data = get_word_distribution(file_path)
      metadata = {
        **metadata, 
        **line_distribution_data, 
        **word_distribution_data
      }
      
  except Exception as e:
    metadata['text_file_error'] = str(e)
  return metadata
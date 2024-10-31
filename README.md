Project Title: swiss_army_crawler

### Description: 
This project, swiss_army_crawler, is designed to extract metadata from various file types, including video, text, and image files. The goal is to provide users with a comprehensive tool that simplifies the retrieval and management of essential information contained within these files.

### Key Features:
 - Metadata Extraction: Automatically extracts metadata from supported file types (videos, text documents, images).
 - Supported Formats: Handles a wide range of file formats, ensuring versatility in metadata extraction.
 - User-Friendly CLI: Offers a straightforward command-line interface for ease of use.
### Installation Instructions:
To install swiss_army_crawler, you can use pip:
```
pip install swiss_army_crawler
```
### Usage Instructions:
Here’s a basic example of how to use the tool:
```
swiss --path /path/to/files --recursive --depth 3 --exclude folder1 folder2
```

### Requirements:
Python 3.x

### Required libraries: 
 - pathlib==1.0.1
 - argparse==1.4.0
 - python-magic==0.4.27
 - Pillow==11.0.0
 - ExifRead==3.0.0
 - langdetect==1.0.9
 - python-dotenv==1.0.1
 - ffmpeg-python==0.2.0

### License:
This project is licensed under the MIT License.


from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import sys 

class InstallConfigs(install):
    """Custom installation to run configuration script after install."""
    
    def run(self):
        install.run(self)
        
        print("Running configuration script...")
        subprocess.check_call([sys.executable,'-m', 'swiss_army_crawler.configure', 'configure'])
    

setup(
    name='swiss-army-crawler',  # Replace with your package name
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
      "pathlib==1.0.1",
      "argparse==1.4.0",
      "python-magic==0.4.27",
      "pillow==11.0.0",
      "exifread==3.0.0",
      "langdetect==1.0.9",
      "python-dotenv==1.0.1",
      "ffmpeg-python==0.2.0"
      ],
    cmdclass={
      "install": InstallConfigs  
    },
    entry_points={
      'console_scripts': [
        'swiss=swiss_army_crawler.__main__:main',
      ],
    },
    author='Mohamed Seddik OUERTANI',
    author_email='mohamedseddikouertani@gmail.com',
    description='A swiss army knife crawling machine',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SeddikOuertani/swiss-army-crawler', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Linux',
    ],
    python_requires='>=3.10.12',
)

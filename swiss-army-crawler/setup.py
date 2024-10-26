from setuptools import setup, find_packages

setup(
    name='swiss-army-crawler',  # Replace with your package name
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, e.g., 'requests', 'numpy'
    ],
    entry_points={
        'console_scripts': [
            'your_command=your_package_name.main:main',  # Adjust if you have a main function
        ],
    },
    author='Mohamed Seddik OUERTANI',
    author_email='mohamedseddikouertani@gmail.com',
    description='A swiss army knife crawling machine',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SeddikOuertani/swiss-army-crawler',  # Repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Linux',
    ],
    python_requires='>=3.10.12',  # Specify required Python version
)

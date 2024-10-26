## 1. define dependencies and their versions
### a. requirements.txt
  - pathlib==1.0.1
  - argparse==1.4.0
  - python-magic==0.4.27
  - Pillow==11.0.0
  - ExifRead==3.0.0
  - langdetect==1.0.9
  - python-dotenv==1.0.1
  - ffmpeg-python==0.2.0

## 2. using **pip** with virtual environments
- install python3-venv
```
apt install python3.10-venv
```
- execute the following command to create a virtual environment
```
python3 -m venv venv
```

### a. activate virtual environment
- execute the following command to activate the virtual environment

- **Linux** : ```source venv/bin/activate```

- **windows** : ```venv\Scripts\activate```

## 4. install dependencies
- execute command
```
pip install -r requirements.txt
```

## 5. install pipenv for dependency management
### a. install pipenv
- execute command
```
pip install pipenv
```
### b. install dependencies by pipenv
- example:
```
pipenv install numpy pandas requests
```
### c. export dependencies to requirements.txt
- execute command
```
pipenv lock -r > requirements.txt
```

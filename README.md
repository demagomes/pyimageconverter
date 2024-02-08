# Python Image Converter (pyimageconverter)
A simple Python concole application for image conversion

In this version it can convert images between PNG,JPEG and WEBP formats.

## Default Values
```
-d '.'
-s JPEG
-t WEBP
```
## Basic Use / Examples

### Help
```
python3 main.py -h

usage: main.py [-h] [-d DIRECTORY] [-f FILE] [-s {JPEG,PNG,WEBP}] [-t {JPEG,PNG,WEBP}]

options:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        Converts files in the folder defined, its the default option with local folder ".": -d <Folder Path>
  -f FILE, --file FILE  Converts the file defined: -f <File Path and Name>
  -s {JPEG,PNG,WEBP}, --source {JPEG,PNG,WEBP}
                        Source File Type: -s JPEG
  -t {JPEG,PNG,WEBP}, --target {JPEG,PNG,WEBP}
                        Target File Type: -s WEBP
```

### Default (without any parameter)
This will convert any JPEG images to WEBP image in the current folder.
```
python3 main.py

Python Image Converter
https://github.com/demagomes/pyimageconverter
Progress: |██████████████████████████████████████████████████| 100.0% Complete
Errors:
```

### Convert all PNG files in a folder to JPEG 
```
python3 main.py -s JPEG -t PNG
```

### Convert oen specif JPEG file to PNG
```
python3 main.py -f IMG_1802.jpeg -t PNG
```

## External Libraries
- Pillow
- pytest


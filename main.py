#NOTE - Main script to execute the basic file converter
import argparse
import os
from classes.utils import Utils
from classes.converter import Converter


# TODO - define list of extensions based on argument passed
# TODO - pass the list to listdirectory
# TODO - make most of the script into functions
# TODO - use the __main__ piece to avoid it being executed when testing
# TODO - write unit tests to functions here
# TODO - work on when no file is found, it is erroring at the moment.

#NOTE - Defines the command line arguments for the script
def setarguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--directory", help="Converts files in the filder defined: -d <Folder Path>")
    parser.add_argument("-f","--file", help="Converts the file defined: -f <File Path and Name>")
    parser.add_argument("-s","--source", help="Source File Type: -s JPEG", choices=['JPEG','PNG','WEBP'],default='JPEG')
    parser.add_argument("-t","--target", help="Target File Type: -s WEBP", choices=['JPEG','PNG','WEBP'],default='WEBP')
    return parser.parse_args()


args = setarguments()

errors = []
u = Utils()
c = Converter()
files = u.listdirectory(['.jpeg','.jpg'])
l = len(files)

# Initial call to print 0% progress
u.printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

for i,image in enumerate(files):
    name = image.split('.')[0]+".webp"
    errors.append(c.convert(image,name)) 
    u.printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

if errors != []:
    u.cprint('Errors:','ERROR')
    for e in errors:
        if e != '':
            print(e)


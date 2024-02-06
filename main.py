#NOTE - Main script to execute the basic file converter
import argparse
import os
from classes.utils import Utils
from classes.converter import Converter
from classes.extenions import Extensions


# DONE - define list of extensions based on argument passed
# DONE - pass the list to listdirectory
# TODO - make most of the script into functions
# TODO - use the __main__ piece to avoid it being executed when testing
# TODO - write unit tests to functions here
# TODO - work on when no file is found, it is erroring at the moment.
# TODO - Change notes for docstring comments!

#NOTE - Defines the command line arguments for the script
def setarguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--directory", help="Converts files in the filder defined: -d <Folder Path>")
    parser.add_argument("-f","--file", help="Converts the file defined: -f <File Path and Name>")
    parser.add_argument("-s","--source", help="Source File Type: -s JPEG", choices=['JPEG','PNG','WEBP'],default='JPEG')
    parser.add_argument("-t","--target", help="Target File Type: -s WEBP", choices=['JPEG','PNG','WEBP'],default='WEBP')
    return parser.parse_args()

if __name__ == '__main__':

    args = setarguments()

    # set instances
    utils = Utils()
    converter = Converter()
    extensions = Extensions()

    errors = []
    lookupext = extensions.getextensions(args.source)
    files = utils.listdirectory(lookupext)
    filecount = len(files)

    # Initial call to print 0% progress
    utils.printProgressBar(0, filecount, prefix = 'Progress:', suffix = 'Complete', length = 50)

    for i,image in enumerate(files):
        name = image.split('.')[0]+".webp"
        errors.append(converter.convert(image,name))
        utils.printProgressBar(i + 1, filecount, prefix = 'Progress:', suffix = 'Complete', length = 50)

    if errors != []:
        utils.cprint('Errors:','ERROR')
        for e in errors:
            if e != '':
                print(e)


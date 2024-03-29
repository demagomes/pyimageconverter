#NOTE - Main script to execute the basic file converter
import argparse
from classes.utils import Utils
from classes.converter import Converter
from classes.extenions import Extensions
from pathlib import Path
from classes.window import Window

def setarguments():
    '''
    Defines the command line arguments for the script

    Returns:
        argparse.Namespace: list of defined command-line arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--directory', help='Converts files in the folder defined, its the default option with local folder ".": -d <Folder Path>',default='.')
    parser.add_argument('-f','--file', help='Converts the file defined: -f <File Path and Name>')
    parser.add_argument('-s','--source', help='Source File Type: -s JPEG', choices=['JPEG','PNG','WEBP'],default='JPEG')
    parser.add_argument('-t','--target', help='Target File Type: -s WEBP', choices=['JPEG','PNG','WEBP'],default='WEBP')
    parser.add_argument('-r','--resize', help='Resizes Image to specified percentage', type=int,choices=[25,50,75,100],default=100)
    parser.add_argument('-g','--gui', help='Enables GUI version', action='store_true')
   
    return parser.parse_args()

if __name__ == '__main__':

    args = setarguments()

    if args.gui:
        #NOTE - GUI version
        app = Window()
        app.mainloop()
    else:
        #NOTE - Terminal version
        # set instances
        utils = Utils()
        converter = Converter()
        extensions = Extensions()

        # set errors list for display after the process is finished
        errors = []

        # check if file argument is present and decide if run for all files in folder or only 1 file
        if args.file != None:
            files = [args.file]
        else:
            # pass the extensions list to the list folder function
            lookupext = extensions.getextensions(args.source)
            files = utils.listdirectory(lookupext,args.directory)
        
        filecount = len(files)

        # print header
        utils.cprint('Python Image Converter','HEADER')
        utils.cprint('https://github.com/demagomes/pyimageconverter','WHITE')

        if filecount == 0:
            errors.append('No Files Found')
        else:
            # Initial call to print 0% progress
            utils.printProgressBar(0, filecount, prefix = 'Progress:', suffix = 'Complete', length = 50)

            for i,image in enumerate(files):
                name = Path(image).stem+extensions.setextension(args.target)
                errors.append(converter.convert(image,name,args.resize))
                utils.printProgressBar(i + 1, filecount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        if errors != []:
            utils.cprint('Errors:','ERROR')
            for e in errors:
                if e != '':
                    print(e)


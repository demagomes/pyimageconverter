
#NOTE - Main script to execute the basic file converter
import os
from classes.utils import Utils
from classes.converter import Converter

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
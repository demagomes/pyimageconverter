
#NOTE - Main script to execute the basic file converter
import os
from classes.utils import Utils
from classes.converter import Converter

# A List of Items
files = os.listdir()
l = len(files)
errors = []
u = Utils()
c = Converter()

# Initial call to print 0% progress
u.printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

for i,image in enumerate(files):
    name = image.split('.')[0]+".webp"
    errors.append(c.convert(image,name)) 
    u.printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

u.cprint('Errors:','ERROR')
for e in errors:
    if e != '':
        print(e)
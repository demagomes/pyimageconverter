#NOTE - Utils class to support the separation of concerns in other classes
import os
from classes.terminalcolours import TerminalColours as tc

class Utils:

    def cprint(self, message, type, endchar='\n'):
        if type == 'HEADER':
            print(f'{tc.HEADER}{message}{tc.ENDC}',end=endchar)
        elif type == 'INFO':
            print(f'{tc.INFO}{message}{tc.ENDC}',end=endchar)
        elif type == 'WARNING':
            print(f'{tc.WARNING}{message}{tc.ENDC}',end=endchar)
        elif type == 'ERROR':
            print(f'{tc.ERROR}{message}{tc.ENDC}',end=endchar)
        elif type == 'OKBLUE':
            print(f'{tc.OKBLUE}{message}{tc.ENDC}',end=endchar)
        elif type == 'OKCYAN':
            print(f'{tc.OKCYAN}{message}{tc.ENDC}',end=endchar)
        elif type == 'WHITE':
            print(f'{tc.WHITE}{message}{tc.ENDC}',end=endchar)


    #NOTE - Basic terminal progress bar. 
    # Source: https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
    def printProgressBar (self,iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = '\r'):
        '''
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. '\r', '\r\n') (Str)
        '''
        percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        self.cprint(f'\r{prefix} |{bar}| {percent}% {suffix}', 'INFO', printEnd)
        # Print New Line on Complete
        if iteration == total: 
            print()

    #NOTE - Directory listing function with param for file extention
    def listdirectory(self,extention,dirpath = '.'):
        # get the unfiltered directory list
        unfiltered = os.listdir(path=dirpath)
        files=[]

        for file in unfiltered:
            # test the argument type
            if type(extention) is list:
                for ex in extention:
                    if file.endswith(ex):
                        files.append(file)
            else:
                if file.endswith(extention):
                    files.append(file)

        return files

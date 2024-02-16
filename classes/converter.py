
from PIL import Image, UnidentifiedImageError

class Converter:
    '''
    Converter class containing all image convertion functions
    '''
    def convert(self,image,newname,percentage = 100):
        '''_summary_

        Args:
            image (str): image name/path
            newname (str): new image name with

        Returns:
            str: a string reponse, empty when sucess and error message when it fails
        '''
        response = ''

        try:
            im = Image.open(image)

            if percentage != 100:
                width = im.size[0]
                height = im.size[1]
                size = int((percentage*width)/100),int((percentage*height)/100)
                newim = im.resize(size)
                newim.save(newname)
            else:
                im.save(newname)

        except UnidentifiedImageError:
            response = 'Cannot Identify File Format: '+image
        except FileNotFoundError:
            response = 'File Not Found: '+ image
        except IsADirectoryError:
            response = 'Cannot Convert a Directory: '+ image
        except OSError as error:
            response = 'An OS Error Occurred: ' + image + ' '+ str(error)
        except Exception as error:
            response = 'An Unexpected Error Occurred: ' + image + ' '+ str(error)

        return response
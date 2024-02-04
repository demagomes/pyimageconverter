#NOTE - converter class using Pillow library

from PIL import Image, UnidentifiedImageError

class Converter:

    def convert(self,image,newname):
        response = ''

        try:
            im = Image.open(image)
            im.save(newname)
        except UnidentifiedImageError:
            response = "Cannot Identigy File Format: "+image
        except FileNotFoundError:
            response = "File Not Found: "+ image
        except IsADirectoryError:
            response = "Cannot Convert a Directory: "+ image
        except OSError as error:
            response = "An Error Occurred: " + image + " "+ error

        return response
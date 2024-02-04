#NOTE - converter class using Pillow library

from PIL import Image, UnidentifiedImageError

class Converter:

    def convert(self,image,newname):
        response = ''

        try:
            im = Image.open(image)
            im.save(newname)
        except UnidentifiedImageError:
            response = "cannot identify image file "+image
        except OSError:
            response = "cannot convert image file "+image

        return response
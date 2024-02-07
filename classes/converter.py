
from PIL import Image, UnidentifiedImageError

class Converter:
    """
    Converter class containing all image convertion functions
    """
    def convert(self,image,newname):
        """_summary_

        Args:
            image (str): image name/path
            newname (str): new image name with

        Returns:
            str: a string reponse, empty when sucess and error message when it fails
        """
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
import os
import pytest
from classes.converter import Converter
from classes.utils import Utils
from classes.extenions import Extensions
from PIL import Image

@pytest.fixture
def getconverterinstance():
    return Converter()

@pytest.fixture
def getutilsinstance():
    return Utils()

@pytest.fixture
def getextensionsinstance():
    return Extensions()

def test_convertimage(getconverterinstance):
    '''Tests convertion to webp

    Args:
        getconverterinstance (Converter): Converter Class is the main class in the project responsible for image conversion
    '''
    # converts the test jpeg image to webp
    # the image is not included in the repo, change the first argument
    # to a local image and add it to gitignore
    getconverterinstance.convert('IMG_1723.jpeg','IMG_1723.webp')

    # asserts the new webpfile exists
    assert os.path.exists('IMG_1723.webp') == True

    # delete the new file
    os.remove('IMG_1723.webp')

def test_convertresizeimage(getconverterinstance):
    '''Tests resizing it to 25% and convertion to webp 

    Args:
        getconverterinstance (Converter): Converter Class is the main class in the project responsible for image conversion
    '''
    # converts the test jpeg image to webp
    # the image is not included in the repo, change the first argument
    # to a local image and add it to gitignore
    getconverterinstance.convert('IMG_1723.jpeg','IMG_1723.webp',25)

    # asserts the new webpfile exists
    assert os.path.exists('IMG_1723.webp') == True
    newimagesize = Image.open('IMG_1723.webp').size
    assert newimagesize == (320,240)

    # delete the new file
    os.remove('IMG_1723.webp')

def test_missingfileerror(getconverterinstance):
    '''Tests for error when file doesnt exist

    Args:
        getconverterinstance (Converter): Converter Class is the main class in the project responsible for image conversion
    '''
        
    # tries to convert an inexistent file
    response = getconverterinstance.convert('IMG_1723.png','newfilename')
    assert response == 'File Not Found: IMG_1723.png'

def test_foldererror(getconverterinstance):
    '''Tests for error when argument is a folder

    Args:
        getconverterinstance (Converter): Converter Class is the main class in the project responsible for image conversion
    '''
    # tries to convert a folder
    response = getconverterinstance.convert('classes','newfilename')
    assert response == 'Cannot Convert a Directory: classes'

def test_folderlisting_str(getutilsinstance):
    '''Tests the listdirectory function with a str argument

    Args:
        getutilsinstance (Utils): Project Utils Class
    '''

    # with 1 jpeg test file in the root of the project
    files = getutilsinstance.listdirectory('.jpeg')
    assert len(files) == 1

def test_folderlisting_list(getutilsinstance):
    '''Tests the listdirectory function with a list argument

    Args:
        getutilsinstance (Utils): Project Utils Class
    '''
    # with 1 jpeg test file in the root of the project
    files = getutilsinstance.listdirectory(['.jpeg','.jpg'])
    assert len(files) == 1

def test_extensionsvalues(getextensionsinstance):
    '''Tests the extensions list values

    Args:
        getextensionsinstance (Extensions): Extensions class injected with pytest.fixture
    '''
    assert getextensionsinstance.JPEG == ['.jpeg','.jpg','.JPEG','.JPG']
    assert getextensionsinstance.PNG == ['.png','.PNG']
    assert getextensionsinstance.WEBP == ['.webp','.WEBP']

def test_getextensions(getextensionsinstance):
    '''Tests the extensions list resposes from getextension function

    Args:
        getextensionsinstance (Extensions): Extensions class injected with pytest.fixture
    '''
    assert getextensionsinstance.getextensions('JPEG') == ['.jpeg','.jpg','.JPEG','.JPG']
    assert getextensionsinstance.getextensions('PNG') == ['.png','.PNG']
    assert getextensionsinstance.getextensions('WEBP') == ['.webp','.WEBP']
    assert getextensionsinstance.getextensions('ANOTHER VALUE') == None
    
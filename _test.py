import os
import pytest
from classes.converter import Converter
from classes.utils import Utils
from classes.extenions import Extensions

@pytest.fixture
def getconverterinstance():
    return Converter()

@pytest.fixture
def getutilsinstance():
    return Utils()

@pytest.fixture
def getextensionsinstance():
    return Extensions()

#NOTE - Tests convertion to webp
def test_convertimage(getconverterinstance):

    # converts the test jpeg image to webp
    # the image is not included in the repo, change the first argument
    # to a local image and add it to gitignore
    getconverterinstance.convert('IMG_1723.jpeg','IMG_1723.webp')

    # asserts the new webpfile exists
    assert os.path.exists("IMG_1723.webp") == True

    # delete the new file
    os.remove('IMG_1723.webp')

#NOTE - Tests for error when file doesnt exist
def test_missingfileerror(getconverterinstance):
    # tries to convert an inexistent file
    response = getconverterinstance.convert('IMG_1723.png','newfilename')
    assert response == 'File Not Found: IMG_1723.png'

#NOTE - Tests for error when file doesnt exist
def test_foldererror(getconverterinstance):
    # tries to convert a folder
    response = getconverterinstance.convert('classes','newfilename')
    assert response == 'Cannot Convert a Directory: classes'

#NOTE - Tests the directory listing function() with string argument
def test_folderlisting_str(getutilsinstance):
    # with 1 jpeg test file in the root of the project
    files = getutilsinstance.listdirectory('.jpeg')
    assert len(files) == 1

#NOTE - Tests the directory listing function() with string argument
def test_folderlisting_list(getutilsinstance):
    # with 1 jpeg test file in the root of the project
    files = getutilsinstance.listdirectory(['.jpeg','.jpg'])
    assert len(files) == 1

def test_extensionsvalues(getextensionsinstance):
    assert getextensionsinstance.JPEG == ['.jpeg','.jpg','.JPEG','.JPG']
    assert getextensionsinstance.PNG == ['.png','.PNG']
    assert getextensionsinstance.WEBP == ['.webp','.WEBP']

def test_getextensions(getextensionsinstance):
    assert getextensionsinstance.getextensions('JPEG') == ['.jpeg','.jpg','.JPEG','.JPG']
    assert getextensionsinstance.getextensions('PNG') == ['.png','.PNG']
    assert getextensionsinstance.getextensions('WEBP') == ['.webp','.WEBP']
    assert getextensionsinstance.getextensions('ANOTHER VALUE') == None
    
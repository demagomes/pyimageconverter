import os
import pytest
# import classes.converter as cv
from classes.converter import Converter

@pytest.fixture
def getclassinstance():
    return Converter()

#NOTE - Tests convertion to webp
def test_convertimage(getclassinstance):
    # converts the test jpeg image to webp
    getclassinstance.convert('IMG_1723.jpeg','IMG_1723.webp')

    # asserts the new webpfile exists
    assert os.path.exists("IMG_1723.webp") == True

    # delete the new file
    os.remove('IMG_1723.webp')

#NOTE - Tests for error when file doesnt exist
def test_missingfileerror(getclassinstance):
    # tries to convert an inexistent file
    response = getclassinstance.convert('IMG_1723.png','newfilename')
    assert response == 'File not found: IMG_1723.png'


#NOTE - Tests for error when file doesnt exist
def test_foldererror(getclassinstance):
    # tries to convert a folder
    response = getclassinstance.convert('classes','newfilename')
    assert response == 'Cannot Convert a Directory: classes'

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

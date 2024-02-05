class Extensions:
    """
    Extensions Class/Enum of file types.
    """

    JPEG=['.jpeg','.jpg','.JPEG','.JPG']
    WEBP=['.webp','.WEBP']
    PNG=['.png','.PNG']

    def getextensions(self,ext):
        if ext == 'JPEG':
            return self.JPEG
        elif ext == 'WEBP':
            return self.WEBP
        elif ext == 'PNG':
            return self.PNG
        else:
            #TODO - throw an error
            #TODO - create a test
            pass





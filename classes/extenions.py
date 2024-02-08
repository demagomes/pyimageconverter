class Extensions:
    '''
    Extensions Class/Enum of file types.
    '''

    JPEG=['.jpeg','.jpg','.JPEG','.JPG']
    WEBP=['.webp','.WEBP']
    PNG=['.png','.PNG']

    def getextensions(self,ext):
        '''gets and returns extension list for each extension enum

        Args:
            ext (str): string representing the file extenion

        Returns:
            list[str]: list extensions as strings
        '''
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



    def setextension(self,ext):
        '''set file extension based on extension argument

        Args:
            ext (str): string representing the file extenion

        Returns:
            _type_: returns the extension to be used in the new filename
        '''
        if ext == 'JPEG':
            return '.jpeg'
        elif ext == 'WEBP':
            return '.webp'
        elif ext == 'PNG':
            return '.png'


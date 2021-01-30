import diccionarios

class Reflector():
    def __init__(self, objDic, inicio):
        self.inicio = inicio
        self.dic = objDic
        
        self.__alphaEncode = self.dic.createAlphaEncoder(self.inicio)
    
    def getCharEncode(self, indice):
        if indice > 26:
            indice -= 27
        return self.__alphaEncode[indice]
    
    def getIndexChar(self, char):
        return self.__alphaEncode.index(char)
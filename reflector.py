import diccionarios

class Reflector():
    def __init__(self, objDic, inicio):
        self.inicio = inicio
        self.dic = objDic
        
        self.__alphaEncode = self.dic.createAlphaEncoder(self.inicio)
    
    def getCharEncode(self, indice):
        if indice > 26:
            indice = indice % 26
        elif indice < 0:
            indice = ((indice*(-1)) % 26)
        return self.__alphaEncode[indice]
    
    def getIndexChar(self, char):
        return self.__alphaEncode.index(char)
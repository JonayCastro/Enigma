import diccionarios

class Reflector():
    def __init__(self, objDic, inicio):
        self.inicio = inicio
        self.dic = objDic
        self.paso = 14
        
        self.__alphaEncode = self.dic.createAlphaEncoder(self.inicio)
    
    def codifica(self, char):
        c = self.__alphaEncode.index(char)+self.paso
        if c > 26:
            c = (c-(c%26))
        return self.__alphaEncode[c]
        
import diccionarios

class Reflector():
    def __init__(self, objDic, inicio):
        self.inicio = inicio
        self.__paso = 3
        self.dic = objDic
        
        self.__alphaEncode = self.dic.createAlphaEncoder(self.inicio)

    def encoder(self, indice):
        pos = indice+self.__paso
        if pos > 26:
            pos = 0
        return self.__alphaEncode[pos]

    def decoder(self, char):
        pos = self.__alphaEncode.index(char)+self.__paso
        if pos > 26:
            pos = 0
        return self.dic.getCharSpanish(pos)
    
    def getSetPaso(self, paso=None):
        if(paso == None):
            return self.__paso
        else:
            self.__paso = paso
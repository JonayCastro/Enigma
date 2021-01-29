import diccionarios

class Rotor:
    def __init__(self, objDic, id, paso, inicio):
        self.__id = id
        self.__paso = paso
        self.inicio = inicio
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

    def getPositionEnc(self, char):
        return self.__alphaEncode.index(char)
    
    def aumentaPaso(self):
        self.__paso+=1
    
    def reducePaso(self):
        self.__paso-=1
    
    def getId(self):
        return self.__id
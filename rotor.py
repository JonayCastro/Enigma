import diccionarios

class Rotor:
    def __init__(self, id, paso, inicio):
        self.__id = id
        self.__paso = paso
        self.inicio = inicio

        dic = diccionarios.Diccionario()

        self.alphaSpanish = dic.createSpanishAlpha()
        self.__alphaEncode = dic.createAlphaEncoder(self.inicio)
         
    def encoder(self, character):
        return self.__alphaEncode[self.alphaSpanish.index(character)+self.__paso]

    def decoder(self, character):
        return self.alphaSpanish[self.__alphaEncode.index(character)+self.__paso]
    
    def getSetPaso(self, paso=None):
        if(paso == None):
            return self.__paso
        else:
            self.__paso = paso
    
    def aumentaPaso(self):
        self.__paso+=1
    
    def reducePaso(self):
        self.__paso-=1
    
    def getId(self):
        return self.__id
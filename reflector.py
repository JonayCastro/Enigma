import diccionarios

class Reflector():
    def __init__(self, inicio):
        self.inicio = inicio
        self.__paso = 3

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
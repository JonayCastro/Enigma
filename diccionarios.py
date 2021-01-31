from string import ascii_uppercase as ALPHA

class Diccionario:
    def __init__(self):
        self.alphaSpanish = []

    def createSpanishAlpha(self):
        for i in range(0,len(ALPHA)):
            if i == 14:
                self.alphaSpanish.append("Ñ")
            self.alphaSpanish.append(ALPHA[i])
        return self.alphaSpanish

    def createAlphaEncoder(self, inicio):
        alphaEncode = (self.alphaSpanish[inicio:]+self.alphaSpanish[:inicio])
        return alphaEncode
    
    def getPositionSpanish(self, char):
        return self.alphaSpanish.index(char)
    
    def getCharSpanish(self, indice):
        if indice > 26:
            indice = indice % 26
        elif indice < 0:
            indice = ((indice*(-1)) % 26)
        return self.alphaSpanish[indice]
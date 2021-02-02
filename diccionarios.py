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
        try:
            alphaEncode = (self.alphaSpanish[inicio:]+self.alphaSpanish[:inicio])
        except:
            alphaEncode = (self.alphaSpanish[self.alphaSpanish.index(inicio):]+self.alphaSpanish[:self.alphaSpanish.index(inicio)])
        return alphaEncode
    
    def getPositionSpanish(self, char):
        return self.alphaSpanish.index(char)
    
    def getCharSpanish(self, indice):
        if indice > len(self.alphaSpanish):
            indice = indice % len(self.alphaSpanish)
        return self.alphaSpanish[indice]
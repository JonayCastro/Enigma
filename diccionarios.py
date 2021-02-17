from string import ascii_uppercase as ALPHA

class Diccionario:
    def __init__(self):
        self.alphaSpanish = []
        self.specialCharts = ["?","¿",".",",","-","_"," "]

    def createSpanishAlpha(self):
        for i in range(0,len(ALPHA)):
            if i == 14:
                self.alphaSpanish.append("Ñ")
            self.alphaSpanish.append(ALPHA[i])
        #self.alphaSpanish.append(" ")
        for j in self.specialCharts:
            self.alphaSpanish.append(j)
        return self.alphaSpanish

    def createAlphaEncoder(self, inicio):
        return self.alphaSpanish[self.alphaSpanish.index(inicio):]+self.alphaSpanish[:self.alphaSpanish.index(inicio)]

    def getPositionSpanish(self, char):
        return self.alphaSpanish.index(char)

    def createAlphaReversed(self, item):
        return list(reversed(item))
    
    def getCharSpanish(self, indice):
        return self.alphaSpanish[indice]
from string import ascii_uppercase as ALPHA

class Diccionario:
    def __init__(self):
        self.alphaSpanish = []

    def createSpanishAlpha(self):
        for i in range(0,len(ALPHA)):
            if i == 14:
                self.alphaSpanish.append("Ñ")
            self.alphaSpanish.append(ALPHA[i])
        print(self.alphaSpanish)
        return self.alphaSpanish

    def createAlphaEncoder(self, inicio):
        alphaEncode = (self.alphaSpanish[inicio:]+self.alphaSpanish[:inicio])
        print(alphaEncode)
        return alphaEncode
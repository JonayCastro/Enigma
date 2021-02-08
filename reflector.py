import diccionarios

class Reflector():
    def __init__(self, objDic, initDat):
        self.__initDat = initDat.upper()
        self.dic = objDic

        self.__alphaEncodeIn = []
        self.__alphaEncodeOut = []
    
    def init(self):
        self.__alphaEncodeIn = self.dic.createAlphaEncoder(self.__initDat)
        self.__alphaEncodeOut = self.dic.createAlphaReversed(self.__alphaEncodeIn)
        
    def codifica(self, item):
        return self.__alphaEncodeOut.index(self.__alphaEncodeIn[item])

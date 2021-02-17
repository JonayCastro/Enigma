import diccionarios

class Rotor:
    def __init__(self, objDic, id, initDat):
        self.__id = id
        self.dic = objDic
        self.__paso = initDat[0].upper()
        self.__indexIn = initDat[1].upper()
        self.__indexOut = initDat[2].upper()

        self.__alphaEncodeIn = []
        self.__alphaEncodeOut = []

    def init(self):
        self.__alphaEncodeIn = self.dic.createAlphaEncoder(self.__indexIn)
        self.__alphaEncodeOut = self.dic.createAlphaEncoder(self.__indexOut)

    def codificaIda(self, item):
        return self.__alphaEncodeOut.index(self.__alphaEncodeIn[item])

    def codificaVuelta(self,item):
        return self.__alphaEncodeIn.index(self.__alphaEncodeOut[item])

    def avanza(self):
        self.__alphaEncodeIn = self.dic.createAlphaEncoder(self.__alphaEncodeIn[1])
        #self.__alphaEncodeOut = self.dic.createAlphaEncoder(self.__alphaEncodeOut[1])

    def isInPaso(self):
        if self.__alphaEncodeIn[0] == self.__paso:
            return True
        return False
    
    def getId(self):
        return self.__id
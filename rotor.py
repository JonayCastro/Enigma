import diccionarios

class Rotor:
    def __init__(self, objDic, id, paso, indexIn, indexOut):
        self.__id = id
        self.dic = objDic
        self.__paso = paso
        self.__indexIn = indexIn
        self.__indexOut = indexOut


        self.__alpahEncodeIn = self.dic.createAlphaEncoder(self.__indexIn)
        self.__alpahEncodeOut = self.dic.createAlphaEncoder(self.__indexOut)

        print(self.__alpahEncodeIn)
        print(self.__alpahEncodeOut)
    
    def codifica(self, char):
        return self.__alpahEncodeOut[self.__alpahEncodeIn.index(char)]
    
    def avanza(self):
        self.__alpahEncodeOut = self.dic.createAlphaEncoder(self.__alpahEncodeOut[1])
    
    def getId(self):
        return self.__id
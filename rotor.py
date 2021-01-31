import diccionarios

class Rotor:
    def __init__(self, id, paso, inicio):
        self.__id = id
        self.__paso = paso
        self.inicio = inicio
        
    def getSetPaso(self, paso=None):
        if(paso == None):
            return self.__paso
        else:
            self.__paso = paso
    
    def reducePaso(self):
        self.__paso-=1
    
    def getId(self):
        return self.__id
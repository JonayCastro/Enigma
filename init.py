import rotor,filtro,sys,diccionarios,reflector

class Init():
    def __init__(self, msg, initRotor1, initRotor2, initRotor3, initReflector, func):
        self.rotors = []
        self.initRotors = []
        self.initRotor1 = initRotor1
        self.initRotor2 = initRotor2
        self.initRotor3 = initRotor3
        self.initReflector = initReflector
        self.reflector = None
        self.msg = msg
        self.func = func

        self.procesaInit()
    def procesaInit(self):
        dic = diccionarios.Diccionario()
        self.initRotors.append(dic.createSpanishAlpha().index(self.initRotor1))
        self.initRotors.append(dic.createSpanishAlpha().index(self.initRotor2))
        self.initRotors.append(dic.createSpanishAlpha().index(self.initRotor3))
        self.initRotors.append(dic.createSpanishAlpha().index(self.initReflector))
    
    def run(self):
        self.msg = self.msg.upper()
        f = filtro.Filtro(self.msg)
        
        if(f.isCorrect()):
            self.reflector = reflector.Reflector(self.initRotors[3])
            for i in range(3):
                self.rotors.append(rotor.Rotor(i, 0, self.initRotors[i]))
            if self.func == 1:
                self.coder()
            elif self.func == 2:
                self.decoder()

    def decoder(self):
        for i in self.msg:
            print(self.rotors[0].decoder(i))
            self.rotors[0].reducePaso()
    def coder(self):
        for i in self.msg:
            print(self.rotors[0].encoder(i))
            self.rotors[0].aumentaPaso()
if __name__ == "__main__":
    '''
        func = 1 Codificar mensaje
        func = 2 Decodificar mensaje
    '''
    Init("vvsty","G","H","C", "N", func).run()


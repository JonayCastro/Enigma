import rotor,sys,re,diccionarios,reflector

class Init():
    def __init__(self, msg, initRotor1, initRotor2, initRotor3, initReflector):
        self.rotors = []
        self.initRotors = []
        self.initRotor1 = initRotor1
        self.initRotor2 = initRotor2
        self.initRotor3 = initRotor3
        self.initReflector = initReflector
        self.reflector = None
        self.msg = msg
        self.func = 2
        self.salida = ""

        self.dic = diccionarios.Diccionario()
        self.dic.createSpanishAlpha()
        
        self.procesaInit()
    def procesaInit(self):
        
        self.initRotors.append(self.dic.getPositionSpanish(self.initRotor1.upper()))
        self.initRotors.append(self.dic.getPositionSpanish(self.initRotor2.upper()))
        self.initRotors.append(self.dic.getPositionSpanish(self.initRotor3.upper()))
        self.initRotors.append(self.dic.getPositionSpanish(self.initReflector.upper()))
    
    def passCtrl(self):
        totalPass = 0
        for i in range(len(self.rotors)):
            totalPass+=self.rotors[i].getSetPaso()
        selec = None
        if totalPass <= 26:
            selec = 0
        elif totalPass <=53:
            selec = 1
        elif totalPass <= 80:
            selec = 2
        elif totalPass > 80:
            selec = 3
            for i in self.rotors:
                i.getSetPaso(0)
            
        if self.func == 1:
            if selec != 3:
                if self.rotors[selec].getSetPaso() >= 26:
                    self.rotors[selec].getSetPaso(0)
                else:
                    self.rotors[selec].aumentaPaso()
        elif self.func == 2:
            if selec != 3:
                if self.rotors[selec].getSetPaso() <= 0:
                    self.rotors[selec].getSetPaso(26)
                else:
                    self.rotors[selec].reducePaso()
        
    def run(self):
        self.msg = self.msg.upper()
        
        if(re.compile(r'[\W_]')):
            self.reflector = reflector.Reflector(self.dic, self.initRotors[3])
            for i in range(3):
                self.rotors.append(rotor.Rotor(i, self.initRotors[i], self.initRotors[i]))
            for c in self.msg:
                if c != " ":
                    self.passCtrl()
                    if self.func == 2:
                        onePass = self.reflector.getIndexChar(c)
                        for r in self.rotors:
                            onePass-=r.getSetPaso()
                        self.salida+=self.dic.getCharSpanish(onePass)
                    
            print(self.salida)
        else:
            print("Solo se permiten letras entra de la 'A' a la 'Z'")

if __name__ == "__main__":
    '''
        parametros de Init(msg, rotor1, rotor2, rotor3, reflector, func):
            msg-> Mensaje a codificar o decoficar
            rotor1-> Posición de inicio del rotor 1
            rotor2-> Posición de inicio del rotor 2
            rotor3-> Posición de inicio del rotor 3
            reflector-> Posición de inicio del reflector (aunque este no varía se puede establecer una posición inicial)
            func-> Modo de funcionamiento, son los siguientes:
                Valor 1 = Codificar msg
                Valor 2 = Decodificremos msg
    '''

    Init("sknw","a","a","a","a").run()
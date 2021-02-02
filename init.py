import rotor,sys,re,diccionarios,reflector

class Init():
    def __init__(self, msg, initRotor1, initRotor2, initRotor3, initRef):
        self.rotors = []
        self.initRotors = []
        self.initRotor1 = initRotor1
        self.initRotor2 = initRotor2
        self.initRotor3 = initRotor3
        self.initReflector = initRef
        self.reflector = None
        self.msg = msg
        self.func = 2
        self.salida = ""
        self.totalPass = 0

        self.dic = diccionarios.Diccionario()
        self.dic.createSpanishAlpha()
        
        self.procesaInit()
        
    def procesaInit(self):
        
        self.initRotors.append(self.dic.getPositionSpanish(self.initRotor1.upper()))
        self.initRotors.append(self.dic.getPositionSpanish(self.initRotor2.upper()))
        self.initRotors.append(self.dic.getPositionSpanish(self.initRotor3.upper()))
        self.initRotors.append(self.dic.getPositionSpanish(self.initReflector.upper()))
    
    def avanceCtrl(self):
        selec = 0
        for i in range(len(self.rotors)):
            if self.rotors[i].isInPaso():
                selec = i

        self.rotors[selec].avanza()
            
    def run(self):
        self.msg = self.msg.upper()
        
        if(re.compile(r'[\W_]')):
            self.reflector = reflector.Reflector(self.dic, self.initRotors[3])
            for i in range(1):
                paso = self.dic.getPositionSpanish("B")
                indexIn = self.dic.getPositionSpanish("B")
                indexOut = self.dic.getPositionSpanish("C")
                self.rotors.append(rotor.Rotor(self.dic, i, paso, indexIn, indexOut))
                
            
            for c in self.msg:
                if c != " ":
                    self.reflector.codifica(self.rotors[0].codifica(c))
                    self.salida+=self.reflector.codifica(self.rotors[0].codifica(c))
                    self.rotors[i].avanza()
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

    Init("ap","a","a","a","b").run()
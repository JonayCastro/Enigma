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

        self.dic = diccionarios.Diccionario()
        self.dic.createSpanishAlpha()
        

        self.procesaInit()
    def procesaInit(self):
        
        self.initRotors.append(self.dic.getPositionSpanish(self.initRotor1))
        self.initRotors.append(self.dic.getPositionSpanish(self.initRotor2))
        self.initRotors.append(self.dic.getPositionSpanish(self.initRotor3))
        self.initRotors.append(self.dic.getPositionSpanish(self.initReflector))
    
    def run(self):
        self.msg = self.msg.upper()
        f = filtro.Filtro(self.msg)
        
        if(f.isCorrect()):
            self.reflector = reflector.Reflector(self.dic, self.initRotors[3])
            for i in range(3):
                self.rotors.append(rotor.Rotor(self.dic, i, 0, self.initRotors[i]))
            
            #Codificar----------------------------------------------------------------
            if self.func == 1:
                for i in self.msg:
                    #print(self.rotors[0].encoder(self.dic.getPositionSpanish(i)))
                    #self.rotors[0].aumentaPaso()
                    if i != " ":
                        onePass = self.rotors[0].encoder(self.dic.getPositionSpanish(i))
                        secondPass = self.rotors[1].encoder(self.rotors[0].getPositionEnc(onePass))
                        thidPass = self.rotors[2].encoder(self.rotors[0].getPositionEnc(secondPass))
                        print(self.reflector.encoder(self.rotors[0].getPositionEnc(thidPass)))
                        
                        for r in range(len(self.rotors)):
                            paso = self.rotors[r].getSetPaso()
                            if paso <= 26:
                                self.rotors[r].aumentaPaso()
                            elif paso == 26:
                                self.rotors[r].getSetPaso(0)
                                if r+1 != 3:
                                    self.rotors[r+1].aumentaPaso()
                                
            #-------------------------------------------------------------------------
            
            #Decodificar--------------------------------------------------------------
            elif self.func == 2:
                for i in self.msg:
                    print(self.rotors[0].decoder(i))
                    self.rotors[0].reducePaso()
            #-------------------------------------------------------------------------
        
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
    Init("aa","G","H","C","N", 1).run()


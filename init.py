import rotor,sys,re,diccionarios,reflector

class Init():
    def __init__(self, msg):
        self.rotors = []
        self.reflector = None
        self.msg = msg
        self.salida = ""
        """
            La variable initDatsRotors es una lista de dos dimensiones que contiene las posiciones de inicio y la posición
            de salto de cada rotor en el siguiente orden:
                [posición de salto, posición parrilla entrada, posición parilla salida]
        """
        self.initDatsRotors = [["E","W","G"],["L","f","L"],["S","o","Q"]]
        self.initDatsReflector = "e"
        self.dic = diccionarios.Diccionario()
        self.dic.createSpanishAlpha()
        
    
    def avanceCtrl(self):
        self.rotors[0].avanza()
        if self.rotors[0].isInPaso():
            self.rotors[1].avanza()
        if self.rotors[1].isInPaso():
            self.rotors[2].avanza()
            
    def run(self):
        self.msg = self.msg.upper()
        
        if(re.compile(r'[\W_]')):
            self.reflector = reflector.Reflector(self.dic, self.initDatsReflector)
            self.reflector.init()
            for i in range(3):
                r = rotor.Rotor(self.dic, i, self.initDatsRotors[i])
                r.init()
                self.rotors.append(r)
            for c in self.msg:
                
                one = self.dic.getPositionSpanish(c)
                    
                #codifica ida rotor-------------------------------------
                two = one
                for i in self.rotors:
                    two = i.codificaIda(two)
                #-------------------------------------------------------

                #codifica reflector-------------------------------------
                three = self.reflector.codifica(two)
                #-------------------------------------------------------

                #codifica vuelta rotor----------------------------------
                four = three
                for j in reversed(self.rotors):
                    four = j.codificaVuelta(four)
                #-------------------------------------------------------

                five = self.dic.getCharSpanish(four)
                    
                self.salida+=five
                self.avanceCtrl()
                    
            #print(self.salida)
            return self.salida
        else:
            #print("Solo se permiten letras entre la 'A' a la 'Z'")
            return "Solo se permiten letras entre la 'A' a la 'Z'"

if __name__ == "__main__":

    print(Init(")VX*>#MNI)O85N2X$?9M5>3'^+YY=T0+Y#P").run())
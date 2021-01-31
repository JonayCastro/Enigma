from tkinter import *
from tkinter import ttk

class Ventana(Tk):
    size = "648x480"
    title = "Enigma"
    
    def __init__(self):
        Tk.__init__(self)
        
        
    
    def start(self):
        self.mainloop()
    
if __name__ == "__main__":
    app = Ventana()
    app.start()
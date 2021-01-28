class Filtro:
    def __init__(self, msg):
        self.msg = msg

    def isCorrect(self):
        if(self.msg.isalpha()):
            return True
        else:
            return False
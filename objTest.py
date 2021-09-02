

class spriteInfo:
    def __init__(self, xcoord, ycoord):
        self.xcoord = xcoord
        self.ycoord = ycoord
    def getx(self):
        return self.xcoord
        
yes = spriteInfo(50,100)
print(yes.getx)


class spriteInfo:
    def __init__(self, xcoord, ycoord):
        self.xcoord = xcoord
        self.ycoord = ycoord
    def get_x(self):
        return self.xcoord
        
yes = spriteInfo(50,100)
print(yes.get_x)
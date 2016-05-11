

two_three = 0

names = range(100)


def newname():
    name = names[0]
    names.remove(name)
    return name


class Signal():
    def __init__(self,x,type):
        self.pos = [x,t]
        self.type = type
        if self.type in ("ZICK","zick","init"):
            self.v = 0.1
        if self.type in ("ZACK","zack"):
            self.v = -0.1
        if self.type in ("w0","wa","wb","wr"):
            self.v = 0
        self.collision = False
        signale.append(self)
    def move(self):
        self.pos[0]=self.pos[0]+self.v
        self.pos[1]= t
    def collide(self,signal2,signal3):
        if self.type == "init":
            if signal2.type == "wb":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp.append(newname())
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"zack")
                temp[1] = Signal(self.pos[0],"wb")
                temp[2] = Signal(self.pos[0],"ZICK")
        if self.type == "zick":
            if signal2.type == "wb" and signal3.type != "ZACK":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"ZICK")
            if signal2.type == "wb" and signal3.type == "ZACK":
                signale.remove(self)
                signale.remove(signal2)
                signale.remove(signal3)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"wr")
            if signal2.type == "ZACK" and signal3.type == "wb":
                signale.remove(self)
                signale.remove(signal2)
                signale.remove(signal3)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"wr")
            if signal2.type == "ZACK" and signal3.type != "wb":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"wr")
        if self.type == "ZICK":
            if signal2.type == "wa":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"ZACK")
            if signal2.type == "ZACK":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"wr")
        if self.type == "zack":
            if signal2.type == "w0":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"w0")
                temp[1] = Signal(self.pos[0],"zick")
        if self.type == "ZACK":
            if signal2.type == "wb" and signal3.type != "zick":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"ZACK")
                temp[1] = Signal(self.pos[0],"wb")
            if signal2.type == "ZICK":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"wr")
            if signal2.type == "zick" and signal3.type != "wb":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"wr")
            if signal2.type == "wb" and signal3.type == "zick":
                signale.remove(self)
                signale.remove(signal2)
                signale.remove(signal3)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"wr")
            if signal2.type == "zick" and signal3.type == "wb":
                signale.remove(self)
                signale.remove(signal2)
                signale.remove(signal3)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"wr")
        if self.type == "w0":
            if signal2.type == "zack":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"w0")
                temp[1] = Signal(self.pos[0],"zick")
        if self.type == "wa":
            if signal2.type == "ZICK":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"ZACK")
        if self.type == "wb":
            if signal2.type == "init":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp.append(newname())
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"zack")
                temp[1] = Signal(self.pos[0],"wb")
                temp[2] = Signal(self.pos[0],"ZICK")
            if signal2.type == "zick" and signal3.type != "ZACK":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"ZICK")
            if signal2.type == "zick" and signal3.type == "ZACK":
                signale.remove(self)
                signale.remove(signal2)
                signale.remove(signal3)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"wr")
            if signal2.type == "ZACK" and signal3.type != "zick":
                signale.remove(self)
                signale.remove(signal2)
                temp = []
                temp.append(newname())
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"ZACK")
                temp[1] = Signal(self.pos[0],"wb")
            if signal2.type == "ZACK" and signal3.type == "zick":
                signale.remove(self)
                signale.remove(signal2)
                signale.remove(signal3)
                temp = []
                temp.append(newname())
                temp[0] = Signal(self.pos[0],"wr")
signale = []
def checkCollision():
    for signal in signale:
        for signal2 in signale:
            if signal.pos == signal2.pos and signal2.collision != True and signal2 != signal:
                for signal3 in signale:
                    if signal3.pos == signal2.pos and signal3.collision != True and signal3 != signal2 and signal3 != signal:
                        signal.collision = True
                        signal2.collision = True
                        signal3.collision = True
                        signal.collide(signal2,signal3)
                    else:
                        global two_three
                        two_three = 1
                if two_three == 1:
                    signal.collision = True
                    signal2.collision = True
                    signal.collide(signal2,None)
                    two_three = 0
    for signal in signale:
        if signal.collision == True:
            signal.collision = False







t=0
sol = None
while t<500 and sol == None:
    t += 1
    start1 = Signal(0.0,"init")
    start2 = Signal(1.0,"wb")
    start3 = Signal(4.0,"wa")
    for signal in signale:
        checkCollision()
    for signal in signale:
        if signal.type == "wr":
            sol = signal.pos[0]
            break
print sol

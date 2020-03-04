import sys

scale = 100

minx = 6*scale
miny = 6*scale

filename = sys.argv[1]


class box():
    def __init__(self,l,b,x,y):
        self.x = x
        self.y = y
        self.l = l
        self.b = b
        self.connections = []
        self.neighbors = []

    def addconnection(self,a):
        self.connections.append(a)

    def addneighbor(self,a):
        self.neighbour.append(a)

f = open(filename,'r')
lines = f.readlines()

boxes = []

for line in lines:
    values = line.split(' ')

    try:
        if(values[1] == "B"):
            net = box(int(values[2]),int(values[3]),int(values[4]),int(values[5][:-2]))
            boxes.append(net)
    except :
        pass
        # print("ERROR")

error_pairs_set = []

for first in range(len(boxes)):
    for second in range(first+1,len(boxes)):
        # print(first,second)
        # print(boxes[first].x,boxes[first].y,boxes[first].l,boxes[first].b)
        # print(boxes[second].x,boxes[second].y,boxes[second].l,boxes[second].b)
        xdistance = boxes[first].x - boxes[second].x
        ydistance = boxes[first].y - boxes[second].y
        if(xdistance<0):
            xdistance *= -1
        if(ydistance<0):
            ydistance *= -1

        # print(xdistance,ydistance)

        xrule = xdistance - 0.5*boxes[first].l - 0.5*boxes[second].l
        yrule = ydistance - 0.5*boxes[first].b - 0.5*boxes[second].b

        # print(xrule,yrule)

        if(xrule>minx):
            pass
            # print(first,second)
            # print(xrule,yrule)
        elif (yrule>miny):
            pass
            # print(first,second)
            # print(xrule,yrule)
        else :
            if(xrule>0 or yrule>0):
                print("POSSIBLE DRC ERROR: SPACING")
                print(first,second)
                print(xrule,yrule)
                error_pair = []
                error_pair.append(first)
                error_pair.append(second)
                error_pairs_set.append(error_pair)

print(error_pairs_set)
print(str(len(error_pairs_set))+" POSSIBLE ERRORS")

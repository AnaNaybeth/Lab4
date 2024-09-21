import math
def dis(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
p1=(3,6)
p2=(4,8)
print(dis(p1,p2))
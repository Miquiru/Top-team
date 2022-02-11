def longueur(xA,yA,xB,yB):
    return ((xB-xA)**2 + (yB-yA)**2 )**0.5

A= (-2,5)
B = (7,3)
print(longueur(*A,*B))
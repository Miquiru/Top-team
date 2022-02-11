def longueur(xA,yA,xB,yB):
    return ((xB-xA)**2 + (yB-yA)**2 )**0.5

points ={'xA':-2 ,'yA':5 ,'xB':7 ,'yB':3}
print(longueur(**points))
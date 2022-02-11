def longueur(xA,yA,xB,yB):
    return ( (xB-xA)**2 + (yB-yA)**2 )**0.5

def longTotale(points):
    somme = ...
	prem = ...
    for key,value in points.items():
        if prem:
            previous = ...
            prem = ...
        else:
            somme += ...
            previous = ...

    return somme

points = {
    'A' : (-2,4),
    'B' : (1,-2),
    'C' : (3,7),
    'D' : (5,-3)
}

print( longTotale(points) )
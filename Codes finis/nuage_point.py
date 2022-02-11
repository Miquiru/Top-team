import random
from math import sqrt
from random import randint

_ref = [
  (25,  7),
  (39, 19),
  (15, 23),
  (24, 21),
  (35, 11),
  (38,  9),
  (41, 33),
  (12, 34),
  (22, 37),
  ( 8, 15)
]
t =[
  (25,  7),
  (39, 19),
  (15, 23),
  (24, 21),
  (35, 11),
  (38,  9),
  (41, 33),
  (12, 34),
  (22, 37),
  ( 8, 15)
]

def distance(p:tuple, q:tuple) ->float:
    """calcule la distance entre deux points"""
    return round(((q[0] - p[0])**2 + (q[1] - p[1])**2)**(1 / 2), 3)
assert distance((1.5, 2.8), (1.5, 3.8)) == 1.0


def tableau(n: int) -> list:
    """renvoie un tableau de n coordonnées aléatoires"""
    list_coord = [(randint(0, 100), randint(0, 100)) for i in range(n)]
    list_coord_final = list()
    for elt in list_coord:
        if elt not in list_coord_final:
            list_coord_final.append(elt)
    return list_coord_final


def sous_tableaux_tries(t: list) -> tuple:
    """renvoie deux tableaux qui possédent les tris par absicces et ordonnées"""
    tx = sorted(t, key=lambda x: x[0])
    ty = sorted(t, key=lambda x: x[1])
    return tx, ty


def plus_courte_distance_naive(t: list):
    """renvoie p, q, delta avec p et q les points les plus proches et delta la distance entre eux"""
    list_triplet = list()
    for elt_d in t:
        for elt_a in t:
            if elt_d != elt_a:
                triplet = distance(elt_d, elt_a), elt_d, elt_a
                list_triplet.append(triplet)

    return sorted(list_triplet, key=lambda x: x[0])[0]


def scinde_tableaux(tx, ty):
    n = len(tx)
    tgx = tx[0 : n//2]
    tdx = tx[n//2:]
    tgy = [0]*(n//2)
    tdy = [0]*(n-n//2)
    g=0
    d=0
    med=tgx[-1]
    for i in range(n):
        if ty[i][0] < med[0] or (ty[i][0] == med[0] and ty[i][1] <= med[1] and g < n//2):
            tgy[g] = ty[i]
            g += 1
        else:
            tdy[d] = ty[i]
            d += 1
    return med[0], tgx, tdx, tgy, tdy
         

def bandeVerticale(ty , delta , medx):
    """Crée un tableau contenant les points issus du tableau ty et à une distance inférieure à delta autour de medx.
    Entrées : le tableau ty des points de la bande trié par ordonnée puis par abscisse , la diamètre delta , l ’ abscisse du point
    médian medx.
    Sortie : le tableau des points d’abscisses comprise entre medx−delta et medx+delta (et trié par ordonnée)
    """
    ty_bande = [] #Tableau des points à déterminer
    n = len(ty)
    j = 1
    for i in range(n):
        if medx-delta <= ty[i][0] and ty[i][0] <= medx+delta :
            ty_bande.append(ty[i])
            j += 1
    return ty_bande


def dist_min_bande(ty_bande, delta):
    """
    Entrées  :   le  tableau  ty_bande de points  de  la  bande centrale   trié   par  ordonnée puis abscisse   ;   delta   la  plus   petite   distance entre  deux points  situés   à  gauche ou deux points  situés   à  droite .
    Sorties   :   Un quadruplet res  =  (b,p1,p2, delta )  où b  est  un booléen qui vaut  False  s ’ il   n’y  a  pas  de point  dans ty_bande à distance   inférieure   à  delta   et  sinon p1,  p2 sont  les   points   les   plus  proches et   delta   leur  distance .
    """
    n = len(ty_bande)
    res = (False, (0, 0), (0, 0), 0)
    list_res = list()
    for i in range(n):
        if i < len(ty_bande) - 1:
            list_res.append((True, ty_bande[i], ty_bande[i + 1],distance(ty_bande[i],ty_bande[i + 1])))
    return sorted(list_res, key=lambda x: x[0])[0]

def plus_courte_dist_dpr(tx, ty):
    if len(tx) < 4:  #Seuil de la récursivité : appel de la fonction non-récursive
        delta = plus_courte_distance_naive(tx)
        return delta
		
    else:  #Mise en place de la récursivité ("multiple" puisqu'on agit sur tx et ty) 
		#medx, tgx, tdx, tgy, tdy = scinde_tableaux(tx, ty)
		#pg0, pg1, delta1 = plus_courte_dist_dpr(tgx, tgy)
		(pd0, pd1, delta2) = plus_courte_dist_dpr(tdx,
		if delta1 < delta2:  #Combinaison
			p0, p1, delta = pg0, pg1, delta1
		else:
			p0, p1, delta = pd0, pd1, delta2
        
		ty_bande = bandeVerticale(ty, delta, medx)
		b, p0_bande, p1_bande, delta_bande = dist_min_bande(ty_bande, delta)

        if b == True: #Cas où le minimum est dans la bande
            p0, p1, delta = p0_bande, p1_bande, delta_bande
        return p0, p1, delta

l = scinde_tableaux(sous_tableaux_tries(t)[0], sous_tableaux_tries(t)[1])

n = plus_courte_distance_naive(t)

r = bandeVerticale(sous_tableaux_tries(t)[1], 20, l[0])

print(dist_min_bande(r, 20))
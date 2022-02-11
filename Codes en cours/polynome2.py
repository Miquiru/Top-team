def polynome(**coef):
    e = 0
    for key,value in coef.items():
        print('Le coefficient du terme de degré {} est : {}'.format(e,value))
        e += 1

polynome(coef0 = -9, coef1 = 2, coef2 = 5)
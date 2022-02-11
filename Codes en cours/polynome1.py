def polynome(*coef):
    r = ''
    for e in range(len(coef)):
        if e == 0 and coef[e] != 0:
            r += str( coef[e] )
        elif e == 1:
            if coef[e] == 1:
                r += '+x'
            elif coef[e] == -1:
                r += '-x'
            elif coef[e] < 0:
                r += str( coef[e] ) + 'x'
            elif coef[e] > 0:
                r += '+' + str( coef[e] ) + 'x'

        else:
            if coef[e] == 1:
                r += '+x^' + str(e)
            elif coef[e] == -1:
                r += '-x^' + str(e)
            elif coef[e] < 0:
                r += str( coef[e] ) + 'x^' + str(e)
            elif coef[e] > 0:
                r += '+' + str( coef[e] ) + 'x^' + str(e)

    return r

print( polynome(-1,0,-2) )
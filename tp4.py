from math import factorial, pow
from PyQt4.QtGui import *
from openalea.plantgl.all import *

#Les polynomes de Bernstein
def bernstein(i, n, u):
    coeff = factorial(n) / (factorial(i) * factorial(n-1))
    bern = coeff * pow(u, i) * pow(1-u, n-1)
    return bern

def spline(ptsControle, nbPts = 10):
    nbControle = len(ptsControle)
    degre = nbPts - 1

    ptsCourbe = []

    #Le premier point de la courbe sera le premier point de contrôle
    ptsCourbe.append(ptsControle[0])

    for i in range(1, nbPts - 1):
        pas = float(i) / nbPts
        pt = QVector3D(0,0,0)

        #Calcul de bernstein
        for j in range(0, nbControle):
            point = point + QVector3D(ptsControle[j]) * bernstein(j, degre, pas)


    #Et le dernier point de la courbe sera le dernier point de contrôle
    ptsCourbe.append(ptsControle[len(ptsControle)-1])

    return ptsCourbe

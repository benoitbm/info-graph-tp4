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

def casteljau(i, j, u, ptsControle):
    if (j <= 0):
        return ptsControle;

    pt1 = casteljau(i, j-1, u, ptsControle)
    pt2 = casteljau(i+1, j-1, u, ptsControle)

    return (1-u) * pt1 + u * pt2


def plot_spline_crv(ctrls, pts):
    """
    Parameters
    ==========
      - ctrl: control points
      - pts : evaluated points on the curve
    """
    scene = Scene()
    crv = Shape(geometry=Polyline(pts), appearance=Material((125, 12, 12)))
    scene.add(crv)

    # To complete: Draw the control points and the line between each ones.

    Viewer.display(scene)


def plot_spline_surface(ctrl_net, points):
    """
    Parameters
    ==========
      - ctrl_net : the net of control points (list of list)
      - points : a set of evaluated points (list of list)
    """
    scene = Scene()
    n = len(points)
    m = len(points[0])

    # Compute a mesh (i.e. TriangleSet) for the set of points
    pointList = [pt for rank in points for pt in rank]
    indexList = []

    for i in range(n - 1):
        for j in range(m - 1):
            ii = i * m + j
            i1 = (ii, ii + 1, ii + m)
            i2 = (ii + 1, ii + m + 1, ii + m)
            indexList.append(i1)
            indexList.append(i2)

    surf = Shape(TriangleSet(pointList, indexList), appearance=Material((12, 125, 12)))
    scene.add(surf)

    # plot the control net
    n = len(ctrl_net)
    m = len(ctrl_net[0])
    for pts in ctrl_net:
        crv = Shape(geometry=Polyline(pts), appearance=Material((125, 12, 12)))
        scene.add(crv)
        for pt in pts:
            scene.add(Shape(Translated(Vector3(pt), Sphere(radius=0.1))))

    for i in range(m):
        pts = [ctrl_net[j][i] for j in range(n)]
        crv = Shape(geometry=Polyline(pts), appearance=Material((12, 12, 125)))
        scene.add(crv)

    Viewer.display(scene)

def basis(i, k, u, knots):
    """ i: ith basis
        k: degree
        u : parameter in [u0,u(n+k+1)]
        knots : knot vector
    """
    pass


def knot_vector(k, n, u_min=0., u_max=1.):
    """ Uniform knot vector.
    """
    m = k + n + 2
    knots = [u_min] * (k + 1)
    n_internals = m - 2 * k - 1

    # complete

    assert (len(knots) == m)
    return knots

def main():
    # Lancement de Qt pour avoir OpenAlea
    qapp = QApplication([])

    # Création des points de contôle
    ptsControles = [QVector3D(0, 0, 0), QVector3D(5, 5, 0), QVector3D(10, 5, 0), QVector3D(15, 0, 0)]

    qapp.exec_();



if __name__ == '__main__':
    main()
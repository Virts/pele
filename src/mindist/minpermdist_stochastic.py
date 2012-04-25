import distpot
import numpy as np
import itertools
import rotations as rot
import math
import mindist
import minpermdist
from quench import quench
import basinhopping
import storage.savenlowest as storage

def aa2xyz(XB, AA):
    nsites = len(XB)/3
    XBnew = np.copy(XB)
    rot_mx = rot.aa2mx( AA )
    for j in range(nsites):
        i = 3*j
        XBnew[i:i+3] = np.dot( rot_mx, XBnew[i:i+3] )
    return XBnew

def aa2dist(XA, XB, AA):
    # Rotate XB according to angle axis AA
    XBnew = aa2xyz( XB, AA)
    dist, XAnew, XBnew = minpermdist.findBestPermutation( XA, XBnew)
    return dist




def minPermDistStochastic(X1, X2, niter = 100):
    """
    Minimize the distance between two clusters.  The following symmetries will be accounted for
    
    Translational symmetry

    Global rotational symmetry

    Permutational symmetry

    
    This method uses basin hopping to find the rotation of X2 which best
    optimizes the overlap (an effective energy) between X1 and X2.  The overlap
    is defined to be permutation independent.

    Once the rotation is optimized, the correct permutation can be determined
    deterministically using the Hungarian algorithm.
    """
    X1 = mindist.CoMToOrigin(X1)
    X2 = mindist.CoMToOrigin(X2)
    X2in = np.copy(X2)

    X2min = np.copy(X2)
    dmin = np.linalg.norm( X2-X1 )
    pot = distpot.MinPermDistPotential( X1, X2, 0.2 )
    Eminglobal = pot.globalEnergyMin()
    print "global Emin", Eminglobal

    aamin = np.array([0.,0.,0.])
    Emin = pot.getEnergy(aamin)
    dist = aa2dist( X1, X2in, aamin)
    print "initial minimum,", Emin, dist

    e, v = pot.getEnergyGradient( aamin )
    print e, "gradient", v
    aaq, Eq, rms, funcalls = quench( aamin, pot.getEnergyGradient, tol=1e-6 )
    dist = aa2dist( X1, X2in, aaq)
    print "quenched minimum,", Eq, dist, funcalls

    aamin = aaq
    Emin = Eq

    saveit = storage.SaveN( 20 )
    takestep = distpot.random_rotation
    print "using basin hopping to optimize rotations + permutations"
    bh = basinhopping.BasinHopping( aamin, pot, takestep, storage=saveit.insert)
    for i in range(niter):
        bh.run(1)
        Emin = saveit.data[0][0]
        if abs(Emin-Eminglobal) < 1e-6:
            print "isomer found"
            break

    """
    Lower energies generally mean smaller distances, but it's not guaranteed.
    Check a number of the lowest energy structures. To ensure get the correct
    minimum distance structure.
    """
    print "lowest structures found"
    aamin = saveit.data[0][1]
    dmin = aa2dist( X1, X2in, aamin )
    for (E, aa) in saveit.data:
        dist = aa2dist( X1, X2in, aa)
        print "E", E, dist
        if dist < dmin:
            dmin = dist
            aamin = aa

    X2min = aa2xyz( X2in, aamin )

    return dmin, X1, X2min

def main():
    from potentials.lj import LJ
    lj = LJ()
    natoms = 12
    X1 = np.random.uniform(-1,1,[natoms*3])*(float(natoms))**(1./3)
    ret = quench( X1, lj.getEnergyGradient)
    X1 = ret[0]
    X2 = np.random.uniform(-1,1,[natoms*3])*(float(natoms))**(1./3)
    aa = rot.random_aa()
    rot_mx = rot.aa2mx( aa )
    for j in range(natoms):
        i = 3*j
        X2[i:i+3] = np.dot( rot_mx, X1[i:i+3] )

    #X1 = np.array( [ 0., 0., 0., 1., 0., 0., 0., 0., 1.,] )
    #X2 = np.array( [ 0., 0., 0., 1., 0., 0., 0., 1., 0.,] )
    import copy
    X1i = copy.copy(X1)
    X2i = copy.copy(X2)

    distinit = np.linalg.norm(X1-X2)
    print "distinit", distinit

    (dist, X1, X2) = minPermDistStochastic(X1,X2)
    distfinal = np.linalg.norm(X1-X2)
    print "dist returned    ", dist
    print "dist from coords ", distfinal

    import printing.print_atoms_xyz as printxyz
    with open("out.xyz", "w") as fout:
        mindist.CoMToOrigin(X1i)
        mindist.CoMToOrigin(X2i)
        printxyz.printAtomsXYZ(fout, X1i )
        printxyz.printAtomsXYZ(fout, X2i )
        printxyz.printAtomsXYZ(fout, X1 )
        printxyz.printAtomsXYZ(fout, X2 )

if __name__ == "__main__":
    main()
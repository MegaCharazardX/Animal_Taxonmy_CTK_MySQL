#mag.flux Density B = mew0*(N(no.of turns)I(current)/l(length))

mew0 = 1.25663706e-06 #mkgs**-2a**-2 

def calc_flux_density (N = 100.0, I =10.0, l = 1.0e-03 ) :
    idk1 = (N*I)
    idk2 = idk1/l
    B = mew0*idk2
    return str(B) + " T"


def calc_force (B = 1.2566370599999999, S = 15.0e-06) :
    F = ((B**2)*S)/ 2*mew0
    return str(F) + " N"

print(calc_flux_density(l = 15.0e-03))

print(calc_force(B = 2))
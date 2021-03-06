# Define a class of a Galaxy as blueprint
class Galaxy:
    '''A Galaxy

    === Attributes ===
    ID: the ID number of the galaxy
    z: the redshift of the galaxy
    mass: the log mass of the galaxy, in solar masses
    RA: the Right Ascension of the galaxy (J2000?)
    dec: the declination of the galaxy (J2000?)
    sersic: the sersic number of the galaxy
    fifth: Fifth closest neighbour to key galaxy
    '''

    def __init__(self, ID, z, mass, RA, dec, sersic):
        self.ID_Number = ID
        self.redshift = z
        self.mass = mass
        self.RA = RA
        self.dec = dec
        self.sersic = sersic
        self.fifth = None
        self.neighbours = []

    def __repr__(self):
        return "ID: " + str(self.ID_Number) + ", z: " + str(self.redshift) + ", Mass: " + str(self.mass) + ", RA: " + \
               str(self.RA) + ", dec: " + str(self.dec) + ", sersic: " + str(self.sersic)

    def __eq__(self, other):
        if isinstance(other, Galaxy):
            return self.ID_Number == other.ID_Number
        else:
            return False

    def distance(self, gal):
        return (math.sqrt((((self.RA - gal.RA)*(math.cos(math.radians(self.dec))))**2) + ((self.dec - gal.dec)**2)))*((math.pi)/180)

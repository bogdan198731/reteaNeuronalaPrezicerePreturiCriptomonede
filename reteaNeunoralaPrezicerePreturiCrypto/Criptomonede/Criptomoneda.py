class CriptomonedaC:
    nume = " "
    X = 1
    data = []
    pretO: float = []
    pretH: float = []
    pretL: float = []
    pretC: float = []
    pretAC: float = []
    volum: float = []

    def __init__(self, nume, data,  x, pretO, pretH, pretL, pretC, pretAC, volum):
        self.nume = nume
        self.data = data
        self.pretO = pretO
        self.pretH = pretH
        self.pretL = pretL
        self.pretC = pretC
        self.pretAC = pretAC
        self.volum = volum
        self.x = x

    def returnNume(self):
        return self.nume

    def returnPretO(self):
        return self.pretO

    def returnPretH(self):
        return self.pretH
    def returnPretL(self):
        return self.pretL
    def returnPretC(self):
        return self.pretC
    def returnPretAC(self):
        return self.pretAC
    def returnVolum(self):
        return self.volum

    def arataMoneda(self):
        print("Nume = " + self.nume + " are preturile la deschidere :")
        for el in self.pretO:
            print ("{:0.2f} , ".format(el))
        print(" si la inchidere :")
        for el in self.pretC:
            print ("{:0.2f} , ".format(el))

    def returnMatCripto(self, x, y):
        df = []
        dM = []
        k = 0
        while k < y:
            df.append(self.pretO[x + k])
            df.append(self.pretH[x + k])
            df.append(self.pretL[x + k])
            df.append(self.pretC[x + k])
            df.append(self.pretAC[x + k])
            df.append(self.volum[x + k])
            k = k + 1
            dM.append(df)
            df = []

        return dM
    def retrunNextPret(self, x):
        return self.pretO[x]


class CryptoMoneda:
    def __init__(self, nume, istoric_preturi, istoric_volum, initialize):
        self.nume = nume
        self.istoric_preturi = istoric_preturi
        self.istoric_volum = istoric_volum
        self.initialize = initialize

    def update(self, pret):
        try:
            self.pref = float(pret)
            self.istoric_preturi.append(self.pret)
            self.pretOk = True
        except:
            self.pretOk = False


    def displayTest(self):
        print("crypto " + self.nume+ " are pret " + self.pret + " si istoric ")




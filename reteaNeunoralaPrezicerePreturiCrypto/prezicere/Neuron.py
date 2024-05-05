from Criptomonede import Criptomoneda
import random
import numpy

from Utile.manipulareCSV import scriereCSV


class NeuronC():
    numeCriptomoneda = ""
    greutateC = []
    greutateF = []
    greutateCM = list
    greutateFM = list
    criopto: Criptomoneda = Criptomoneda
    X = 1
    nrScriere = 0
    predictieN = 0

    def __init__(self, x, cripto):
        self.X = x
        gc = []
        gf = []
        gcM = []
        gfM = []
        i = 0
        while i < self.X:
            t = 0
            gc = []
            gf = []
            while t < 6:
                gc.append(random.random()*100)
                gf.append(random.random())
                t = t + 1
            gcM.append(gc)
            gfM.append(gf)
            i = i + 1
        self.greutateC = gc
        self.greutateF = gf
        self.greutateCM = gcM
        self.greutateFM = gfM
        self.criopto = cripto

    def predictie(self, y):
        t = numpy.array(self.criopto.returnMatCripto(y, self.X)).round(5)


        W1 = 3.1  # Open
        W2 = 2.9  # High
        W3 = 2.9  # Low
        W4 = 3.3  # Close
        W5 = 3.2  # Adj Close
        W6 = 2.0  # Volume
        E = 1000
        # print(t)
        for line in t:
            line[0] = line[0] * W1 / E
            line[1] = line[1] * W2 / E
            line[2] = line[2] * W3 / E
            line[3] = line[3] * W4 / E
            line[4] = line[4] * W5 / E
            line[5] = line[5] * W6 / E / 1000


        # print(t)
        # print((numpy.dot(t.T, self.greutateCM)))
        # print(numpy.linalg.det(numpy.dot(t.T, self.greutateCM).round(5)))
        return float(numpy.linalg.det(numpy.dot(t.T, self.greutateCM)))
        # return numpy.sum(numpy.dot(t.T, self.greutateCM))

    def verPreictie(self, y):
        W1 = 3.1  # Open
        W2 = 2.9  # High
        W3 = 2.9  # Low
        W4 = 3.3  # Close
        W5 = 3.2  # Adj Close
        W6 = 2.0  # Volume
        E = 1000
        pred = self.predictie(y)
        self.predictieN = pred
        pretulUrmator = self.criopto.retrunNextPret(y + self.X)
        procenrRecalculare = 20;
        preocentScriere = 1;
        if pred < 0.0000000000:
           pred = self.criopto.returnPretAC()[y + self.X]
        if (pred > pretulUrmator + pretulUrmator / 100 * procenrRecalculare):
            for el in self.greutateCM:
                el[0] = el[0] - (pred - pretulUrmator) / pred/W1
                el[1] = el[1] - (pred - pretulUrmator) / pred/W2
                el[2] = el[2] - (pred - pretulUrmator) / pred/W3
                el[3] = el[3] - (pred - pretulUrmator) / pred/W4
                el[4] = el[4] - (pred - pretulUrmator) / pred/W5
                el[5] = el[5] - (pred - pretulUrmator) / pred/W6
        elif (pred < pretulUrmator - pretulUrmator / 100 * procenrRecalculare):
            for el in self.greutateCM:
                el[0] = el[0] + (pretulUrmator - pred) / pretulUrmator * W1
                el[1] = el[1] + (pretulUrmator - pred) / pretulUrmator * W2
                el[2] = el[2] + (pretulUrmator - pred) / pretulUrmator * W3
                el[3] = el[3] + (pretulUrmator - pred) / pretulUrmator * W4
                el[4] = el[4] + (pretulUrmator - pred) / pretulUrmator * W5
                el[5] = el[5] + (pretulUrmator - pred) / pretulUrmator * W6
        elif(pred < pretulUrmator + pretulUrmator / 100 * preocentScriere and pred > pretulUrmator - pretulUrmator / 100 * preocentScriere):
            # print(" Predictie inainte de scriere in fisier = {:0.10f} , pret real = {:0.2f}".format(pred, pretulUrmator))

            # self.save(self.nrScriere)
            self.nrScriere = self.nrScriere + 1
        if y % 200 == 0:
            print(" Predictie = {:0.10f} , pret real = {:0.2f}".format(pred, pretulUrmator))
            # print(self.greutateCM)

    def startPredictie(self, start, nrDeInregistrariTestate):
        i = start
        while i < nrDeInregistrariTestate:
            self.verPreictie(i)
            i = i + 1

    def save(self, pref):
        nume = "" + str(pref)
        scriereCSV("matricie"  + nume, self.greutateCM)

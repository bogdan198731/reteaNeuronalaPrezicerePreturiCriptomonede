import Criptomonede
from Criptomonede.Criptomoneda import CriptomonedaC
from Utile.manipulareCSV import citireCsvPanda
from Criptomonede import Criptomoneda


def alimentareCripto(numeCripto):
    W1 = 3.1  # Open
    W2 = 2.9  # High
    W3 = 2.9  # Low
    W4 = 3.3  # Close
    W5 = 3.2  # Adj Close
    W6 = 2.0  # Volume
    E = 1000




    sursa = citireCsvPanda("C:/Users/bogda/PycharmProjects/proiectLicenta/ProiectLicenta/csv/BTC-USD.csv")
    k = 0
    pretO = []
    pretH = []
    pretL = []
    pretC = []
    pretAC = []
    volum = []
    data = []
    for pret in sursa.get("Open"):
        pretO.append(pret);
        pretC.append(sursa.get("Close")[k])
        pretH.append(sursa.get("High")[k])
        pretL.append(sursa.get("Low")[k])
        pretAC.append(sursa.get("Adj Close")[k])
        volum.append(sursa.get("Volume")[k])
        data.append(sursa.get("Date")[k])
        k = k + 1
    return CriptomonedaC(numeCripto, data, 7, pretO, pretH, pretL, pretC, pretAC, volum)

# a = alimentareCripto("btc")
# a.arataMoneda()

import random
from Criptomonede import Criptomoneda
import Neuron
from Criptomonede.PopulareCriptomonede import alimentareCripto

X = 15
runda = 0

neuron = Neuron.NeuronC(X, alimentareCripto("btc"))
while runda < 1000:
    neuron.startPredictie(0, len(neuron.criopto.pretO)-X)
    runda = runda + 1
print(neuron.greutateCM)
print(neuron.predictieN)


runda = 1
#neuron.nrGreutatiOk
while runda < neuron.nrGreutatiOk:
    print(neuron.predictieF(len(neuron.criopto.pretO)-X, neuron.greutatiOK[runda]))
    runda = runda + 1
import random
from Criptomonede import Criptomoneda
import Neuron
from Criptomonede.PopulareCriptomonede import alimentareCripto

X = 15
runda = 0

neuron = Neuron.NeuronC(X, alimentareCripto("btc"))
while runda < 1000:
    neuron.startPredictie(0, len(neuron.criopto.pretO)-15)
    runda = runda + 1
print(neuron.greutateCM)
print(neuron.predictieN)
import discretize
from SimPEG import utils
h1 = [(10, 5, -1.3), (5, 20), (10, 3, 1.3)]
M = discretize.TensorMesh([h1, h1], x0='CN')
M.plotGrid(showIt=True)
import numpy as np
import discretize
from SimPEG import maps
import matplotlib.pyplot as plt
M = discretize.TensorMesh([100])
expMap = maps.ExpMap(M)
m = np.zeros(M.nC)
m[M.vectorCCx>0.5] = 1.0
expMap.test(m, plotIt=True)
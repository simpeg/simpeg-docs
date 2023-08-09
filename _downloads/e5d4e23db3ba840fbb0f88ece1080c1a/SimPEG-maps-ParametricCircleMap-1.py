# Here we define the parameterized model for a circle in a wholespace. We then
# create and use a ``ParametricCircleMap`` to map the model to a 2D mesh.
#
from SimPEG.maps import ParametricCircleMap
from discretize import TensorMesh
import numpy as np
import matplotlib.pyplot as plt
#
h = 0.5*np.ones(20)
mesh = TensorMesh([h, h])
#
sigma0, sigma1, x0, y0, R = 0., 10., 4., 6., 2.
model = np.r_[sigma0, sigma1, x0, y0, R]
mapping = ParametricCircleMap(mesh, logSigma=False, slope=2)
#
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
mesh.plot_image(mapping * model, ax=ax)

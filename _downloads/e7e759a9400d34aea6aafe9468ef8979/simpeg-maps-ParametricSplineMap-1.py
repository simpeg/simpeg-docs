# In this example, we define a 2 layered model with a sloping
# interface on a 2D mesh. The model consists of the physical
# property values for the layers and the known elevations
# for the interface at the horizontal positions supplied when
# creating the mapping.
#
from simpeg.maps import ParametricSplineMap
from discretize import TensorMesh
import numpy as np
import matplotlib.pyplot as plt
#
h = 0.5*np.ones(20)
mesh = TensorMesh([h, h])
#
x = np.linspace(0, 10, 6)
y = 0.5*x + 2.5
#
model = np.r_[10., 0., y]
mapping = ParametricSplineMap(mesh, x, order=2, normal='Y', slope=2)
#
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
mesh.plot_image(mapping * model, ax=ax)

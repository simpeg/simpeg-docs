# In this example, we define a layer in a wholespace whose interface is sharp.
# We construct the mapping from the model to the set of active cells
# (i.e. below the surface), We then use an active cells mapping to map from
# the set of active cells to all cells in the mesh.
#
from SimPEG.maps import ParametricLayer, InjectActiveCells
from discretize import TensorMesh
import numpy as np
import matplotlib.pyplot as plt
#
dh = 0.25*np.ones(40)
mesh = TensorMesh([dh, dh])
ind_active = mesh.cell_centers[:, 1] < 8
#
sig0, sig1, zL, h = 5., 10., 4., 2
model = np.r_[sig0, sig1, zL, h]
#
layer_map = ParametricLayer(
    mesh, indActive=ind_active, slope=4
)
act_map = InjectActiveCells(mesh, ind_active, 0.)
#
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
mesh.plot_image(act_map * layer_map * model, ax=ax)

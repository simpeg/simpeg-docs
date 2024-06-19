# In this example, we define a rectangular block in a wholespace whose
# interface is sharp. We construct the mapping from the model to the
# set of active cells (i.e. below the surface), We then use an active
# cells mapping to map from the set of active cells to all cells in the mesh.
#
from SimPEG.maps import ParametricBlock, InjectActiveCells
from discretize import TensorMesh
import numpy as np
import matplotlib.pyplot as plt
#
dh = 0.5*np.ones(20)
mesh = TensorMesh([dh, dh])
ind_active = mesh.cell_centers[:, 1] < 8
#
sig0, sigb, xb, Lx, yb, Ly = 5., 10., 5., 4., 4., 2.
model = np.r_[sig0, sigb, xb, Lx, yb, Ly]
#
block_map = ParametricBlock(mesh, indActive=ind_active)
act_map = InjectActiveCells(mesh, ind_active, 0.)
#
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
mesh.plot_image(act_map * block_map * model, ax=ax)

# In this example, we define a 2 layer model whose interface is sharp and lies
# along a polynomial function :math:`y(x)=c_0 + c_1 x`. In this case, the model is
# defined as :math:`\mathbf{m} = [\sigma_1 , \sigma_2 , c_0 , c_1]`. We construct
# a polynomial mapping from the model to the set of active cells (i.e. below the surface),
# We then use an active cells mapping to map from the set of active cells to all
# cells in the 2D mesh.
#
from SimPEG.maps import ParametricPolyMap, InjectActiveCells
from discretize import TensorMesh
import numpy as np
import matplotlib.pyplot as plt
#
h = 0.5*np.ones(20)
mesh = TensorMesh([h, h])
ind_active = mesh.cell_centers[:, 1] < 8
sig1, sig2, c0, c1 = 10., 5., 2., 0.5
model = np.r_[sig1, sig2, c0, c1]
#
poly_map = ParametricPolyMap(
    mesh, order=1, logSigma=False, normal='Y', actInd=ind_active, slope=1e4
)
act_map = InjectActiveCells(mesh, ind_active, 0.)
#
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
mesh.plot_image(act_map * poly_map * model, ax=ax)
ax.set_title('Mapping on a 2D mesh')
#
# Here, we recreate the previous example on a 3D mesh but with a smoother interface.
# For a 3D mesh, the 2D polynomial defining the sloping interface is given by
# :math:`z(x,y) = c_0 + c_x x + c_y y + c_{xy} xy`. In this case, the model is
# defined as :math:`\mathbf{m} = [\sigma_1 , \sigma_2 , c_0 , c_x, c_y, c_{xy}]`.
#
mesh = TensorMesh([h, h, h])
ind_active = mesh.cell_centers[:, 2] < 8
sig1, sig2, c0, cx, cy, cxy = 10., 5., 2., 0.5, 0., 0.
model = np.r_[sig1, sig2, c0, cx, cy, cxy]
poly_map = ParametricPolyMap(
    mesh, order=[1, 1], logSigma=False, normal='Z', actInd=ind_active, slope=2
)
act_map = InjectActiveCells(mesh, ind_active, 0.)
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
mesh.plot_slice(act_map * poly_map * model, ax=ax, normal='Y', ind=10)
ax.set_title('Mapping on a 3D mesh')

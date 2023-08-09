# Here we project a 3 layered Earth model defined on a 2D tensor mesh
# to a 3D tensor mesh. We assume that at for some y-location, we
# have a 2D tensor model which defines the physical property distribution
# as a function of the *x* and *z* location. Using ``Surject2Dto3D``,
# we project the model along the y-axis to obtain a 3D distribution
# for the physical property (i.e. a 3D tensor model).
#
from SimPEG.maps import Surject2Dto3D
from discretize import TensorMesh
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#
dh = np.ones(20)
mesh2D = TensorMesh([dh, dh], 'CC')
mesh3D = TensorMesh([dh, dh, dh], 'CCC')
#
# Here, we define the 2D tensor model.
#
m = np.zeros(mesh2D.nC)
m[mesh2D.cell_centers[:, 1] < 0] = 10.
m[mesh2D.cell_centers[:, 1] < -5] = 5.
#
# We then plot the 2D tensor model; which is defined along the
# x and z axes.
#
fig1 = plt.figure(figsize=(6, 5))
ax11 = fig1.add_axes([0.1, 0.15, 0.7, 0.8])
mesh2D.plot_image(m, ax=ax11, grid=True)
ax11.set_ylabel('z')
ax11.set_title('2D Tensor Model')
ax12 = fig1.add_axes([0.83, 0.15, 0.05, 0.8])
norm1 = mpl.colors.Normalize(vmin=np.min(m), vmax=np.max(m))
cbar1 = mpl.colorbar.ColorbarBase(ax12, norm=norm1, orientation="vertical")
#
# By setting *normal = 'Y'* we are projecting along the y-axis.
#
mapping = Surject2Dto3D(mesh3D, normal='Y')
u = mapping * m
#
# Finally we plot a slice of the resulting 3D tensor model.
#
fig2 = plt.figure(figsize=(6, 5))
ax21 = fig2.add_axes([0.1, 0.15, 0.7, 0.8])
mesh3D.plot_slice(u, ax=ax21, ind=10, normal='Y', grid=True)
ax21.set_ylabel('z')
ax21.set_title('Projected to 3D Mesh (y=0)')
ax22 = fig2.add_axes([0.83, 0.15, 0.05, 0.8])
norm2 = mpl.colors.Normalize(vmin=np.min(m), vmax=np.max(m))
cbar2 = mpl.colorbar.ColorbarBase(ax22, norm=norm2, orientation="vertical")

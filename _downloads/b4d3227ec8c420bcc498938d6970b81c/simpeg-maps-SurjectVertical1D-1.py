# Here we define a 1D layered Earth model comprised of 3 layers
# on a 1D tensor mesh. We then use ``SurjectVertical1D`` to
# construct a mapping which projects the 1D model onto a 2D
# tensor mesh.
#
from simpeg.maps import SurjectVertical1D
from simpeg.utils import plot_1d_layer_model
from discretize import TensorMesh
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#
dh = np.ones(20)
mesh1D = TensorMesh([dh], 'C')
mesh2D = TensorMesh([dh, dh], 'CC')
#
m = np.zeros(mesh1D.nC)
m[mesh1D.cell_centers < 0] = 10.
m[mesh1D.cell_centers < -5] = 5.
#
fig1 = plt.figure(figsize=(5,5))
ax1 = fig1.add_subplot(111)
plot_1d_layer_model(
    mesh1D.h[0], np.flip(m), ax=ax1, z0=0,
    scale='linear', show_layers=True, plot_elevation=True
)
ax1.set_xlim([-0.1, 11])
ax1.set_title('1D Model')
#
mapping = SurjectVertical1D(mesh2D)
u = mapping * m
#
fig2 = plt.figure(figsize=(6, 5))
ax2a = fig2.add_axes([0.1, 0.15, 0.7, 0.8])
mesh2D.plot_image(u, ax=ax2a, grid=True)
ax2a.set_title('Projected to 2D Mesh')
ax2b = fig2.add_axes([0.83, 0.15, 0.05, 0.8])
norm = mpl.colors.Normalize(vmin=np.min(m), vmax=np.max(m))
cbar = mpl.colorbar.ColorbarBase(ax2b, norm=norm, orientation="vertical")

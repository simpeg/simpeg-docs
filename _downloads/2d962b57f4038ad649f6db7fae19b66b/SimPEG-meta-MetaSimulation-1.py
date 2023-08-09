# Create a list of 1D simulations that perform a piece of a
# stitched problem.
#
from SimPEG.simulation import ExponentialSinusoidSimulation
from SimPEG import maps
from SimPEG.meta import MetaSimulation
from discretize import TensorMesh
import matplotlib.pyplot as plt
#
# Create a mesh for space and time, then one that represents
# the full dimensionality of the model.
mesh_space = TensorMesh([100])
mesh_time = TensorMesh([5])
full_mesh = TensorMesh([5, 100])
#
# Lets say we have observations at 5 locations in time. For simplicity
# we will just use the same times from the time mesh, but this is not
# required. Then create a simulation for each of these times. We also
# create an operator that maps the model in full space to the model for
# each simulation.
obs_times = mesh_time.cell_centers_x
sims, mappings = [], []
for time in obs_times:
    sims.append(ExponentialSinusoidSimulation(
        mesh=mesh_space,
        model_map=maps.IdentityMap(),
    ))
    ccs = mesh_space.cell_centers
    p_ave = full_mesh.get_interpolation_matrix(
        np.c_[np.full_like(ccs, time), ccs]
    )
    mappings.append(maps.LinearMap(p_ave))
sim = MetaSimulation(sims, mappings)
#
# This simulation acts like a single simulation, which can be used for modeling
# and inversion. This model is a moving box car.
true_model = np.zeros(full_mesh.shape_cells)
speed, start, width = 0.8, 0.1, 0.2
for i, time in enumerate(mesh_time.cell_centers):
    center = speed * time  + start
    in_box = np.abs(mesh_space.cell_centers - center) <= width/2
    true_model[i, in_box] = 1.0
true_model = true_model.reshape(-1, order='F')
#
# Then use the simulation to create data.
d_pred = sim.dpred(true_model)
plt.plot(d_pred.reshape(5, -1).T)
plt.show()

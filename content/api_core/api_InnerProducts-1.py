import numpy as np
import discretize
mesh = discretize.TensorMesh([10,50,3])
m1 = np.random.rand(mesh.nC)
m2 = np.random.rand(mesh.nC,3)
m3 = np.random.rand(mesh.nC,6)
M = list(range(3))
M[0] = mesh.getFaceInnerProduct(m1)
M[1] = mesh.getFaceInnerProduct(m2)
M[2] = mesh.getFaceInnerProduct(m3)
plt.figure(figsize=(13,5))
for i, lab in enumerate(['Isotropic','Anisotropic','Tensor']):
    plt.subplot(131 + i)
    plt.spy(M[i],ms=0.5,color='k')
    plt.tick_params(axis='both',which='both',labeltop='off',labelleft='off')
    plt.title(lab + ' Material Property')
plt.show()
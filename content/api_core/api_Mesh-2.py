import discretize
import numpy as np
import matplotlib.pyplot as plt
hx = np.r_[3,2,1,1,1,1,2,3]
hy = np.r_[3,1,1,3]
M = discretize.TensorMesh([hx, hy])
M.plotGrid(faces=True, nodes=True)
plt.title('Cell faces in the x- and y-directions.')
plt.legend(('Nodes', 'X-Faces', 'Y-Faces'))
plt.show()
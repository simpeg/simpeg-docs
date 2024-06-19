import matplotlib.pyplot as plt
from SimPEG.utils.model_builder import create_random_model
m = create_random_model((50,50), bounds=[-4,0])
plt.colorbar(plt.imshow(m))
plt.title('A very cool, yet completely random model.')
plt.show()

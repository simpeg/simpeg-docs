import matplotlib.pyplot as plt
import SimPEG.utils.model_builder as MB
plt.colorbar(plt.imshow(MB.randomModel((50,50),bounds=[-4,0])))
plt.title('A very cool, yet completely random model.')
plt.show()
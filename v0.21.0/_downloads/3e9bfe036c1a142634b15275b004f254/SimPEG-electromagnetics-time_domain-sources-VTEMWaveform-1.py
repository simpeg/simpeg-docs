import matplotlib.pyplot as plt
import numpy as np
from SimPEG.electromagnetics import time_domain as tdem
#
times = np.linspace(0, 1e-2, 1000)
waveform = tdem.sources.VTEMWaveform()
plt.plot(times, [waveform.eval(t) for t in times])
plt.show()

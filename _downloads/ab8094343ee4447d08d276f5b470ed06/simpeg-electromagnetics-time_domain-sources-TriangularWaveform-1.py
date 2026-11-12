import matplotlib.pyplot as plt
import numpy as np
from simpeg.electromagnetics import time_domain as tdem
#
times = np.linspace(0, 1e-2, 1000)
waveform = tdem.sources.TriangularWaveform(start_time=1E-3, off_time=6e-3, peak_time=3e-3)
plt.plot(times, [waveform.eval(t) for t in times])
plt.show()

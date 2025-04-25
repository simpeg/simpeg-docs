import matplotlib.pyplot as plt
import numpy as np
from simpeg.electromagnetics import time_domain as tdem
#
times = np.linspace(0, 1e-4, 1000)
waveform = tdem.sources.RampOffWaveform(off_time=1e-5)
plt.plot(times, [waveform.eval(t) for t in times])
plt.show()

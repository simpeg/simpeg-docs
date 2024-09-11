import matplotlib.pyplot as plt
import numpy as np
from simpeg.electromagnetics import time_domain as tdem
#
times = np.linspace(0, 1e-2, 1000)
waveform = tdem.sources.QuarterSineRampOnWaveform(ramp_on=(0, 2e-3), ramp_off=(3e-3, 3.5e-3))
plt.plot(times, [waveform.eval(t) for t in times])
plt.show()

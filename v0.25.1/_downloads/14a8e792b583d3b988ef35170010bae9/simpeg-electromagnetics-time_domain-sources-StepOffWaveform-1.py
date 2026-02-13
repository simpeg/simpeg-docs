# The default off-time for the step-off waveform is 0s. In the example below, we set it to
# 1e-5 s (0.01 ms) to illustrate it in a plot
#
import matplotlib.pyplot as plt
import numpy as np
from simpeg.electromagnetics import time_domain as tdem
#
times = np.linspace(0, 1e-4, 1000)
waveform = tdem.sources.StepOffWaveform(off_time=1e-5)
plt.plot(times, [waveform.eval(t) for t in times])
plt.show()

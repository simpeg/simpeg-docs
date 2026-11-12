# In this example, we define a saw-tooth waveform
#
import matplotlib.pyplot as plt
import numpy as np
from simpeg.electromagnetics import time_domain as tdem
#
def my_waveform(t):
    period = 1e-2
    quarter_period = period / 4
    t_cycle = np.mod(t, period)
    if t_cycle <= quarter_period:
        return t_cycle / quarter_period
    elif (t_cycle > quarter_period) & (t_cycle <= 3*quarter_period):
        return -t_cycle / quarter_period + 2
    elif t_cycle > 3*quarter_period:
        return t_cycle / quarter_period - 4
#
times = np.linspace(0, 1e-2, 1000)
waveform = tdem.sources.RawWaveform(waveform_function=my_waveform)
plt.plot(times, [waveform.eval(t) for t in times])
plt.show()

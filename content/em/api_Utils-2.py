import numpy as np
from SimPEG import electromagnetics as EM
import matplotlib.pyplot as plt
from scipy.constants import mu_0
freqs = np.logspace(-2, 5, 301)
Bx, By, Bz = EM.analytics.FDEM.MagneticDipoleWholeSpace(
        [0, 100, 0], [0, 0, 0], 1e-2, freqs, moment='Z')
plt.figure()
plt.loglog(freqs, Bz.real/mu_0, 'C0', label='Real')
plt.loglog(freqs, -Bz.real/mu_0, 'C0--')
plt.loglog(freqs, Bz.imag/mu_0, 'C1', label='Imaginary')
plt.loglog(freqs, -Bz.imag/mu_0, 'C1--')
plt.legend()
plt.xlim([1e-2, 1e5])
plt.ylim([1e-13, 1e-6])
plt.show()
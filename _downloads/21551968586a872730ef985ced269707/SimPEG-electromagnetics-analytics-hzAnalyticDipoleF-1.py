import matplotlib.pyplot as plt
from SimPEG import electromagnetics as em
freq = np.logspace(-1, 5, 301)
test = em.analytics.hzAnalyticDipoleF(
       100, freq, 0.01, secondary=False)
plt.loglog(freq, test.real, 'C0-', label='Real')
plt.loglog(freq, -test.real, 'C0--')
plt.loglog(freq, test.imag, 'C1-', label='Imaginary')
plt.loglog(freq, -test.imag, 'C1--')
plt.title('Response at $r=100$ m')
plt.xlim([1e-1, 1e5])
plt.ylim([1e-12, 1e-6])
plt.xlabel('Frequency (Hz)')
plt.ylabel('$H_z$ (A/m)')
plt.legend(loc=6)
plt.show()
#
# **Reference**
#
# - Ward, S. H., and G. W. Hohmann, 1988, Electromagnetic theory for
#   geophysical applications, Chapter 4 of Electromagnetic Methods in Applied
#   Geophysics: SEG, Investigations in Geophysics No. 3, 130--311; DOI:
#   `10.1190/1.9781560802631.ch4

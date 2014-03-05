# Plot the filter's frequency response, showing the flat group delay and
# the relationship to the Butterworth's cutoff frequency:

from scipy import signal
import matplotlib.pyplot as plt

b, a = signal.butter(4, 100, 'low', analog=True)
w, h = signal.freqs(b, a)
plt.plot(w, 20 * np.log10(np.abs(h)), color='silver', ls='dashed')
b, a = signal.bessel(4, 100, 'low', analog=True)
w, h = signal.freqs(b, a)
plt.plot(w, 20 * np.log10(np.abs(h)))
plt.xscale('log')
plt.title('Bessel filter frequency response (with Butterworth)')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green') # cutoff frequency
plt.show()

plt.figure()
plt.plot(w[1:], -np.diff(np.unwrap(np.angle(h)))/np.diff(w))
plt.xscale('log')
plt.title('Bessel filter group delay')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Group delay [seconds]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.show()

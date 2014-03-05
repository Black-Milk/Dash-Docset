# We want to construct a filter with a passband at 0.2-0.4 Hz, and
# stop bands at 0-0.1 Hz and 0.45-0.5 Hz. Note that this means that the
# behavior in the frequency ranges between those bands is unspecified and
# may overshoot.

from scipy import signal
bpass = signal.remez(72, [0, 0.1, 0.2, 0.4, 0.45, 0.5], [0, 1, 0])
freq, response = signal.freqz(bpass)
ampl = np.abs(response)

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.semilogy(freq/(2*np.pi), ampl, 'b-')  # freq in Hz
plt.show()

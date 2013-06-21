# Plot real component, imaginary component, and envelope for a 5 Hz pulse,
# sampled at 100 Hz for 2 seconds:

from scipy import signal
import matplotlib.pyplot as plt
t = np.linspace(-1, 1, 2 * 100, endpoint=False)
i, q, e = signal.gausspulse(t, fc=5, retquad=True, retenv=True)
plt.plot(t, i, t, q, t, e, '--')

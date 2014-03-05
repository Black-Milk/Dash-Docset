from scipy import signal
import matplotlib.pyplot as plt

# Generate a test signal, a 2 Vrms sine wave at 1234 Hz, corrupted by
# 0.001 V**2/Hz of white noise sampled at 10 kHz.

fs = 10e3
N = 1e5
amp = 2*np.sqrt(2)
freq = 1234.0
noise_power = 0.001 * fs / 2
time = np.arange(N) / fs
x = amp*np.sin(2*np.pi*freq*time)
x += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)

# Compute and plot the power spectral density.

f, Pxx_den = signal.welch(x, fs, 1024)
plt.semilogy(f, Pxx_den)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()

# If we average the last half of the spectral density, to exclude the
# peak, we can recover the noise power on the signal.

np.mean(Pxx_den[256:])
# 0.0009924865443739191

# Now compute and plot the power spectrum.

f, Pxx_spec = signal.welch(x, fs, 'flattop', 1024, scaling='spectrum')
plt.figure()
plt.semilogy(f, np.sqrt(Pxx_spec))
plt.xlabel('frequency [Hz]')
plt.ylabel('Linear spectrum [V RMS]')
plt.show()

# The peak height in the power spectrum is an estimate of the RMS amplitude.

np.sqrt(Pxx_spec.max())
# 2.0077340678640727

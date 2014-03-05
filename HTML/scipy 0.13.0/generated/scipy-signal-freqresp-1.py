# # Generating the Nyquist plot of a transfer function

from scipy import signal
import matplotlib.pyplot as plt

s1 = signal.lti([], [1, 1, 1], [5])
# # transfer function: H(s) = 5 / (s-1)^3

w, H = signal.freqresp(s1)

plt.figure()
plt.plot(H.real, H.imag, "b")
plt.plot(H.real, -H.imag, "r")
plt.show()

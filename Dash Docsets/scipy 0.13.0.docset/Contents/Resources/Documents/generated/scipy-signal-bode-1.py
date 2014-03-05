from scipy import signal
import matplotlib.pyplot as plt

s1 = signal.lti([1], [1, 1])
w, mag, phase = signal.bode(s1)

plt.figure()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.figure()
plt.semilogx(w, phase)  # Bode phase plot
plt.show()

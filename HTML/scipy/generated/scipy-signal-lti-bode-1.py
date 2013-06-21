from scipy import signal
import matplotlib.pyplot as plt

s1 = signal.lti([1], [1, 1])
w, mag, phase = s1.bode()

plt.figure()
plt.semilogx(w, mag)    # bode magnitude plot
plt.figure()
plt.semilogx(w, phase)  # bode phase plot
plt.show()

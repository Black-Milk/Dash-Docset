from scipy import signal
import matplotlib.pyplot as plt

points = 100
a = 4.0
vec2 = signal.ricker(points, a)
print(len(vec2))
# 100
plt.plot(vec2)
plt.show()

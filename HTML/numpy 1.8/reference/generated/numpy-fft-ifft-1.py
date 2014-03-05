np.fft.ifft([0, 4, 0, 0])
# array([ 1.+0.j,  0.+1.j, -1.+0.j,  0.-1.j])

# Create and plot a band-limited signal with random phases:

import matplotlib.pyplot as plt
t = np.arange(400)
n = np.zeros((400,), dtype=complex)
n[40:60] = np.exp(1j*np.random.uniform(0, 2*np.pi, (20,)))
s = np.fft.ifft(n)
plt.plot(t, s.real, 'b-', t, s.imag, 'r--')
# [<matplotlib.lines.Line2D object at 0x...>, <matplotlib.lines.Line2D object at 0x...>]
plt.legend(('real', 'imaginary'))
# <matplotlib.legend.Legend object at 0x...>
plt.show()

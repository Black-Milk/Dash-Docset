# Draw samples from the distribution:

mu, kappa = 0.0, 4.0 # mean and dispersion
s = np.random.vonmises(mu, kappa, 1000)

# Display the histogram of the samples, along with
# the probability density function:

import matplotlib.pyplot as plt
import scipy.special as sps
count, bins, ignored = plt.hist(s, 50, normed=True)
x = np.arange(-np.pi, np.pi, 2*np.pi/50.)
y = -np.exp(kappa*np.cos(x-mu))/(2*np.pi*sps.jn(0,kappa))
plt.plot(x, y/max(y), linewidth=2, color='r')
plt.show()

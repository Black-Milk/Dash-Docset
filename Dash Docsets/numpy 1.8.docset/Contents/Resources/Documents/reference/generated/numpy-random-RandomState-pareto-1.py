# Draw samples from the distribution:

a, m = 3., 1. # shape and mode
s = np.random.pareto(a, 1000) + m

# Display the histogram of the samples, along with
# the probability density function:

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 100, normed=True, align='center')
fit = a*m**a/bins**(a+1)
plt.plot(bins, max(count)*fit/max(fit),linewidth=2, color='r')
plt.show()

# Draw samples from the distribution:

import numpy as np
s = np.random.poisson(5, 10000)

# Display histogram of the sample:

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 14, normed=True)
plt.show()

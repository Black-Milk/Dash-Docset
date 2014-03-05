# Custom made discrete distribution:

import matplotlib.pyplot as plt
from scipy import stats
xk = np.arange(7)
pk = (0.1, 0.2, 0.3, 0.1, 0.1, 0.1, 0.1)
custm = stats.rv_discrete(name='custm', values=(xk, pk))
h = plt.plot(xk, custm.pmf(xk))

# Random number generation:

R = custm.rvs(size=100)

# Display frozen pmf:

numargs = generic.numargs
[ <shape(s)> ] = ['Replace with resonable value', ]*numargs
rv = generic(<shape(s)>)
x = np.arange(0, np.min(rv.dist.b, 3)+1)
h = plt.plot(x, rv.pmf(x))

# Here, ``rv.dist.b`` is the right endpoint of the support of ``rv.dist``.

# Check accuracy of cdf and ppf:

prb = generic.cdf(x, <shape(s)>)
h = plt.semilogy(np.abs(x-generic.ppf(prb, <shape(s)>))+1e-20)

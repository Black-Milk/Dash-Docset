import scipy.misc
lena = scipy.misc.lena()
lena.shape
# (512, 512)
lena.max()
# 245
lena.dtype
# dtype('int32')

import matplotlib.pyplot as plt
plt.gray()
plt.imshow(lena)
plt.show()

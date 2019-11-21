import statmechtools as stm
import numpy as np


# print("printing help")
# help(stm)
# help(stm.convolve2d)

# a = np.linspace(0, 1, 20)

# print("checking for 1d array-------------------------------------")
# print (a.shape)
# c = stm.convolve1d(a, 1)
# print (c)

# print("checking for 2d array-------------------------------------")
# a = a.reshape((a.shape[0], 1))
# print (a.shape)
# print(a)
# c = stm.convolve2d(a, 1)
# print (c)
# y = np.linspace(0, 10, 1000000)
# y1 = stm.convolve1d_fast(y, 1, 1e-6)


print("testing a file")
import matplotlib.pyplot as plt

filename = "./data/sq_lattice_site_percolation_periodic__entropy_order_L100_avg.txt"
x, y = np.loadtxt(filename, usecols=(0,1), unpack=True)
# plt.plot(x, y, label='old')


# y1 = stm.convolve1d(y, 4)
y1 = stm.convolve1d_fast(y, 1, 1e-3)
# plt.plot(x, y1, label='new')
# plt.ylim(0, 13)
# plt.legend()
# plt.show()

C = -(1-x[1:]) * np.diff(y) / np.diff(x)
plt.plot(x[1:], C)

C = -(1-x[1:]) * np.diff(y1) / np.diff(x)
plt.plot(x[1:], C)
plt.show()
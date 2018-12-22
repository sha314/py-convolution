import statmechtools as stm
import numpy as np


# print("printing help")
# help(stm)
# help(stm.convolve2d)

a = np.linspace(0, 1, 20)

print("checking for 1d array-------------------------------------")
print (a.shape)
c = stm.convolve1d(a, 1)
print (c)

print("checking for 2d array-------------------------------------")
a = a.reshape((a.shape[0], 1))
print (a.shape)
print(a)
c = stm.convolve2d(a, 1)
print (c)



# print("testing a file")
# import matplotlib.pyplot as plt

# filename = "sq_lattice_site_percolation_periodic_entropy_avg_std-L_200.csv"
# x, y = np.loadtxt(filename, usecols=(0,1), unpack=True)
# plt.plot(x, y, label='old')

# y1 = stm.convolve1d(y, 3)
# plt.plot(x, y1, label='new')
# plt.ylim(0, 13)
# plt.legend()
# plt.show()

# C = -(1-x[1:]) * np.diff(y1) / np.diff(x)
# plt.plot(x[1:], C)
# plt.show()
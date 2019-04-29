import time
import numpy as np
from scipy import stats as stats

I = 100
J = 100

# J x I matrix of random numbers
data = [stats.expon.rvs(size=I, loc=0, scale=17) for j in range(J)]

# way 1 - from NumPy - better with wider
time_np = time.time()
means1 = [np.mean(data[j]) for j in range(J)]
time_np = time.time() - time_np

# way 2 - manually
time_man = time.time()
means2 = [sum(data[j])/I for j in range(J)]
time_man = time.time() - time_man

# way 3 - dot product - better with longer
# However 'dot' has better performance because we calculate v only once.
time_dot = time.time()
v = [1/I for i in range(I)]
means3 = np.dot(data, v)
time_dot = time.time() - time_dot

# print times
print('np.mean(): ', time_np*1000, ' [ms]')
# print('manual: ', time_man*1000, ' [ms]')
print('np.dot(): ', time_dot*1000, ' [ms]')

# checking errors
error12 = max([abs(means1[j]-means2[j]) for j in range(J)])
error23 = max([abs(means3[j]-means2[j]) for j in range(J)])
error31 = max([abs(means3[j]-means1[j]) for j in range(J)])
print(error12, error23, error31)

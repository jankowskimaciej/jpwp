import time
from scipy import stats as stats

S = 10**5
N = 30
lam = 0.7
Z = 0

time_gamma = time.time()
g = stats.gamma.rvs(size=S, loc=Z, a=N, scale=lam)
time_gamma = time.time() - time_gamma

time_exp = time.time()
exp = [sum(stats.expon.rvs(size=N, loc=Z, scale=lam) for i in range(S))]
time_exp = time.time() - time_exp

print('Single Gamma: ', time_gamma*1000, ' [ms]')
print('Multiple exponentials: ', time_exp*1000, ' [ms]')
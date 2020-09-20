import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sts
from statsmodels.distributions.empirical_distribution import ECDF

df = 27
chi2_rv = sts.chi2(df)
sample = chi2_rv.rvs(1000)
x = np.linspace(0, 100, 100)
cdf = chi2_rv.cdf(x)
pdf = chi2_rv.pdf(x)
###############################
plt.plot(x, pdf, label='theoretical PDF')
plt.hist(sample, density=True)
###############################
rvs5 = chi2_rv.rvs(size=[1000, 5])
rvs10 = chi2_rv.rvs(size=[1000, 10])
rvs50 = chi2_rv.rvs(size=[1000, 50])
###############################
mean5 = [np.mean(z) for z in rvs5]
mean10 = [np.mean(z) for z in rvs10]
mean50 = [np.mean(z) for z in rvs50]
###############################
M = df
D = 2 * df
###############################
norm_rv = sts.norm(M, np.sqrt(D / 5))
pdf = norm_rv.pdf(x)
plt.plot(x, pdf, label='theoretical PDF (n=5)')
plt.hist(mean5, density=True)
###############################
#norm_rv = sts.norm(M, np.sqrt(D / 10))
#pdf = norm_rv.pdf(x)
#plt.plot(x, pdf, label='theoretical PDF (n=10)')
#plt.hist(mean10, density=True)
###############################
norm_rv = sts.norm(M, np.sqrt(D / 50))
pdf = norm_rv.pdf(x)
plt.plot(x, pdf, label='theoretical PDF (n=50)')
plt.hist(mean50, density=True)
###############################
plt.ylabel('$f(x)$')
plt.xlabel('$x$')
plt.legend(loc='upper right')
plt.show()
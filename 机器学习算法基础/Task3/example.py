import numpy as np
from scipy.stats import norm
from math import sqrt
# generating data
# mixture unvariate normal
# phi*N(0,1) + (1-phi)*N(4,1)
_phi = 1/2
_mu1 = 0
_mu2 = 4
_s1 = _s2 = 1
N = 300
data = []
np.random.seed(100)
for _ in range(N):
    u = np.random.random()
    if u < _phi:
        data.append(np.random.randn()*_s1 + _mu1)
    else:
        data.append(np.random.randn()*_s2 + _mu2)

data = np.array(data)
# EM Alg
niter = 500
# initial value
phi = 1/3
mu1 = 0.5
mu2 = 1
s1 = s2 = 0.5
for _ in range(niter):

    # E-step
    # wv = (w1,w2,...,wn), wi is weight for N(mu1, s1**2)
    wv = phi  * norm.pdf(data, mu1, s1) / (phi * norm.pdf(data, mu1, s1) + (1-phi) * norm.pdf(data, mu2, s2))
    # M-step
    # update parameter
    mu1 = sum(wv*data) / sum(wv)
    mu2 = sum((1-wv)*data) / sum(1-wv)
    s1 =  sqrt(sum(wv*(data-mu1)**2) / sum(wv))
    s2 =  sqrt(sum((1-wv)*(data-mu2)**2) / sum(1-wv))
    phi = sum(wv) / len(wv)
print("true parameter:{:.2f},{:.2f},{:.2f},{:.2f},{:.2f}".format(_phi, _mu1, _mu2, _s1, _s2))
print("estimated parameter:{:.2f},{:.2f},{:.2f},{:.2f},{:.2f}".format(phi, mu1, mu2, s1, s2))
    


from math import gcd
from sympy.ntheory import factorint
import numpy as np
import gc

factorint_vec = np.vectorize(factorint)
factor_ary = factorint_vec(np.arange(0, 100000))
factor_cum_dict = {}.copy()
factor_cum_ary = factor_cum_ary = np.repeat(None, len(factor_ary))
factor_cum_ary[0] = factor_cum_dict
for i in range(1, len(factor_ary)):
    factor_new_set = factor_ary[i].keys() - factor_cum_dict.keys()
    for item in factor_new_set:
        factor_cum_dict[item] = 0
    
    for item in factor_ary[i]:
        factor_cum_dict[item] += factor_ary[i][item]
    factor_cum_ary[i] = factor_cum_dict.copy()

def cum_prod(m, factor_ary = factor_ary, factor_cum_ary = factor_cum_ary):
    n_prod = 1
    for item in factor_ary[m]:
        n_prod *= pow(item, factor_cum_ary[m][item])
    return n_prod

def proceed(g_m, m, k, mod_n):
    g_m_next_mult = (g_m*m + pow(g_m, k, mod_n)) % mod_n
    n_gcd = gcd(mod_n, m + 1)
    mod_n_next = mod_n//n_gcd
    if g_m_next_mult % n_gcd == 0:
        g_m_next = (pow((m + 1)//n_gcd, -1, mod_n_next)*(g_m_next_mult//n_gcd)) % mod_n_next
        return (g_m_next, mod_n_next)
    # else:
        # print("Warning: proceed(): non-integer value for m =", m + 1)

for k in range(800000, 900000):
    # put the code below in for_loop of m_max
    m_max = 1
    while m_max < len(factor_ary):
        m_max += 1
        g_1 = 2  # (1 + 1^2)/1
        m = 1
        g_m_state = (g_1, cum_prod(m_max))  # second arg should be determined according to m_max
        while m < m_max:
            g_m_state = proceed(g_m_state[0], m, k, g_m_state[1])
            # print(m + 1, g_m_state)
            m += 1
        if g_m_state is None:
            print("%d,%d" % (k, m), flush = True)
            # print("non-integer value m =", m, "for k =", k)
            break


# g_m_next_mult = (g_m_state[0]*m + pow(g_m_state[0], k, g_m_state[1])) % g_m_state[1]

_ = '''
k = 2
# p, n is set according to factor_cum_ary for each factor in m
p, n = 2, 3  # a specific prime factor and the multiplicity for the 4th term

g_0 = 1
m = 1
g_m = 1

g_m_next_mult = g_m*(g_m + m)
mod_dict = [m + 1]
if gcd(m + 1, p) == 1:
    pow(g_m_next_mult, -1, p)
else:
    if g_m_next_mult % (p**factor_ary[m + 1][p]):
        pow(g_0, -1, p)
    else:
        # non-integer error
'''

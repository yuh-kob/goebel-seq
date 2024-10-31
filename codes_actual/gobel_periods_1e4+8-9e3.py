from math import gcd
from sympy.ntheory.generate import primerange
import numpy as np
import gc

def proceed(g_m, m, k, mod_n):
    g_m_next_mult = (g_m*m + pow(g_m, k, mod_n)) % mod_n
    n_gcd = gcd(mod_n, m + 1)
    mod_n_next = mod_n//n_gcd
    if g_m_next_mult % n_gcd == 0:
        g_m_next = (pow((m + 1)//n_gcd, -1, mod_n_next)*(g_m_next_mult//n_gcd)) % mod_n_next
        return (g_m_next, mod_n_next)
    # else:
        # print("Warning: proceed(): non-integer value for m =", m + 1)

for p in primerange(18000, 19000):
    for k in range(2, p + 1):
        # put the code below in for_loop of m_max
        m_max = p
        g_1 = 2  # (1 + 1^2)/1
        m = 1
        g_m_state = (g_1, p)  # second arg should be determined according to m_max
        while m < m_max:
            g_m_state = proceed(g_m_state[0], m, k, g_m_state[1])
            # print(m + 1, g_m_state)
            m += 1
        if g_m_state is None:
            print("%d,%d,%d" % (m, m - 1, k % (m - 1)), flush = True)
            # print("non-integer value m =", m, "for k =", k)
            # break
        # else:
            # print("Pass for k = ", k)

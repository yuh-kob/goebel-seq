from math import gcd
from sympy.ntheory.generate import primerange
import numpy as np
import pickle
import gc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys

def proceed(g_m, m, k, mod_n):
    g_m_next_mult = (g_m*m + pow(g_m, k, mod_n)) % mod_n
    n_gcd = gcd(mod_n, m + 1)
    mod_n_next = mod_n//n_gcd
    if g_m_next_mult % n_gcd == 0:
        g_m_next = (pow((m + 1)//n_gcd, -1, mod_n_next)*(g_m_next_mult//n_gcd)) % mod_n_next
        return (g_m_next, mod_n_next)

def proceed_p(g_m, m, k, mod_n):
    g_m_next_mult = (g_m*m + pow(g_m, k, mod_n)) % mod_n
    g_m_next = (pow((m + 1), -1, mod_n)*(g_m_next_mult)) % mod_n
    return (g_m_next, mod_n)

def comp_proceed_all(k_, l_, p_):
    m_max = p_
    g_1 = l_  # (1 + 1^2)/1
    m = 1
    g_m_state = (g_1, p_)  # second arg should be determined according to m_max
    while m < m_max - 1:
        g_m_state = proceed_p(g_m_state[0], m, k_, g_m_state[1])
        # print(m + 1, g_m_state)
        # res_vec_ary[l, m] = g_m_state[0]
        m += 1
    g_m_state = proceed(g_m_state[0], m, k_, g_m_state[1])
    if g_m_state is None:
        # print("%d,%d,%d" % (m, m - 1, k % (m - 1)), flush = True)
        # print("non-integer value m =", m, "for k =", k)
        res = 0  # Modified at latest
    else:
        # print("Pass for k =", k)
        res = 1  # Modified at latest
    return res

def l_thres_binsearch_p(p):
    k = (p - 1)//2
    l_back = 0
    l_fore = 2
    cont_flag = (comp_proceed_all(k, l_fore, p) == 1)
    break_flag = False
    while cont_flag:
        l_fore *= 2
        cont_flag = (comp_proceed_all(k, l_fore, p) == 1)
        if l_fore > p:
            break_flag = True
            break
    if break_flag:
        print("Error at l_thres_binsearch_p(%d): l_thres not determined" % p, file = sys.stderr, flush = True)
        return (None, None)
    while True:
        l_mid = (l_back + l_fore)//2
        l_mid -= 1 if (l_mid % 2 ==1) else 0
        if comp_proceed_all(k, l_mid, p) == 1:
            l_back = l_mid
        else:
            l_fore = l_mid
        if l_fore - l_back == 2:
            break
    if comp_proceed_all(k, l_back, p) != 1 or comp_proceed_all(k, l_fore, p) != 0:
        print("Error at p = %d: non-matching l_back and l_fore" % p, file = sys.stderr)
    return (l_back, l_fore)

def l_thres_binsearch_m(p):
    k = (p - 1)//2
    l_back = p - 1
    l_fore = p - 3
    cont_flag = (comp_proceed_all(k, l_fore, p) == 1)
    break_flag = False
    while cont_flag:
        l_fore = p - (p - l_fore + 1)*2 - 1
        cont_flag = (comp_proceed_all(k, l_fore, p) == 1)
        if l_fore < 0:
            break_flag = True
            break
    if break_flag:
        print("Error at l_thres_binsearch_m(%d): l_thres not determined" % p, file = sys.stderr, flush = True)
        return (None, None)
    while True:
        l_mid = (l_back + l_fore)//2
        l_mid -= 1 if (l_mid % 2 ==1) else 0
        if comp_proceed_all(k, l_mid, p) == 1:
            l_back = l_mid
        else:
            l_fore = l_mid
        if l_back - l_fore == 2:
            break
    if comp_proceed_all(k, l_back, p) != 1 or comp_proceed_all(k, l_fore, p) != 0:
        print("Error at p = %d: non-matching l_back and l_fore" % p, file = sys.stderr, flush = True)
    return (l_back, l_fore)

integrality_dict = {}
file_index_str = "15e4-18e4"
for p in primerange(150000, 180000):
    if p % 4 == 1:
        print("---- Set p =", p, "----", file = sys.stderr, flush = True)
        integrality_dict[p] = l_thres_binsearch_p(p) + tuple(reversed(l_thres_binsearch_m(p)))
    
    with open('k-l-gobel-mid_prime-integrality-binsrc_%s.pkl' % file_index_str, 'wb') as handle:
        pickle.dump(integrality_dict, handle, protocol = pickle.HIGHEST_PROTOCOL)


# with open("k-l-gobel-mid_prime-integrality-binsrc_3e3-1e5.pkl", "rb")) as handle:
#    pd.DataFrame.from_dict(pickle.load(handle, orient = "index")


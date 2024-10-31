from math import gcd
from sympy.ntheory.generate import primerange
import numpy as np
import pickle
import gc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

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


# pdf = PdfPages('k-l-gobel_prime-integrality_1e3-15e2.pdf')
integrality_list = []

for p in primerange(1000, 1500):
    print("-------- Set p =", p, "--------", flush = True)
    res_mat_ary = np.zeros((p - 1, p), dtype = int) - 1
    for k in range(2, p + 2):
      for l in range(0, p):
        m_max = p
        g_1 = l  # (1 + 1^2)/1
        m = 1
        g_m_state = (g_1, p)  # second arg should be determined according to m_max
        while m < m_max - 1:
            g_m_state = proceed_p(g_m_state[0], m, k, g_m_state[1])
            # print(m + 1, g_m_state)
            # res_mat_ary[l, m] = g_m_state[0]
            m += 1
        g_m_state = proceed(g_m_state[0], m, k, g_m_state[1])
        if g_m_state is None:
            # print("%d,%d,%d" % (m, m - 1, k % (m - 1)), flush = True)
            # print("non-integer value m =", m, "for k =", k)
            res_mat_ary[k % (p - 1), l] = 0  # Modified at latest
            # break
        else:
            # print("Pass for k =", k)
            res_mat_ary[k % (p - 1), l] = 1  # Modified at latest
    # print(res_mat_ary)
    integrality_list.append(res_mat_ary)
    
    fig, ax = plt.subplots()
    ax.imshow(res_mat_ary)
    ax.set_title("p = %d" % p)
    # ax.spines['top'].set_visible(False)
    # ax.spines['left'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    # ax.spines['right'].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    # plt.show()
    # pdf.savefig()
    plt.close()
    with open('k-l-gobel_prime-integrality_1e3-15e2.pkl', 'wb') as handle:
        pickle.dump(integrality_list, handle, protocol = pickle.HIGHEST_PROTOCOL)

# pdf.close()


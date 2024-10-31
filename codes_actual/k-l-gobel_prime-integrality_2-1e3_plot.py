from math import gcd
from sympy.ntheory.generate import primerange
import numpy as np
import pickle
import gc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

with open('k-l-gobel_prime-integrality_2-1e3.pkl', 'rb') as handle:
    integrality_list = pickle.load(handle)

cnt = 0
pdf = PdfPages('k-l-gobel_prime-integrality_2-1e3_full.pdf')
for p in primerange(2, 1000):
    fig, ax = plt.subplots()
    tmp_bool_ary = np.ones(integrality_list[cnt].shape[0], dtype = bool)
    tmp_bool_ary[1] = False
    ax.pcolormesh(integrality_list[cnt][tmp_bool_ary, :],
        cmap = 'viridis' if integrality_list[cnt][tmp_bool_ary, :].sum() < integrality_list[cnt][tmp_bool_ary, :].size else 'viridis_r')
    ax.set_title("p = %d" % p)
    spines_width = 0.5
    ax.spines['top'].set_linewidth(spines_width)
    ax.spines['left'].set_linewidth(spines_width)
    ax.spines['bottom'].set_linewidth(spines_width)
    ax.spines['right'].set_linewidth(spines_width)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    ax.invert_yaxis()
    # plt.show()
    pdf.savefig()
    plt.close()
    cnt += 1

pdf.close()


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
pdf = PdfPages('k-l-gobel_prime-integrality_2-1e3_full-img.pdf')
for p in primerange(2, 1000):
    print("Plotting p =", p, flush = True)
    fig, ax = plt.subplots()
    tmp_bool_ary = np.ones(integrality_list[cnt].shape[0], dtype = bool)
    tmp_bool_ary[1] = False
    rotate_ary = np.concatenate([[tmp_bool_ary.size - 2], np.arange(0, tmp_bool_ary.size - 2, dtype = int)])
    ax.imshow(integrality_list[cnt][tmp_bool_ary, :][rotate_ary, :],
            cmap = 'viridis' if integrality_list[cnt][tmp_bool_ary, :].sum() < integrality_list[cnt][tmp_bool_ary, :].size else 'viridis_r')
    ax.set_title("p = %d" % p)
    spines_width = 0.25
    ax.spines['top'].set_linewidth(spines_width)
    ax.spines['left'].set_linewidth(spines_width)
    ax.spines['bottom'].set_linewidth(spines_width)
    ax.spines['right'].set_linewidth(spines_width)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    # plt.show()
    pdf.savefig(dpi = (integrality_list[cnt].shape[0] - 1)*2.7056)
    plt.close()
    cnt += 1

pdf.close()


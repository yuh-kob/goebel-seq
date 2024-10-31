from math import gcd
from sympy.ntheory.generate import primerange
import numpy as np
import pickle
import gc
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.colors import LinearSegmentedColormap

# if 'Helvetica' in matplotlib.rcParams['font.sans-serif']:
#     matplotlib.rcParams['font.sans-serif'].remove('Helvetica')
#     matplotlib.rcParams['font.sans-serif'] = ['Helvetica'] + matplotlib.rcParams['font.sans-serif']

# plt.rcParams['font.family'] = 'Arial'
plt.rc('font', family = 'serif', size = 24)
plt.rcParams['figure.titlesize'] = 20
matplotlib.rc('text', usetex = True)

colors = [(0, 0, 1, 1), (1, 1, 1, 0)]
cmap_bw = LinearSegmentedColormap.from_list("BlueWhite", colors, N = 2)

with open('k-l-gobel_prime-integrality_2-1e3_patched.pkl', 'rb') as handle:
    integrality_list = pickle.load(handle)

cnt = 0
pdf = PdfPages('k-l-gobel_prime-integrality_pub-1.pdf')
for p in primerange(1, 200):
    fig, ax = plt.subplots()
    ax.pcolormesh(integrality_list[cnt],
        cmap = 'Greys_r' if integrality_list[cnt].sum() < integrality_list[cnt].size else 'Greys')
    if p % 4 == 1:
        tmp_dat_ary = integrality_list[cnt].copy()
        tmp_dat_ary[0:(p - 1)//2, :] = 1
        tmp_dat_ary[((p - 1)//2 + 1):, :] = 1
        ax.pcolormesh(tmp_dat_ary, cmap = cmap_bw)

    ax.set_title(r'$p = %d \equiv %d\:\,(\textrm{mod}\:{4})$' % (p, p % 4))
    spines_width = 0.5
    ax.spines['top'].set_linewidth(spines_width)
    ax.spines['left'].set_linewidth(spines_width)
    ax.spines['bottom'].set_linewidth(spines_width)
    ax.spines['right'].set_linewidth(spines_width)
    ax.tick_params(width = 0.5)
    ax.set_xticks(np.arange(0, p, 50, dtype = float) + 0.5, np.arange(0, p, 50, dtype = int))
    ax.set_yticks(np.arange(0, p - 1, 50, dtype = float) + 0.5, np.arange(0, p - 1, 50, dtype = int))
    ax.set_aspect('equal')
    ax.invert_yaxis()
    ax.set_xlabel('$l$')
    ax.set_ylabel('$k$', rotation = 0)
    # plt.show()
    pdf.savefig(bbox_inches = 'tight')
    plt.close()
    cnt += 1

pdf.close()


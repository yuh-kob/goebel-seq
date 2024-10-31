import torch
import numpy as np
import datetime
import sys

print("[%s]" % datetime.datetime.now(), "Loading PERIODS file ...", file = sys.stderr)
filepath_str = "/work/kobayashi/gobel/gobel_periods_2-15e3.dat"
acc_ary = np.loadtxt(filepath_str, delimiter = ",", dtype = int)
print("[%s]" % datetime.datetime.now(), "Loaded PERIODS file \"%s\"" % filepath_str, file = sys.stderr)

def exclude_with_offset(n_len, excl_ary, offset = 0):
    unacc_cuda_ary = torch.ones(n_len, dtype = bool, device = 'cuda')
    # cnt = 0
    for item_ary in excl_ary:
        offset_mod = (item_ary[2] + item_ary[1] - (offset % item_ary[1])) % item_ary[1]
        unacc_cuda_ary[offset_mod::item_ary[1]] = False
        # if cnt % 10000 == 0:
            # print("Issued cnt =", cnt, flush = True)
        # cnt += 1
    res_tns = torch.tensor([], dtype = int)
    for i in range(0, n_len//(10**9), 2):
        tmp_tns = torch.where(unacc_cuda_ary[i*(10**9):(i+2)*(10**9)])[0].cpu() + i*(10**9) + offset
        res_tns = torch.concat([res_tns, tmp_tns])
    return res_tns

for i in range(0, 1000):
    print("[%s]" % datetime.datetime.now(), "Started batch num. i =", i, file = sys.stderr)
    unacc_tns = exclude_with_offset(10**10, acc_ary, offset = i*(10**10))
    if len(unacc_tns) > 0:
        print('\n'.join(list(map(lambda x: "%d" % x, unacc_tns))), flush = True)
    print("[%s]" % datetime.datetime.now(), "Finished batch num. i = %d, #(unaccounted):" % i, len(unacc_tns), file = sys.stderr)


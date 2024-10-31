import sys
import math
from sympy import sieve

def reflect(l_, p_):
    return l_ if (l_*2 < p_) else (p_ - l_)

# Note: Applicable for even number 2 <= l < p - 1
def find_sign_seq_2(l_, p):
    l = l_ if (l_*2 < p) else (p - (l_ + 2))
    cond_dict = {i: [] for i in range(1, p//2 + 1)}
    cond_dict_pair = {}
    n_thres = min([l, p - (l + 2)])
    former_list_1 = [(reflect(l - i, p), reflect(l + 2 + i, p), -1) for i in range(0, n_thres)]
    former_list_2 = [(reflect(l + 2 + i, p), reflect(l - i, p), -1) for i in range(0, n_thres)]
    n_init = l + 2 + (n_thres - 1) + 2
    latter_list_1 = [(reflect(1 + i, p), reflect(n_init + i, p), +1) for i in range(0, (p - n_init)//2)]
    latter_list_2 = [(reflect(n_init + i, p), reflect(1 + i, p), +1) for i in range(0, (p - n_init)//2)]
    for item in former_list_1 + former_list_2 + latter_list_1 + latter_list_2:
        cond_dict[item[0]].append((item[1], item[2]))
        cond_dict_pair.update({(item[0], item[1]): item[2]})
    
    sign_dict_tmp = {}
    n_pivot = reflect(l + 1, p)
    n_pivot_back = -1
    sign_dict_tmp[n_pivot] = 1  # Temporary
    while True:
        n_forward_list = [item[0] for item in cond_dict[n_pivot]]
        while n_pivot_back in n_forward_list:
            n_forward_list.remove(n_pivot_back)
        
        if len(n_forward_list) > 0:
            n_forward = n_forward_list[0]
            sign_dict_tmp[n_forward] = sign_dict_tmp[n_pivot]*cond_dict_pair[(n_pivot, n_forward)]
        else:
            break
        
        n_pivot_back = n_pivot
        n_pivot = n_forward
    
    sign_adjust = sign_dict_tmp[1]
    sign_list = [sign_dict_tmp[i]*sign_adjust for i in range(1, p//2 + 1)]
    return sign_list

for p in sieve.primerange(10000, 15000):
    if (p % 4) == 1:
        for l in range(2, p - 1, 2):
            seq_manual = find_sign_seq_2(l, p)
            # seq_manual += seq_manual[::-1]
            # seq_manual_part_sq = [seq_manual[q*q - 1] for q in range(1, math.isqrt(p - 2) + 1)]
            # if (-1) in seq_manual_part_sq:
            #     first_minus_pos = seq_manual_part_sq.index(-1) + 1
            # else:
            #     first_minus_pos = ""
            print(p, l, ''.join(map(lambda x: "+" if x > 0 else "-" if x < 0 else "0", seq_manual)), sep = ",", flush = True)

        print(flush = True)

import numpy as np
import scipy.sparse
import scipy.sparse.linalg
import itertools
import sys

def match_array(a_ary, b_ary):
	if np.sum(a_ary.size != b_ary.size):
		return None
	
	if np.sum(a_ary != b_ary) == 0:
		return True
	else:
		return False

def reflect_val(x, l): # l even
	x_ = x % (l + 1)
	return (x_, +1) if (x_ <= l//2) else ((l + 1) - x_, -1)

sign_chr = lambda x: '+' if x > 0 else '-' if x < 0 else '0'

for l in range(500, 10000, 2):
	# c: a_0
	gcd_ary = np.gcd(l + 1, 2*np.arange(0, l + 1, dtype = int) + 1)
	a_axis_ary = np.where(gcd_ary == 1)[0]
	for a_axis in a_axis_ary:
		row_ary = np.zeros(l + 1, dtype = np.int32)
		col_ary = np.zeros(l + 1, dtype = np.int32)
		dat_ary = np.zeros(l + 1, dtype = np.int8)
		
		for i in range(0, l//2):
			back_dat = reflect_val(a_axis - i, l)
			fore_dat = reflect_val(a_axis + 1 + i, l)
			row_ary[2*i + 0] = i
			col_ary[2*i + 0] = back_dat[0]
			dat_ary[2*i + 0] = back_dat[1]
			row_ary[2*i + 1] = i
			col_ary[2*i + 1] = fore_dat[0]
			dat_ary[2*i + 1] = -fore_dat[1]
		
		row_ary[l] = l//2
		col_ary[l] = 1
		dat_ary[l] = 1
		
		x_mat_coo = scipy.sparse.coo_matrix((dat_ary, (row_ary, col_ary)), shape = (l//2 + 1, l//2 + 1))
		x_mat_csr = x_mat_coo.tocsr()
		# x_mat_coo.toarray()
		
		b_ary = np.zeros(l//2 + 1, dtype = np.int8)
		b_ary[l//2] = 1
		
		sol_ary = scipy.sparse.linalg.spsolve(x_mat_csr, b_ary)
		sol_ary = np.sign(sol_ary).astype(np.int8)
		
		if not match_array(x_mat_csr @ sol_ary, b_ary):
			print("Error: x_mat_csr @ sol_ary does not match b_ary at l = %d, a_axis = %d" % (l, a_axis), file = sys.stderr, flush = True)
		
		cyclic_ary = np.concatenate([sol_ary, -sol_ary[:0:-1], sol_ary])
		n_iter_max = max(len(list(y)) for (c,y) in itertools.groupby(cyclic_ary))
		
		print(l, ("%%%dd" % len("%d" % np.max(a_axis_ary))) % a_axis, sep = ',', end = ',')
		print(("%%%dd" % len("%d" % (l//2 + 1))) % (n_iter_max - 1), end = ',')
		print(sign_chr(sol_ary[0]), '|', sep = '', end = '')
		print(''.join(map(sign_chr, sol_ary[1:])), end = '|')
		print(''.join(map(sign_chr, -sol_ary[:0:-1])), flush = True)
	
	print()



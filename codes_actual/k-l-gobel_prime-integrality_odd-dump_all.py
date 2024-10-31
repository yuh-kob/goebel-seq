import numpy as np
import pickle

sep_str = ","
file_str_list = ["2-1e3_patched", "1e3-15e2", "15e2-18e2", "18e2-20e2", "20e2-22e2", "22e2-24e2", "24e2-26e2", "26e2-28e2", "28e2-30e2"]

integ_list = []
for file_str in file_str_list:
    with open("k-l-gobel_prime-integrality_%s.pkl" % file_str, "rb") as fin:
    	integ_list += pickle.load(fin)

for integ_ary in integ_list:
	if integ_ary.shape[1] % 4 == 1:
		focus_ary = integ_ary[(integ_ary.shape[1] - 1)//2,:]
		if (focus_ary == 0).sum() + (focus_ary == 1).sum() == focus_ary.size:
			focus_noninteg_ary = np.where(focus_ary == 0)[0]
			if focus_noninteg_ary.size > 0:
				focus_noninteg_sim_ary = np.arange(focus_noninteg_ary.min(), focus_noninteg_ary.max() + 1, 2)
			else:
				focus_noninteg_sim_ary = np.array([], dtype = int)
			if focus_noninteg_ary.size == focus_noninteg_sim_ary.size:
				if (focus_noninteg_ary != focus_noninteg_sim_ary).sum() == 0:
					print(integ_ary.shape[1], end = sep_str)
					if focus_noninteg_ary.size > 0:
						f_min = focus_noninteg_ary.min()
						f_max = focus_noninteg_ary.max()
						print(f_min, f_max, (f_max - f_min)//2 + 1, f_min + f_max - integ_ary.shape[1], sep = sep_str)
					else:
						print("-", "-", "-", "-", sep = sep_str)
		focus_str = ','.join(list(map(lambda x: "%d" % x, focus_ary.tolist())))
		# print(focus_str)



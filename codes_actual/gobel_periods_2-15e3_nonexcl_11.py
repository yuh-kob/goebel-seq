import numpy as np

periods_ary = np.loadtxt("gobel_periods_2-15e3.dat", delimiter = ",", dtype = int)

_ = '''
bool_ary = np.repeat(True, 10**9)
cnt = 0
for period_ary in periods_ary:
	bool_ary[period_ary[2]::period_ary[1]] = False
	cnt += 1
	if cnt % 1000 == 0:
		print("Finished cnt =", cnt, flush = True)

np.savetxt("gobel_periods_2-15e3_nonexcl-1e9.dat", np.where(bool_ary)[0], fmt = "%d")
'''

unbounded_list = []
for i in range(700, 800):
	bool_ary = np.repeat(True, 10**9)
	offset = i*(10**9)
	cnt = 0
	for period_ary in periods_ary:
		offset_mod = (period_ary[2] + period_ary[1] - (offset % period_ary[1])) % period_ary[1]
		bool_ary[offset_mod::period_ary[1]] = False
		cnt += 1
		if cnt % 1000 == 0:
			print("Finished cnt =", cnt, flush = True)
	unbounded_ary = np.where(bool_ary)[0] + offset
	unbounded_list.append(unbounded_ary)

np.savetxt("gobel_periods_2-15e3_nonexcl-7-8e11.dat", np.concatenate(unbounded_list), fmt = "%d")


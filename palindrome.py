import sys
import matplotlib.pyplot as plt

num_iter = 0
start_num = 0
sums = []
num_iters = []
ex = []

sys.setrecursionlimit(1000)

def reverse(num):
	num = str(num)
	new_str = ""
	for index in range(len(num)-1, -1, -1):
		new_str = new_str+num[index]
	return (new_str)

def get_sum(num):
	num = str(num)
	s = 0
	for idex in range(len(num)-1):
		s += int(num[idex])

	return s

def get_new_check(num):
	global num_iter, start_num, sums, num_iter
	# print num
	if str(num) == reverse(num):
		print 'Num: ', start_num, ' Palindrome: ', str(num), ' Iter: ', num_iter
		sums.append(get_sum(start_num))
		num_iters.append(num_iter)
		ex.append(start_num*reverse(start_num))
		return 
	else:
		num_iter += 1
		get_new_check(num + int(reverse(num)))

for i in range(int(sys.argv[1])):
	start_num = i
	try:
		get_new_check(i)
	except:
		pass

plt.figure(1)
print len(sums), len(num_iters)
plt.hist2d(ex, num_iters, bins=sums)
plt.colorbar()
plt.show()
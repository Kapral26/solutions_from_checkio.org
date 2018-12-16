def long_repeat(line):
	max_i = 0
	last = 0
	# print(len(line))
	for i in range(0, len(line)):
		# print(max_i)
		if i == 0:
			max_i += 1
			continue
		if line[i] != line[i-1] or i == len(line)-1:
			print(max_i, last)
			if max_i > last:
				last=max_i
			max_i = 1
			continue
		max_i += 1
	
	return last

print(long_repeat("abababa"))

# print(long_repeat('sdsffffse'))
# # print(long_repeat('ddvvrwwwrggg'))
# # print(long_repeat("abababaab"))
print(long_repeat("aa"))


def modulo11(bnum):
	"""
	the function takes int (bank number) with len from 1 - 10 and return True or False
	if a total sum after multiplication of every character with weight is divisible by 11
	"""
	weight = [6, 3, 7, 9, 10, 5, 8, 4, 2, 1]
	#add additional zeroes until len(full_bnum) == 10
	full_bnum = (len(weight)-len(str(bnum))) * "0" + str(bnum)
	total = 0
	for n in range(len(scales)):
		total += scales[n] * int(fullbnum[n])
	return total % 11 == 0

# function to check if two stings are palindromes (webscraping NEB for enzymes)
# step 1 determine the reverse_compliment of a sequence string Martin Schweitzer PyCon Australia 2016
# step 2 join original string with new string
# step 3 check if palindrome

def sticky_finder(dna):

	from functools import reduce
	import operator
	
	DNA = []
	test_seq = []
	sticky = []
	b = ['A', 'T', 'C', 'G']
	complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
	d = ''
	
	for e in dna:
		for i in e:
			if i not in b:
				break
			elif i in b:
				d += i
	if len(d) == len(dna)-1:
		DNA.append(d)
	
	for e in DNA:
		rev = ''.join(complement.get(base, base) for base in reversed(e))
		test_seq.append(rev)
		for i in test_seq:
			if i == e:
				return e

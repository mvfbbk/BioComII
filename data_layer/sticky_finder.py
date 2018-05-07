"""
Programme:  Sticky Finder
File:       sticky_finder.py

Version:    Alpha_1.0
Date:       2018-03-28
Function:   A function for determining the palindromic nature of short DNA
            sequences

Copyright:  (c) Matthieu Vizuete-Forster, BBK, 2018
Author:     Matthieu Vizuete-Forster
Address:    Department of Biological Sciences
            Malet Steet, London, WC1E 7HX

--------------------------------------------------------------------------

released under GPL v3.0 licence

--------------------------------------------------------------------------
Description:
============
this is a requried function for the NEB Scraper to work correctly
--------------------------------------------------------------------------
Usage:
======
This file needs to be in the same directory as the NEB Scraper so that it 
can be used.

--------------------------------------------------------------------------
Revision History:
=================
A_0.1   23.03.18   Alpha   By: MVF
"""

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
		

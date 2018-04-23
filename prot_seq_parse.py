"""
Programme:  ProtSeqParser
File:       prot_seq_parse.py

Version:    Alpha_1.0
Date:       2018-03-14
Function:   Obtain Protein sequence from one or more GenBank records

Copyright:  (c) Matthieu Vizuete-Forster, BBK, 2018
Author:     Matthieu Vizuete-Forster
Address:    Department of Biological Sciences
            Malet Steet, London, WC1E 7HX

--------------------------------------------------------------------------

Copyright not yet assigned

--------------------------------------------------------------------------
Description:
============
Module for extracting Protein sequence data from a GenBank file. The 
module will allow the extraction of the first protein sequence entry
within the GenBank entry by use of the moreThanOneEntry function and the 
unique sequence using the singleEntry function

--------------------------------------------------------------------------
Usage:
======
Module requires the name of the file to be processed as an input file.
This information can be supplied within a configuration file.

--------------------------------------------------------------------------
Revision History:
=================
A_0.1   14.03.18   Alpha   By: MVF
A_0.2   23.04.18   Alpha   By: MVF  Comment: A_0.1 did not return a 
                                            functional dictionary when 
                                            applied to input file. function
                                            correted to allow all sequences 
                                            to be extracted from the source
"""


import os
import glob
import re
import gzip

def prot_seq_parse(file):

    rx_sequence = re.compile(r'\/translation="(\w+)"')
    prot_seq = {}
        n = 0
    
    for f in file:
        with gzip.open(path.format(f), 'rt') as d:
            data = d.read().replace("\n", "")
            data = data.replace(" ","")
            s = data.split('LOCUS//')

    for i in s:
        n += 1
        for match in rx_sequence.finditer(i):
            seq = match.group(1)
            prot_seq[seq] = n
    
    return prot_seq
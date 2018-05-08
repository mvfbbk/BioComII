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

---------------------------------------------------------------------------

released under GPL v3.0 licence

---------------------------------------------------------------------------
Description:
"""


import os
import glob
import re
import gzip

path = os.getcwd() + '/{}'
file = glob.glob("*.gz")



    
def prot_seq_parse(data):
    
    d = data.read().replace("\n", "")
    d = d.replace(" ","")
    s = d.split('//')

    rx_sequence = re.compile(r'\/translation="(\w+)"')
    prot_seq = {}

    n = 0

    for i in s:
        n += 1
        for match in rx_sequence.finditer(i):
            seq = match.group(1)
            prot_seq[n] = seq
    return prot_seq

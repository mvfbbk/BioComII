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

import os
import glob
import re
import gzip

path =  os.getcwd() + "/{}"
file_list = glob.glob('*.gz')

rx_sequence = re.compile(r'\/translation="(\w+)"')
prot_seq = {}
n = 0
    
for f in file_list:
    with gzip.open(path.format(f), 'rt') as d:
        data = d.read().replace("\n", "")
        data = data.replace(" ","")
        s = data.split('//L')

for i in s:
    n += 1
    for match in rx_sequence.finditer(i):
        seq = match.group(1)
        prot_seq[n] = seq
    
with open(path.format('prot.csv'), 'w') as outfile:
    for k, v in prot_seq.items():
        outfile.write(str(k))
        outfile.write(';')
        outfile.write(v)
        outfile.write('\n')
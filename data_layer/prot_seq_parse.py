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
============
Module for extracting Protein sequence data from one or more GenBank files.
The module will allow the extraction of the first protein sequence entry
within the GenBank entry by use of the moreThanOneEntry function and the 
unique sequence using the singleEntry function

---------------------------------------------------------------------------
Usage:
======
Module requires a list of files to be processed. This list can be 
generated automatically from the main script and passed to the function.
By saving the files to be processed in the working directory these can be
parsed automatically in the event that updates are required.

---------------------------------------------------------------------------
Revision History:
=================
A_0.1   14.03.18   Alpha   By: MVF
A_0.2   23.04.18   Alpha   By: MVF      Comment: A_0.1 did not return a 
                                            functional dictionary when 
                                            applied to input file. function
                                            correted to allow all sequences 
                                            to be extracted from the source
A0.3    23.04.18    Alpha   By: MVF     Comment: Make function executable
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

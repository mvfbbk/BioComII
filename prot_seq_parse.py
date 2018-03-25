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
"""


import os
import re

rx_sequence=re.compile(r"\/translation=\"((\w+)(?:\W+\w+)+)\"\nO")
rx_sequence_1=re.compile(r"\/translation=\"((\w+)(?:\W+\w+)+)\"\n\s+g")
rx_blank=re.compile(r"\W")

sequence = {}

def singeEntry(data):
    for match in rx_sequence_1.finditer(data):
        seq = match.group(1)
        seq = rx_blank.sub("", seq)
        n = 0
        if len(seq) > 0:
            n +=1
            sequence[n] = seq
    return sequence

def moreThanOneEntry(data):
    for match in rx_sequence_1.finditer(data):
        seq = match.group(1)
        seq = rx_blank.sub("", seq)
        n = 0
        if len(seq) > 0:
            n +=1
            sequence[n] = seq
    
    for match in rx_sequence.finditer(data):
        seq = match.group(1)
        seq = rx_blank.sub("", seq)
        n = 0
        if len(seq) > 0:
            n += 1
            sequence[n] = seq
    return sequence 
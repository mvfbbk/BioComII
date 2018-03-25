"""
Programme:  DNAseqParse
File:       dna_seq_parse.py

Version:    Alpha0.1
Date:       2018-03-08
Function:   Obtain DNA sequence information from one or more GenBank records

Copyright:  (c) Matthieu Vizuete-Forster, BBK, 2018
Author:     Matthieu Vizuete-Forster
Address:    Department of Biological Sciences
            Malet Steet, London, WC1E 7HX
            
--------------------------------------------------------------------------

Copyright not yet assigned

--------------------------------------------------------------------------
Description:
============
This file will strip out the DNA sequence data from the GenBank records
called in the main programme. The data will be returned in a dictionary
with an entry per record. This dictionary will be used to update the SQL
Database

--------------------------------------------------------------------------
Usage:
======
Module requires the name of the file to be processed as an input file.
This information can be supplied within a configuration file.

--------------------------------------------------------------------------
Revision History:
=================
A0.1   01.03.18   Alpha   By: MVF
"""

#*************************************************************************
# Import libraries

def dnaSeqParse(data):
    
    import re
    start = "ORIGIN"
    end = "//\n"
    sequence = ''

    file = data #open('AB003151_1.txt')
    started =  False

    for line in file:
        if end in line:
            started = False
        if started:
            sequence += line.strip()
        if start in line:
            started = True
        sequence = re.sub('[\W|\d]' , '', sequence)
    file.close()
    return sequence
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
<<<<<<< HEAD
Module requires a list of files to be processed. This list can be 
generated automatically from the main script and passed to the function.
By saving the files to be processed in the working directory these can be
parsed automatically in the event that updates are required.
=======
Module requires the name of the file to be processed as an input file.
This information can be supplied within a configuration file.
>>>>>>> 28412ee8e04c049a6d0256f17e31c3dd80536d33

--------------------------------------------------------------------------
Revision History:
=================
<<<<<<< HEAD
A0.1    01.03.18    Alpha   By: MVF
A0.2    07.04.18    Alpha   By: MVF     Comment: using glob and gzip 
                                                modules to support 
                                                ingestion of compressed
                                                data files
A0.3    12.04.18    Alpha   By: MVF     Comment: A0.2 version returned
                                                poorly formated dictionary
                                                update changed string 
                                                formatting order to allow
                                                dictionnary entries to be
                                                valid
A0.4    23.04.18    Alpha   By: MVF     Comment: Corrected input for the
                                                function and updated usage
                                                information
A0.5    23.04.18    Alpha   By: MVF     Comment: Make function executable
"""

import os
import glob
import re
import gzip

path = os.getcwd() + "/{}"
file = glob.glob('*.gz')

# above is not needed in the main script as the 'data' varable will be the 
# files opened in the main script, kept here for testing

def dna_seq_parse(file):
    start = "ORIGIN"
    end = "//\n"
    sequence = {}
    n = 0
    started = False

    for f in file:
        with gzip.open(path.format(f), 'rt') as d:
            data = d.readlines()
            s = ''
            for line in data:
                if end in line:
                    started = False
                if start in line:
                    started = True
                if started:
                    line = re.sub('[\W|\d]', '', line)
                    s += line.strip()
            S = s.split(sep='ORIGIN')
    for i in S:
        if len(i) >= 1:
            n += 1
            sequence[n] = i
    return sequence
=======
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
>>>>>>> 28412ee8e04c049a6d0256f17e31c3dd80536d33

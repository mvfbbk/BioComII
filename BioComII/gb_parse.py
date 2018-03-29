"""
Programme:  GeneBankParser
File:       gb_parse.py

Version:    Alpha_1.0
Date:       2018-03-08
Function:   Obtain Gene characteristics from one or more GenBank records

Copyright:  (c) Matthieu Vizuete-Forster, BBK, 2018
Author:     Matthieu Vizuete-Forster
Address:    Department of Biological Sciences
            Malet Steet, London, WC1E 7HX

--------------------------------------------------------------------------

Copyright not yet assigned

--------------------------------------------------------------------------
Description:
============
This file will strip out the gene data from the GenBank records
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
A_0.1   01.03.18    Alpha   By: MVF
A_0.2   14.03.18    Alpha   By: MVF Comment: Corrected faulty return 
                                            statement at end of function
A_0.3   29.03.18    Alpha   By: MVF Comment: Introduced feature allow
                                            function to ingest GZip files
                                             Corrected dictionary key 
                                            counter to ensure returned
                                            dictionaries contained correct
                                            keys 
"""
import os
import glob
import re
import gzip

path = os.getcwd() + "/{}"
file = glob.glob('*.gz') # test file "AB003151_1.txt"

def GenBankParser(file):
    chr_map = {}
    accession = {}
    gene = {}
    EC_number = {}
    protein_id = {}
    product = {}
    
    for f in file:
        with gzip.open(path.format(f), 'rt') as d:
            data = d.read()
        #             #print(line)
            map_matches = re.findall(r'\/map=\"(?P<map>\d{1,2}.*)\"', data) #corrected regex
            n = 0
            for i in map_matches:
                n += 1 # counter for the dictionary objects
                if len(i) > 0:
                    chr_map[n] = i
            accession_matches = re.findall(r'ACCESSION\s+(?P<acc>[A-Z][A-Z]?[0-9][0-9][0-9][0-9][0-9][0-9]?)', data)
            n = 0
            for i in accession_matches:
                n +=1 
                if len(i) > 0:
                    accession[n] = i
            gene_matches = re.findall(r'\s+/gene=\"(?P<gene>\w*)\"', data)
            n = 0
            for i in gene_matches:
                n += 1
                if len(i) > 0:
                    gene[n] = i
            EC_number_matches = re.findall(r'\s+/EC_number=\"(?P<EC_number>.*)\"', data)
            n = 0
            for i in EC_number_matches:
                n += 1 
                if len(i) > 0:
                    EC_number[n] = i
            protein_id_matches = re.findall(r'\s+/protein_id=\"(?P<protein_id>.*)\"', data)
            n = 0
            for i in protein_id_matches:
                n += 1 
                if len(i) > 0:
                    protein_id[n] = i
            product_matches = re.findall(r'\s+/product=\"(?P<product>.*)\"', data)
            n = 0
            for i in product_matches:
                n += 1
                if len(i) > 0:
                    product[n] = i
    
    return chr_map, accession, gene, EC_number, protein_id, product
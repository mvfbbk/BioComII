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
A_0.1   01.03.18   Alpha   By: MVF
A_0.2   14.03.18   Alpha   By: MVF  Comment: Corrected faulty return 
                                             statement at end of function
"""
import os
import re

#path = os.getcwd() + "/{}"
#file = "AB003151_1.txt"

def GenBankParser(data):
    chr_map = {}
    accession = {}
    gene = {}
    EC_number = {}
    protein_id = {}
    product = {}
    #protein_seq = {}
    #DNA_seq = {}

    #with open(path.format(file), 'r') as data:
    for line in data:
        map_matches = re.findall(r'\s+/map=\"(?P<map>\w+.\w*)\"',line)
        for i in map_matches:
            n = 0 # counter for the accession dictionary objects
            if len(i) > 0:
                n += 1
                chr_map[n] = i
        accession_matches = re.findall(r'ACCESSION\s+(?P<acc>[A-Z][A-Z]?[0-9][0-9][0-9][0-9][0-9][0-9]?)', line)
        for i in accession_matches:
            n = 0 
            if len(i) > 0:
                n += 1
                accession[n] = i
        gene_matches = re.findall(r'\s+/gene=\"(?P<gene>\w*)\"',line)
        for i in gene_matches:
            n = 0 
            if len(i) > 0:
                n += 1
                gene[n] = i
        EC_number_matches = re.findall(r'\s+/EC_number=\"(?P<EC_number>.*)\"',line)
        for i in EC_number_matches:
            n = 0 
            if len(i) > 0:
                n += 1
                EC_number[n] = i
        protein_id_matches = re.findall(r'\s+/protein_id=\"(?P<protein_id>.*)\"',line)
        for i in protein_id_matches:
            n = 0 
            if len(i) > 0:
                n += 1
                protein_id[n] = i
        product_matches = re.findall(r'\s+/product=\"(?P<product>.*)\"',line)
        for i in product_matches:
            n = 0 
            if len(i) > 0:
                n += 1
                product[n] = i

    return chr_map, accession, gene, EC_number, protein_id, product
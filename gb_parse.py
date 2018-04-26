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
A_0.4   26.04.18    Alpha   By: MVF Comment: Code rewrite to return 
                                            dictionary
"""
import os
import glob
import re
import gzip

path = os.getcwd() + "/{}"
file = glob.glob('*.gz') # test file "AB003151_1.txt"

def GenBankParser(file):

    features = {}

    for f in file:
            with gzip.open(path.format(f), 'rt') as d:
                data = d.read().replace("\n", "")
                data = data.replace(" ","")
                s = data.split('//')
    for i in s:
        features_list = []
        accession_matches = re.findall(r'ACCESSION(?P<acc>[A-Z][A-Z]?[0-9][0-9][0-9][0-9][0-9][0-9]?)', i)
        map_matches = re.findall(r'\/map=\"(?P<map>\d{1,2}\w\d{1,2}-?(\w\d{1,2})?)\"', i)
        gene_matches = re.findall(r'/gene=\"(?P<gene>\w*)\"', i)
        EC_number_matches = re.findall(r'/EC_number=\"(?P<EC_number>.*?)\"', i)
        protein_id_matches = re.findall(r'/protein_id=\"(?P<protein_id>\w{3}\d{5}\.\d)\"', i)
        product_matches = re.findall(r'/product=\"(.*?)\"', i)
        join_match = re.findall(r'join\(((\d+..\d+,){1,}(\d+..\d+))\)', i)
        print()

        if len(map_matches) > 0:
            features_list.append([x[0] for x in map_matches])
        else:
            features_list.append('N/A')

        if len(gene_matches) > 0:
            features_list.append(gene_matches[0])
        else:
            features_list.append('N/A')

        if len(EC_number_matches) > 0:
            features_list.append(EC_number_matches[0])
        else:
            features_list.append('N/A')

        if len(protein_id_matches) > 0:
            features_list.append(protein_id_matches[0])
        else:
            features_list.append('N/A')

        if len(product_matches) > 0:
            features_list.append(product_matches[0])
        else:
            features_list.append('N/A')

        if len(join_match) > 0:
            features_list.append(join_match[0])
        else:
            features_list.append('N/A')

        for e in accession_matches:
                    features[e] = features_list

    return features

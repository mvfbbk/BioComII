"""
Programme:  simple_query
File:       simple_query.py

Version:    Alpha0.1
Date:       2018-05-06
Function:   Obtain DNA sequence information from one or more GenBank records

Copyright:  (c) Matthieu Vizuete-Forster, BBK, 2018
Author:     Matthieu Vizuete-Forster
Address:    Department of Biological Sciences
            Malet Steet, London, WC1E 7HX
            
--------------------------------------------------------------------------

released under GPL v3.0 licence

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
Module requires a list of files to be processed. This list can be 
generated automatically from the main script and passed to the function.
By saving the files to be processed in the working directory these can be
parsed automatically in the event that updates are required.

--------------------------------------------------------------------------
Revision History:
=================
A0.1    01.03.18    Alpha   By: MVF
A0.2    06.05.18    Alpha   By: MVF     Comment: 
A0.3    06.05.18    Alpha   By: MVF     Comment: Make function executable
"""

import os
import re
import glob
import csv
import pymysql

path = os.getcwd() + '/{}'

def query_wrapper(query, search_term):

    connection = pymysql.connect(host = 'localhost', 
            user='root', 
            port = 3306, 
            password ='', 
            db = 'bc_test', 
            charset='utf8mb4', 
            cursorclass=pymysql.cursors.DictCursor)

    request = query

    if request == 'get_all':
        sqlQuery = """SELECT *
            FROM genbank gb
            WHERE gb.gene_name      != 'N/A' 
            AND gb.accession_number != 'N/A' 
            AND gb.prot             != 'N/A' 
            AND gb.prod             != 'N/A' 
            AND gb.map_coord        != 'N/A'"""
        with connection.cursor() as cursor:
            cursor.execute(sqlQuery)
            returned_data = cursor.fetchall()
            
    if request == 'get_all_in_db':
        sqlQuery = """SELECT
            gb.accession_number AS accession,
            gb.prod             AS protein_name,
            gb.map_coord        AS location,
            gb.exon_joins       AS cds_locations,
            gb.exon_num         AS num_exons,
            s.prot_seq          AS aa_seq,
            s.DNA_seq           AS dna_seq_whole
            FROM genbank gb,  sequences s
            WHERE gb.gene_name      != 'N/A'
            AND gb.accession_number != 'N/A'
            AND gb.prot             != 'N/A'
            AND gb.prod             != 'N/A'
            AND gb.map_coord        != 'N/A'"""
        with connection.cursor() as cursor:
            cursor.execute(sqlQuery)
            returned_data = cursor.fetchall()

    elif request == 'search':
        sqlQuery = """SELECT * 
        FROM genbank gb 
        WHERE gb.accession_number = '{0}' 
        OR gb.gene_name   = '{0}' 
        OR gb.prot        = '{0}' 
        OR gb.map_coord   = '{0}' 
        OR gb.prod        = '{0}';""".format(search_term)
        with connection.cursor() as cursor:
            cursor.execute(sqlQuery)
            returned_data = cursor.fetchall()

    elif request == 'id_full':
        sqlQuery = """select gb.*, s.DNA_seq, s.prot_seq 
        from genbank gb, sequences s  
        where gb.accession_number = '{0}' 
        or gb.gene_name           = '{0}' 
        or gb.prot                = '{0}' 
        or gb.map_coord           = '{0}' 
        or gb.prod                = '{0}' 
        and gb.accession_number = s.accession_number;""".format(search_term)
        with connection.cursor() as cursor:
            cursor.execute(sqlQuery)
            returned_data = cursor.fetchall()
    
    elif request == 'enzymes':
        sqlQuery = """SELECT e.enz_name, e.enz_seq
                FROM enzymes e
                WHERE e.enz_name LIKE '%HindIII%'
                OR    e.enz_name LIKE '%SmaI%'
                OR    e.enz_name LIKE '%EcoRV%'
                OR    e.enz_name LIKE '%EcoRI%'
                OR    e.enz_name LIKE '%DraI%'
                OR    e.enz_name LIKE '%BamHI%'
                OR    e.enz_name LIKE '%BfaI%'
                OR    e.enz_name LIKE '%SacI%'
                OR    e.enz_name LIKE '%Sau3AI%'
                OR    e.enz_name LIKE '%NotI%';"""
        with connection.cursor() as cursor:
            cursor.execute(sqlQuery)
            returned_data = cursor.fetchall()

    elif request == 'enzyme_list':
        sqlQuery = """SELECT e.enz_name, e.enz_seq
                FROM enzymes e;"""
        with connection.cursor() as cursor:
            cursor.execute(sqlQuery)
            returned_data = cursor.fetchall()
            
    return returned_data

    if __name__ == '__main__':
        query_wrapper(query, search_term)

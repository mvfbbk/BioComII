"""
Programme:  GenerateDB
File:       generate_db.py

Version:    Alpha_1.0
Date:       2018-03-23
Function:   A method for creating SQL database 

Copyright:  (c) Matthieu Vizuete-Forster, BBK, 2018
Author:     Matthieu Vizuete-Forster
Address:    Department of Biological Sciences
            Malet Steet, London, WC1E 7HX

--------------------------------------------------------------------------

released under GPL v3.0 licence

--------------------------------------------------------------------------
Description:
============
Script that will create the database, tables contained within the schema
--------------------------------------------------------------------------
Usage:
======
Functions will require the host, username and password to access the 
database. Additionally the SQL scripts used need to be present in the /SQL
subfolder to allow the database to be build.
--------------------------------------------------------------------------
Revision History:
=================
A_0.1   23.03.18    Alpha   By: MVF
A_0.2   06.05.18    Alpha   By: MVF Comment: rewrite to populate from 
                                            input files
"""
import os
import getpass
import re
import glob
import csv
import pymysql

path = os.getcwd() + '/{}'
g = 'genbank.csv'
d = 'seq.csv'
p = 'prot.csv'
e = 'enzymes.csv'

hst = input('host: ')
usr = input('user: ')
passwd = getpass.getpass(prompt='Password', stream=None)

connection = pymysql.connect(host = hst, 
        user= usr, 
        port = 3306, 
        password = passwd,  
        charset='utf8mb4', 
        cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        for line in open(path.format('SQL/create_tables.sql')):
            cursor.execute(line)
except Exception as msg:
    print(msg)
connection.commit()

with open(path.format(g),'rt') as gen_bank_data:
    for row in gen_bank_data.readlines():
        x = row.split(';')
        acc_num   = x[0]
        gene_name = x[1]
        map_coord = x[2]
        prot      = x[3]
        prod      = x[4]
        exon_join = x[5]
        exon_num  = x[6]

        sqlQuery = """INSERT INTO genbank (`accession_number`,`gene_name`, `map_coord`, `prot`, `prod`, `exon_join`, `exon_num`) 
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')""".format(acc_num, gene_name, map_coord, prot, prod, exon_join, exon_num)

        try:
            with connection.cursor() as cursor:
                cursor.execute(sqlQuery)
        except Exception as msg:
            print(msg)
        connection.commit()

try:
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO sequences (accession_number) SELECT accession_number FROM genbank;")
        cursor.execute(sqlQuery)
except Exception as msg:
        print(msg)
connection.commit()

with open(path.format(d), 'rt') as DNA_data:
    for row in DNA_data.readlines():
        z = row.split(';')
        DNA_seq = z[1]

        sqlQuery = "INSERT INTO temp_seq_table (`VALUE`) VALUES ('{0}')".format(DNA_seq)

    try:
        with connection.cursor() as cursor:
            cursor.execute("CREATE TEMPORARY TABLE temp_seq_table (table_key INT AUTO_INCREMENT, value LONGTEXT, PRIMARY KEY (table_key));")
            cursor.execute(sqlQuery)
            cursor.execute("UPDATE sequences INNER JOIN temp_seq_table SET sequences.DNA_seq = temp_seq_table.value;")
            cursor.execute("DROP TEMPORARY TABLE temp_seq_table")
    except Exception as msg:
            print(msg)
connection.commit()

with open(path.format(p),'rt') as prot_data:
    for row in prot_data.readlines():
        y = row.split(';')
        prot_seq = y[1]

        sqlQuery = "INSERT INTO temp_prot_table (`VALUE`) VALUES ('{0}')".format(prot_seq)
    try:
        with connection.cursor() as cursor:
            cursor.execute("CREATE TEMPORARY TABLE temp_prot_table (table_key INT AUTO_INCREMENT, value LONGTEXT, PRIMARY KEY (table_key))")
            cursor.execute(sqlQuery)
            cursor.execute("UPDATE sequences INNER JOIN temp_prot_table SET sequences.prot_seq = temp_prot_table.value;")
            cursor.execute("DROP TEMPORARY TABLE temp_prot_table")
    except Exception as msg:
            print(msg)
connection.commit()

with open(path.format(e), 'rt') as enz_data:
    for row in enz_data:
        w = row.split(';')
        enz_name = w[0]
        enz_seq = w[1]

        sqlQuery = """INSERT INTO enzymes (`enz_name`, `enz_seq`) VALUE ('{0}','{1}')""".format(enz_name, enz_seq)
        try:
            with connection.cursor() as cursor:
                cursor.execute(sqlQuery)
        except Exception as msg:
                print(msg)
        connection.commit()
"""
Programme:  QueryHandler
File:       query_handler.py

Version:    Alpha_1.0
Date:       2018-03-26
Function:   Run SQL Queries passed in from 

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
A_0.1   01.03.26   Alpha   By: MVF

"""

import pymysql

def QueryHandler(sqlQuery):

    connection = pymysql.connect(host = 'localhost',
                                user = 'root',
                                port = 3306,
                                password ='')
    cursor =  connection.cursor()
    cursor.execute(sqlQuery)

    data = cursor.fetchall()

    connection.close()

    return data

if __name__ == __QueryHandler__:
    Main()
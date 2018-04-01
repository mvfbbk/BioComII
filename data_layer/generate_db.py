"""
Programme:  
File:       generate_db.py

Version:    Alpha_1.0
Date:       2018-03-23
Function:   A method for creating SQL database 

Copyright:  (c) Matthieu Vizuete-Forster, BBK, 2018
Author:     Matthieu Vizuete-Forster
Address:    Department of Biological Sciences
            Malet Steet, London, WC1E 7HX

--------------------------------------------------------------------------

Copyright not yet assigned

--------------------------------------------------------------------------
Description:
============
Module for handling SQL queries

--------------------------------------------------------------------------
Usage:
======
Module requires 

--------------------------------------------------------------------------
Revision History:
=================
A_0.1   23.03.18   Alpha   By: MVF
"""
import PyMySQL.cursors

def CreateDatabase(database):
    #create database
    connection = pymysql.connect(host = 'localhost',
                                user = 'root',
                                port = 3306,
                                password ='')
    try:
        with connection.cursor() as cursor:
            sql = 'CREATE DATABSE %s;' %s database        
            cursor.execute(sql)
    finally:
        connection.close()
  
#create table
def createTable(table, column):
    connection = pymysql.connect(host = 'localhost',
                                user = 'root',
                                port = 3306,
                                password = '',
                                db = database,
                                cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sqlQuery = "CREATE TABLE IF NOT EXISTS %s (%s, );" %s (table, column)
            cursor.execute(sqlQuery)
    finally:
        connection.close()
    
# insert data in to the table
def dataInsert(table, source):
    connection = pymysql.connect(host = 'localhost',
                                user = 'root',
                                port = 3306,
                                password = '',
                                db = database,
                                cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sqlQuery = "BULK INSERT INTO %s FROM %s" %s (table, source) "WITH (rowterminator = '\n', fieldterminator = ',');" 
    finally:
        connection.close()
    
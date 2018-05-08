"""
Program:    BioComII
File:       api.py

Version:    V1.0
Date:       07.05.18
Function:   Expose database layer api for the UI logic layer to consume.

Copyright:  (c) Ifigenia Tsitsa, BBK, 2018
Author:     Ifigenia Tsitsa
Address:    Department of Biological Sciences
            Malet Steet, London, WC1E 7HX
	        Birkbeck, University of London
      
---------------------------------------------------------------------------

Copyright not yet assigned

--------------------------------------------------------------------------
Description:
============
This program connects to the database and exposes query functions 
to the logic layer.
--------------------------------------------------------------------------
Revision History:
=================

A0.1    07.05.18    Alpha   By: IT
A0.2    07.05.18    Alpha   By: IT     Comment: Add initial layer integration.
"""
#*************************************************************************
# import libraries
import json
from glob import glob

from dummy_data.utils import read_enzymes

from .query_wrapper import query_wrapper
#*************************************************************************
def get_all():
     """
        Gets all the genes from the database.

        Return: gene_id, accenssion, protein_name, location for 
        every gene.

        07.05.18 Original By: IT
        """
    return query_wrapper('get_all', '')

#*************************************************************************
def search(param):
     """
        Gets all the genes from the database filtered by a search parameter.

        Return: gene_id, accenssion, protein_name, location for 
        every gene applicable to the search parameter.

        07.05.18 Original By: IT
        """
    return query_wrapper('search', param)

#*************************************************************************
def get_by_gene_id(id):
    """
        Gets all the information from the database for a single gene.

        Return: all the information about a gene.

        07.05.18 Original By: IT
        """
    return query_wrapper('id_full', id)

#*************************************************************************
def get_all_genes():
    """
        Gets all the information about all the  genes from the database.

        Return: all the info about all the genes.

        07.05.18 Original By: IT
        """
    return query_wrapper('id_full_all', 'c')

#*************************************************************************
def get_restriction_enzymes():
    """
        Gets all the restriction enzymes from the database.

        Return: all the restriction enzymes along with their sequences.

        07.05.18 Original By: IT
        """
    return query_wrapper('enzyme_list', '')
#*************************************************************************

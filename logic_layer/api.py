"""
Program:    BioComII
File:       api.py

Version:    V1.0
Date:       07.05.18
Function:   Expose logic layer api with methods for the UI to consume.

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
This program connects to the api exposed by the data layer and runs any 
calculations that are required for the data to be consumed by the UI.

--------------------------------------------------------------------------
Revision History:
=================

A0.1    01.04.18    Alpha   By: IT
A0.2    01.04.18    Alpha   By: IT     Comment: Add initial layer integration.
A0.3    02.05.18    Alpha   By: IT     Comment: Add gene coding region 
                                                calculations and tests.
A0.4    03.05.18    Alpha   By: IT     Comment: Add alignment of dna 
                                                to amino acid.
A0.5    07.04.18    Alpha   By: IT     Comment: Add codon usage, overall codon 
                                                usage and and restriction 
                                                enzyme handling 
                                                relevant functions.
"""
#*************************************************************************
# import libraries
import json
import os

from .codons import codontable
from .errors import NoGeneException
from .gene import Gene
from .utils import calculate_frequencies


#*************************************************************************
class LogicApi:
    """ 
    A class for implementing the logic layer api providing methods
    for the UI to consume. 
    """

    def __init__(self, data_api):
        """ 
        Initialiazes the LogicApi using an instance of the Data Layer Api.
        01.04.18 Original By: IT
        """
        self.data_api = data_api
#*************************************************************************

    def get_all(self):
        """
        Get all the genes from the database, returned in a short format.

        Return: (gene_id, accenssion, protein_name, location) -- A list of 
        dictionaries containing gene_id,accession,protein_name,location for 
        every gene.

        01.04.18 Original By: IT
        """
        return self.data_api.get_all()
#*************************************************************************

    def search(self, parameter):
        """
        Get all the genes from the database filtered by a parameter,
        returned in a short format.

        Input: parameter  --- A parameter pasted from the front-end layer.
        Return: (gene_id, accenssion, protein_name, location) --- A list of 
        dictionaries containing gene_id,accession,protein_name,location
        applicable to the search parameter.

        01.04.18 Original By: IT
        """
        return self.data_api.search(parameter)

#*************************************************************************

    def get_by_gene_id(self, gene_id):
        """
        Get an instance of a Gene class for a specific gene filter by gene_id
        with all the possible information from the database and all the
        appropriate calcucations executed.

        Return: An instance of the Gene class.

        01.04.18 Original By: IT
        """
        if gene_id is None:
            raise NoGeneException

        # Get gene from the database layer
        gene = self.data_api.get_by_gene_id(gene_id)

        return self._gene_dict_to_gene(gene)

# *************************************************************************

    def get_overall_codon_frequencies(self):
        """ 
        Calculate the codon usage across all coding regions.

        Return:(overall_freq)  --- A dictionary containing the frequencies of
        codons in all the coding regions.

        07.04.18 Original By: IT
        """
        genes = self.data_api.get_all_genes()
        dna_to_aa_all = []
        data = {}

        try:
            with open('./data/overall_frequencies.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError as e:
            print(e)

        if len(data) is not 0:
            return data
        #calculate the overall codon frequencies
        for gene_dict in genes:
            g = self._gene_dict_to_gene(gene_dict)
            dna_to_aa_all = dna_to_aa_all + g.dna_to_aa

        overall_freq = calculate_frequencies(dna_to_aa_all)

        # create a file to store the frequencies
        try:
            os.mkdir('./data')
        except FileExistsError:
            pass

        try:
            with open('./data/overall_frequencies.json', 'w') as f:
                json.dump(overall_freq, f)
        except Exception as e:
            print(e)

        return overall_freq

#*************************************************************************

    def get_amino_from_codon(self, codon):
        """
        Align codons with the relevant amino acids.

        Input: codon string
        Return: a string with the long name of the amino acid

        07.04.18 Original By: IT
        """

        return codontable[codon.upper()]

#*************************************************************************

    def get_gene_with_restriction_enzymes(self,
                                          gene_id,
                                          restriction_enzymes_list=None):
        """
        Get an instance of a Gene class for a specific gene filter by gene_id
        with all the possible information from the database and all the
        appropriate calcucations executed and the restriction enzymes
        calculated. If no restriction_enzymes_list is passed then it will 
        get all the available restriction enzymes from the database.

        Input: gene_id string, restriction_enzymes_list list
        Return: An instance of the Gene class.

        06.04.18 Original By: IT
        """
        if gene_id is None:
            raise NoGeneException

        # if the restriction_enzymes_list is empty then get the REs from the db.
        if restriction_enzymes_list is None:
            res = self.data_api.get_restriction_enzymes()
        else:
            res = restriction_enzymes_list
        #
        gene = self.get_by_gene_id(gene_id)
        gene.find_restriction_enzymes(res)

        return gene

#*************************************************************************

    def get_restriction_enzymes(self):
        """
        Obtain the all the restriction enzymes from the database layer.

        Return: (restriction enzymes) --- A list of all the available
        restriction enzymes.

        06.04.18 Original By: IT
        """
        return self.data_api.get_restriction_enzymes()


#*************************************************************************

    def _gene_dict_to_gene(self, gene_dict):
        """
        Creates a Gene Class with the data from the gene_dict.

        Input:gene_dict the dictionary with all the gene data returned from the
        data layer api 
        Return: An instance of the Gene class

        01.04.18 Original By: IT
        """
        return Gene(
            gene_id=gene_dict['gene_id'],
            accession=gene_dict['accession'],
            protein_name=gene_dict['protein_name'],
            location=gene_dict['location'],
            codon_start=gene_dict['codon_start'],
            cds_locations=gene_dict['cds_locations'],
            dna_seq_whole=gene_dict['dna_seq_whole'],
            aa_seq=gene_dict['aa_seq'],
            num_exons=gene_dict['num_exons'],
        )

"""
Program:    BioComII
File:       utils.py

Version:    V1.0
Date:       02.05.18
Function:   Store and calculate the data of every gene.

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

A0.3    02.05.18    Alpha   By: IT     Comment: Add gene coding region 
                                                calculations.
A0.5    05.04.18    Alpha   By: IT     Comment: Add codon usage.
"""
#*************************************************************************
def location_to_int(location_string):
    """ 
        Turn the location strings into intigers.

        Input: a location string

        01.04.18 Original By: IT
        """
    a, b = location_string.split('..')
    a_num = int(a)
    b_num = int(b)

    if a_num > 0 and b_num > 0:
        return a_num, b_num
    else:
        raise Exception
#*************************************************************************

def calculate_frequencies(list_of_dicts):
    """ 
        Calculates the codon frequency in a gene.

        Input: a list of dictionaries  
        Return: a dictionary with the frequencies of each codon

        05.05.18 Original By: IT
        """
    total_count = {}
    freq = {}
    total = len(list_of_dicts)

    # Count the items in the list
    for item in list_of_dicts:
        for k in item.keys():
            if k in total_count:
                total_count[k] += 1
            else:
                total_count[k] = 1

    # Calculate the frequencies
    for k, v in total_count.items():
        freq[k] = (v)/total

    return freq
#*************************************************************************
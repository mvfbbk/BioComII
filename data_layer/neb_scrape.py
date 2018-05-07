"""
Programme:  Neb Scraper
File:       neb_scraper.py

Version:    Alpha_1.0
Date:       2018-03-28
Function:   A method for collecting and filtering enzyme data from the NEB
            website

Copyright:  (c) Matthieu Vizuete-Forster, BBK, 2018
Author:     Matthieu Vizuete-Forster
Address:    Department of Biological Sciences
            Malet Steet, London, WC1E 7HX

--------------------------------------------------------------------------

released under GPL v3.0 licence

--------------------------------------------------------------------------
Description:
============
This module will retrieve the list of enzymes and cut-site recognition 
sequences from the New England Biolabs website. The module will then 
filter the sequences through a secondary function (stickyFinder) that will
remove degenerate and non-base characters from the sequence and determine 
which sequences are palindromic before returning a dictionary of enzyme 
names
--------------------------------------------------------------------------
Usage:
======
Module requires the stickyFinder funtion be present in the working
directory

--------------------------------------------------------------------------
Revision History:
=================
A_0.1   23.03.18   Alpha   By: MVF
"""
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import sticky_finder

path = os.getcwd() + '/{}'
url = 'https://www.neb.com/tools-and-resources/selection-charts/alphabetized-list-of-recognition-specificities'
html = urlopen(url)

#retrieve the html data from NEB website, included in the parameters as different suppliers have varying layout
#not all suppliers have been tested to ensure compatibility
soup = BeautifulSoup(html)

columnHeaders = [th.getText() for th in soup.findAll('tr')[0].findAll('th')]
data_rows = soup.findAll('tr')[1:]
enzyme_sequence = [[td.getText() for td in data_rows[i].findAll('td')] for i in range(len(data_rows))]
df = pd.DataFrame(enzyme_sequence, columns=columnHeaders)

E_list = df['Enzyme'].tolist()
R_seq = df['Recognition Sequence'].tolist()
data = {E_list: R_seq for E_list, R_seq in zip(E_list, R_seq)}
filtered_seq = {}

for k, v in data.items():
    filtered_seq[k] = sticky_finder.sticky_finder(v)
data.clear()
new_dict = {k:v for k, v in filtered_seq.items() if v is not None}
with open(path.format('enzymes.csv'), 'w') as outfile:
    for k, v in new_dict.items():
        outfile.write(str(k))
        outfile.write(';')
        outfile.write(str(v))
        outfile.write('\n')
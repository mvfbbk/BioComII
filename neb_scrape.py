from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.neb.com/tools-and-resources/selection-charts/alphabetized-list-of-recognition-specificities'
html = urlopen(url)

soup = BeautifulSoup(html)
#soup.findAll('tr')

columnHeaders = [th.getText() for th in soup.findAll('tr')[0].findAll('th')]
data_rows = soup.findAll('tr')[1:]
enzyme_sequence = [[td.getText() for td in data_rows[i].findAll('td')] for i in range(len(data_rows))]
df = pd.DataFrame(enzyme_sequence, columns=columnHeaders)
E_list = df['Enzyme'].tolist()
R_seq = df['Recognition Sequence'].tolist()

data = {E_list: R_seq for E_list, R_seq in zip(E_list, R_seq)}
filtered_seq = {}
import stickyFinder
for k, v in data.items():
    filtered_seq[k] = stickyFinder.stickyFinder(v)
data.clear()
new_dict = {k:v for k, v in filtered_seq.items() if v is not None}
print(new_dict)
filtered_seq.clear()
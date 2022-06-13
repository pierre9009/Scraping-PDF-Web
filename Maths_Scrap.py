import requests
from bs4 import BeautifulSoup
import os
import time
output='.\path_of-your_choice\'
site="https://ronan.lauvergnat.fr/Enseignements_actuels_RL.html"
ht=requests.get(site)
soup=BeautifulSoup(ht.text, 'html.parser')

for a in soup.find_all('a', class_="doc"):
	time.sleep(0.5)
	print("Found the URL:", "https://ronan.lauvergnat.fr/"+a['href'])
	temp="https://ronan.lauvergnat.fr/"+a['href']
	tempo=requests.get(temp)
	file_path= os.path.join(output, os.path.basename(temp))
	with open(file_path,'wb') as f:
		f.write(tempo.content)

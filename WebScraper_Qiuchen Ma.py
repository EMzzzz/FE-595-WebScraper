import requests
from bs4 import BeautifulSoup
import pandas as pd

Name = []
Purpose = []
a = 'Name: '
b = 'Purpose: '
for i in range(50):
    response = requests.get("http://3.95.249.159:8000/random_company")
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.text)
    li = soup.select('li')
    li_len = len(li)
    for j in range(li_len):
        if a in li[j].text:
            Name.append(li[j].text[6:])
        elif b in li[j].text:
            Purpose.append(li[j].text[9:])

data = pd.DataFrame({'Name': [],
                     'Purpose': []})
data['Name'] = Name
data['Purpose'] = Purpose
data.to_csv('WebScraper_Qiuchen Ma.csv')

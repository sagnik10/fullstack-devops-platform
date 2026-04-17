import requests
from bs4 import BeautifulSoup
from articles.models import Article,Category

def scrape():
url="https://dev.to"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
titles=soup.find_all("h2")

cat,_=Category.objects.get_or_create(name="DevOps")

for t in titles[:5]:
Article.objects.create(
title=t.text,
slug=t.text.replace(" ","-"),
content=t.text,
category=cat,
published=False
)

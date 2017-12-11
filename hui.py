import requests
from bs4 import BeautifulSoup as soup


url="https://book.douban.com/top250"

def getcont():
    r=requests.get(url)
    print(r.content)

def main():
    response=getcont(url)
    text=soup(html,"html.parser")

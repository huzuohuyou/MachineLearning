__author__ = 'wuhailong 2016-12-16'
import requests
from bs4 import BeautifulSoup
import re
import codecs
def getGils(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    start_html=requests.get(url,headers = headers)
    Soup=BeautifulSoup(start_html.text,'lxml')
    gilslist=Soup.find_all(class_='p-tit')
    content=''
    for item in gilslist:
        hrefitem = BeautifulSoup(str(item),'lxml')
        if "【" in hrefitem.a.get_text():
            continue
        else:
            content +=hrefitem.a['href']+'\t'+hrefitem.a.get_text()+'\n'
        #print(hrefitem.a['href']+'\t'+hrefitem.a.get_text())
    return content

def getDetail(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    start_html=requests.get(url,headers = headers)
    soup=BeautifulSoup(start_html.text,'lxml')
    detail=soup.find_all(class_='p-entry')
    soupdetail=BeautifulSoup(str(detail),'lxml')
    soupdetail.find_all('p')
    for item  in soupdetail:
        print(item.get_text())
    print(detail)

if __name__ == '__main__':
    # i=1
    # content=''
    # while(i<=15):
    #     url="http://date.jobbole.com/page/{page}/".format(page=str(i))
    #     print(url)
    #     content+=getGils(url)
    #     i=i+1
    # fr = codecs.open ( 'content.txt', 'w', 'utf_8' )
    # fr.write(content)
    getDetail("http://date.jobbole.com/3849/")
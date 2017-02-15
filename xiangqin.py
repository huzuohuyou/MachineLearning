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
    details=''

    for item  in soupdetail.get_text().split('\n'):
        #details+=soupdetail.get_text().replace(' ', '')
        if '：' in item:
            s=item.split('：')[1].replace('[','').replace("登录后查看»	]","").replace(' ', '')+'\t'
            details+=s
            print(s)
        else:
            details+=item.replace('[','').replace("登录后查看»	]","").strip()
    #print(details)
    return  details

    #print(content)

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
    fr = codecs.open ( 'content.txt', 'r' , 'utf_8')
    content=''
    while 1:
        line = fr.readline()
        if not line:
            break
        print(line)
        content+=getDetail(line.split('\t')[0])+'\n'
    fw = codecs.open ( 'details.txt', 'w', 'utf_8' )
    fw.write(content)
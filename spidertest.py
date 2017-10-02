import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100011693%204814%20600038463&IsNodeId=1&cm_sp=CAT_SSD_1-_-VisNav-_-2.5%E2%80%9D-Inch_1'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")


# parada lapas source 0_o
# page_soup.body

containers = page_soup.findAll("div",{"class":"item-container"})

#parada cik atrada div ar klasi item-container
len(containers)

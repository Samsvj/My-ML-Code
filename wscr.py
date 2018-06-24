#!/usr/bin/python3

#import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
my_url='https://www.newegg.com/global/in/Video-Cards-Video-Devices/Category/ID-38'

uClient=ureq(my_url)

page_html=uClient.read()
uClient.close()
#htmlparsing
page_soup=soup(page_html, "html.parser")

#grabs each product 
containers=page_soup.findAll("div",{"class":"item-container"})

filename="products.csv"
f=open(filename,"w")

headers= "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
    brand= container.div.div.a.img["title"]
    title_container=container.findAll("a",{"class":"item-title"})
    product_name=title_container[0].text
    shipping_container=container.findAll("li",{"class":"price-ship"})
    shipping=shipping_container[0].text.strip()
    print ("Brand: " +brand)
    print ("Product_name: "+product_name)
    print ("Shipping: "+shipping)
    
    f.write(brand + "," +product_name.replace(",", "|")+"," + shipping +"\n")

f.close()


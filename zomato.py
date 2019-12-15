import requests,pprint
from bs4 import BeautifulSoup
from selenium import webdriver

driver=webdriver.Chrome("./chromedriver") 		#same version google chrome and chromedriver
driver.get("https://www.zomato.com/ncr")
page=driver.execute_script("return document.documentElement.outerHTML")			#b
driver.quit()

def zomato_link():
	soup=BeautifulSoup(page,"html.parser")
	main_div=soup.find("div",class_="ui segment row")
	place=main_div.find_all("a",class_="col-l-1by3 col-s-8 pbot0")
	link_list=[]
	counter=0
	list_of_place=[]
	for pl in place:
		url=pl.get("href")
		link_list.append(url)
		all_place=(pl.text.strip().split())
		counter+=1
		places_list=(counter," ".join(all_place))
		list_of_place.append(places_list)
	# pprint.pprint(list_of_place)
	return(link_list)		
places=zomato_link()
# pprint.pprint(places)
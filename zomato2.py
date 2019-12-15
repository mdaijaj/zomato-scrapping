import requests,pprint,json
from zomato import zomato_link
from bs4 import BeautifulSoup 
from selenium import webdriver

def resturant_details():
	seemore_list=[]
	for url in zomato_link():
		driver=webdriver.Chrome("./chromedriver")  #same version google chrome and chromedriver
		driver.get(url)
		page=driver.execute_script("return document.documentElement.outerHTML")
		driver.quit()

		soup=BeautifulSoup(page,"html.parser")
		seemore=soup.find_all("a",class_="zred")
		for j in seemore:
			dic={}
			link_see=j["href"]

			driver2=webdriver.Chrome("./chromedriver")
			driver2.get(link_see)
			page2=driver2.execute_script("return document.documentElement.outerHTML")
			driver2.quit()

			soup2=BeautifulSoup(page2,"html.parser")
			main_div=soup2.find_all("div",class_="content")
			for m in main_div:
				rate=m.find("span",class_="col-s-11 col-m-12 pl0")
				if (rate != None):
					rate1=rate.text
					dic["rate"]=rate1

				rating=m.find("div",class_="ta-right floating search_result_rating col-s-4 clearfix")
				if rating!=None:
					rating1=rating.text.split()[0]
					dic["rating"]=rating1

				times=m.find("div",class_="col-s-11 col-m-12 pl0 search-grid-right-text ")
				if (times!=None):
					time=times.text.strip()	
					dic["time"]=time

				names=m.find("div",class_="col-s-12")
				if names!=None:
					data=names.text.strip().split("\n")
					address=(data[-1])
					if len(data)==5:
						hotel_name=data[1]
					else:
						hotel_name=data[0]
					dic["name"]=hotel_name
					dic["address"]=address
					pprint.pprint(dic)
				
			with open("zomato.json","w")as files:
				inf=json.dump(dic,files,indent=4)
resturant_details()
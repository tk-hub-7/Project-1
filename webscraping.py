import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/tyy/4io/~cs-moay4jbyje/pr?sid=tyy%2C4io&collection-tab-name=MOTOROLA+Edge+60+Fusion&pageCriteria=default&param=220&otracker=clp_bannerads_1_6.bannerAdCard.BANNERADS_moto%2Bedge%2B60%2Bfusion%2BPL-Sale%2BIs%2BOn_mobile-phones-store_VFA5SB5ISYB4&sort=price_asc")

#print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
names=soup.find_all('div', class_='KzDlHZ')
print(names)
name=[]
for i in names[0:4]:
    d=i.text
    name.append(d)
    #print(name)
prices=soup.find_all('div', class_='Nx9bqj _4b5DiR')
#print(prices)
price=[]
for i in prices[0:4]:
     d=i.text
     price.append(d)
     #print(price)  
ratings=soup.find_all("div", class_="XQDdHH")
#print(ratings)
rating=[]
for i in ratings[0:4]:
     d=i.text
     rating.append(d)
     #print(rating)
discounts=soup.find_all("div", class_="UkUFwK")    
#print(discounts)
discount=[]
for i in discounts[0:4]:
    d=i.text
    discount.append(d)
    #print(discount)
links=soup.find_all("a" ,class_="CGtC98") 
link=[]
for i in links[0:4]:
     d="https://www.flipkart.com"+i['href']
     link.append(d)
    # print(link)
images=soup.find_all("img", class_="DByuf4") 
image=[]
for i in images[0:4]:
     d=i['src']
     image.append(d)
    # print(image)
data={'Names':pandas.Series(name),'price':pandas.Series(price),'Ratings':pandas.Series(rating),'discounts':pandas.Series(discount),'images':pandas.Series(image),'links':pandas.Series(link)}
print(data)
df=pandas.DataFrame(data)
print(df)  
df.to_csv("mobiles_data.csv")  

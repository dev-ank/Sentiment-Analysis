'''

Code to scrape the reviews from www.etsy.com to further analyse those reviews as 
positive or negative based on a pretrained neural network model

'''



from selenium import webdriver
import pandas as pd
import sqlite3 as sql
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("user-agent=python 2.7")


all_reviews=[]

for i in range(186,250):
    url=f"https://www.etsy.com/in-en/c/jewelry/necklaces/pendants?ref=pagination&explicit=1&page={i}"
    browser = webdriver.Chrome(chrome_options=opts)  #driver in current directory
    browser.get(url)
    print(f'Page {i-1} of 250 scraped')
    for prod_num in range(1,65):
        path=f'//*[@id="content"]/div/div[1]/div/div[4]/div[2]/div[2]/div[3]/div/div/ul/li[{prod_num}]/div/a'
        
        try:
            each_url=browser.find_element_by_xpath(path).get_property('href')
            browser.get(each_url)
            reviews=browser.find_elements_by_class_name('wt-content-toggle--truncated-inline-multi')
            x=0
            while x<4:
                try:
                    all_reviews.append(reviews[x].text)
                except:
                    pass
                x+=1
            browser.get(url)
            print(f'product {prod_num} scraped')
        except:
            pass
    browser.close()
    

df=pd.DataFrame()
df['Reviews']=all_reviews
    

conn=sql.connect('extracted_reviews.db')        #storing the scraped reviews into DB which will be used to determine the sentiments based on pre trained moedel
df.to_sql('scraped_table',conn)
     

df.to_csv('extracted_reviews4.csv',index=False)   #storing the reviews into a csv file





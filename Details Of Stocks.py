#!/usr/bin/env python
# coding: utf-8

# In[1]:



from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd                                               #for converting data into table
from IPython.core.display import HTML
HTML("<b>Rendered HTML</b>")

from bs4 import BeautifulSoup                                   #use for parsing into html


# In[2]:


url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=INFY&illiquid=0&smeFlag=0&itpFlag=0"


# In[3]:


driver = webdriver.Chrome(ChromeDriverManager().install()) #For installing chromeDriver
driver.get(url)                                            #get the url page
import time
time.sleep(5)


# In[4]:


action = ActionChains(driver)
html = driver.page_source              
soup = BeautifulSoup(html,"html.parser")         #parse the page source into html

time.sleep(7)


# In[5]:


#Stock main information

Stock_name = soup.find("span",attrs={"id":'companyName'})
Stock_Code = soup.find("a",attrs={"class":'sel'})
Stock_High_Day = soup.find("div",attrs={"id":'dayHigh'})
Stock_Low_day = soup.find("div",attrs={"id":'dayLow'})
Date = soup.find("span",attrs={"id":'LastUpdatedDiv'})
Symbol = soup.find("span",attrs={"id":'symbol'})
ISIN_Code = soup.find("span",attrs={"id":'isinCode'})
Status_code = soup.find("span",attrs={"id":'statusCode'})
Previous_Close = soup.find("div",attrs={"id":'previousClose'})
Stock_Open_Value = soup.find("div",attrs={"id":'open'})
Last_price = soup.find("span",attrs={"id":'lastPrice'})
Precentage_changes = soup.find("a",attrs={"id":'pChange'})
Increased_by = soup.find("span",attrs={"id":'change'})


# In[6]:


#Trade Snapshot value
#left cloumn
VWAP = soup.find("span",attrs={"id":'vwap'})
Face_Value = soup.find("span",attrs={"id":'faceValue'})
Traded_Volume = soup.find("span",attrs={"id":'tradedVolume'})
Traded_Value = soup.find("span",attrs={"id":'tradedValue'})
Free_Float_Market_Cap = soup.find("span",attrs={"id":'ffmid'})
Fifty_Two_week_high = soup.find("span",attrs={"id":'high52'})
Fifty_Two_week_low = soup.find("span",attrs={"id":'low52'})
Lower_Price_Band = soup.find("span",attrs={"id":'lowpriceBand'})
Upper_Price_Band = soup.find("span",attrs={"id":'upperpriceBand'})


# In[7]:


sy = soup.find('ul',attrs={'id':'pe_details'})
Sy_PE= list(sy.children)[0]
Se_PE =list(sy.children)[1]
SeI = list(sy.children)[2]


# In[8]:


#trade snapshot value
#right column
#order Book Table

result = soup.find('div',attrs={'id': 'tab9Content'})
table_rows = result.find_all('tr')
l = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    l.append(row)
    
order_book_table = pd.DataFrame(l, columns=["Buy Qty.","Buy Price","Sell Price","Sell Qty."])
order_book_table = order_book_table.drop([0], axis=0)


# In[10]:


order_book_table


# In[11]:


# variable names
Information_name_List = ['Stock Name','Stock Code','Stock High Day','Stock Low day','Date', 'Symbol', 'ISIN Code','Status Code',
                         'Previous Close','Stock Open Value','Stock Last','Stock Precentage changes','Stock Value Increased_by',
                         'VWAP','Stock Face Value', 'Traded Volume (Shares)','Traded Value (lacs)','Free_Float_Market_Cap (crs)',
                         'Fifty_Two_week_high','Fifty_Two_week_low','Lower_Price_Band','Upper_Price_Band',list(Sy_PE.children)[0],
                        list(Se_PE.children)[0],list(SeI.children)[0]]

# variable name text information fetch
stock_information_list = [Stock_name.text,Stock_Code.text,Stock_High_Day.text,Stock_Low_day.text,Date.text,Symbol.text,ISIN_Code.text,
                          Status_code.text,Previous_Close.text,Stock_Open_Value.text,Last_price.text,Precentage_changes.text,
                          Increased_by.text,VWAP.text,Face_Value.text,Traded_Volume.text,Traded_Value.text,Free_Float_Market_Cap.text,
                          Fifty_Two_week_high.text,Fifty_Two_week_low.text,Lower_Price_Band.text,Upper_Price_Band.text,list(Sy_PE.children)[1].text,
                         list(Se_PE.children)[1].text,list(SeI.children)[1].text]

dic = { 'Variable Name':Information_name_List, 'Infosys Stock Information':stock_information_list}


# In[12]:


print(dic)


# In[59]:


Stock_Information_Df = pd.DataFrame(dic)


# In[49]:


Stock_Information_Df


# In[52]:


concatDf = pd.concat([Stock_Information_Df,order_book_table],axis=1)


# In[51]:


concatDf


# In[17]:


concatDf.to_csv("Infosys Stock Data information.csv", index = None)


# In[42]:


Peer_info = soup.find('div',attrs={'class': 'accordian'})
table_row = result.find_all('tr')
pi = []

for tr in table_row:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    pi.append(row)


# In[43]:


pi


# In[ ]:





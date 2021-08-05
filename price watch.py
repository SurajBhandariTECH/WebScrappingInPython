#!/usr/bin/env python
# coding: utf-8

# In[20]:



from webdriver_manager.chrome import ChromeDriverManager         #use to install the webdriver for chrome and store in cache 
from selenium import webdriver                                   #RUN THE WEBDRIVER eg chormedriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd                                               #for converting data into table,create dataFrames
from IPython.core.display import HTML
HTML("<b>Rendered HTML</b>")

from bs4 import BeautifulSoup    


# In[21]:


url = "https://www1.nseindia.com/companytracker/cmtracker.jsp?symbol=INFY&cName=cmtracker_nsedef.css#"


# In[40]:


driver = webdriver.Chrome(ChromeDriverManager().install()) #For installing chromeDriver
driver.get(url)                                            #get the url page
import time
time.sleep(5)


# In[41]:


action = ActionChains(driver)
html = driver.page_source              
soup = BeautifulSoup(html,"html.parser")         #parse the page source into html

time.sleep(7)


# In[56]:


result = soup.find('div',attrs={'id': 'centertab'})
new_result = list(result.children)[1]
next_result = list(new_result.children)[1]


# In[139]:


#security information
Equality_Shares= soup.find("td",attrs={"class":'specialhead2_leftalign'}).text
Most_Active_Futures = "Most Active Futures \n" + soup.find("div",attrs={"id":'strike_price_futstk'}).text
Most_Active_Call ="Most_Active_Call\n "+ soup.find("div",attrs={"id":'strike_price_ca'}).text
Most_Active_Put = "Most_Active_Put \n" + soup.find("div",attrs={"id":'strike_price_pa'}).text
Most_Active_Nifty_Futures = "Most_Active_Nifty_Futures \n"+ soup.find("div",attrs={"id":'strike_price_nifty'}).text
Most_Active_Midcap_Futures =" Most_Active_Midcap_Futures "

lis_security = [Equality_Shares,Most_Active_Futures,Most_Active_Call,Most_Active_Put,
                Most_Active_Nifty_Futures,Most_Active_Midcap_Futures]


# In[155]:


#LTP column
LTP_list = [soup.find("div",attrs={"id":'ltp_cm'}).text,soup.find("div",attrs={"id":'ltp_futstk'}).text,
           soup.find("div",attrs={"id":'ltp_ca'}).text,
           soup.find("div",attrs={"id":'ltp_pa'}).text,
           soup.find("div",attrs={"id":'ltp_nifty'}).text,
           '-']


# In[156]:


LTP_list


# In[157]:


#buy_quantity
buy_qty = [soup.find("div",attrs={"id":'buy_qty_cm'}).text,
          soup.find("div",attrs={"id":'buy_qty_futstk'}).text,
          soup.find("div",attrs={"id":'buy_qty_ca'}).text,
          soup.find("div",attrs={"id":'buy_qty_pa'}).text,
           soup.find("div",attrs={"id":'buy_qty_nifty'}).text,"-"]


# In[158]:


buy_qty


# In[159]:


buy_Price = [soup.find("div",attrs={"id":'buy_price_cm'}).text,
          soup.find("div",attrs={"id":'buy_price_futstk'}).text,
          soup.find("div",attrs={"id":'buy_price_ca'}).text,
          soup.find("div",attrs={"id":'buy_price_pa'}).text,
           soup.find("div",attrs={"id":'buy_price_nifty'}).text,"-"]


# In[160]:


Sell_Price = [soup.find("div",attrs={"id":'sell_price_cm'}).text,
          soup.find("div",attrs={"id":'sell_price_futstk'}).text,
          soup.find("div",attrs={"id":'sell_price_ca'}).text,
          soup.find("div",attrs={"id":'sell_price_pa'}).text,
           soup.find("div",attrs={"id":'sell_price_nifty'}).text,"-"]


# In[161]:


Sell_Qty = [soup.find("div",attrs={"id":'sell_qty_cm'}).text,
          soup.find("div",attrs={"id":'sell_qty_futstk'}).text,
          soup.find("div",attrs={"id":'sell_qty_ca'}).text,
          soup.find("div",attrs={"id":'sell_qty_pa'}).text,
           soup.find("div",attrs={"id":'sell_qty_nifty'}).text,"-"]


# In[162]:


TurnOver =  [soup.find("div",attrs={"id":'turnover_cm'}).text,
          soup.find("div",attrs={"id":'turnover_futstk'}).text,
          soup.find("div",attrs={"id":'turnover_ca'}).text,
          soup.find("div",attrs={"id":'turnover_pa'}).text,
           soup.find("div",attrs={"id":'turnover_nifty'}).text,"-"]


# In[163]:


premiumTurnOver = [soup.find("div",attrs={"class":'tablerow1'}),
          soup.find("div",attrs={"class":'tablerow1'}),
          soup.find("div",attrs={"id":'premturnover_ca'}).text,
          soup.find("div",attrs={"id":'premturnover_pa'}).text,
           soup.find("div",attrs={"class":'tablerow1'}),"-"]


# In[164]:


premiumTrunOver


# In[165]:


dic = {'Security':lis_security, 'LTP':LTP_list, 'Buy Qty':buy_qty,'Buy Price':buy_Price, 'Sell Price':Sell_Price, 
      'Sell Qty':Sell_Qty, 'Turnover(in lakhs)':TurnOver, 'Premium Turnover(in lakhs)':premiumTrunOver}


# In[166]:


Price_Watch_table = pd.DataFrame(dic)


# In[172]:


left_align_Price_Watch_table = Price_Watch_table.style.set_properties(**{'text-align':"left"})
left_aligned_price_watch_df = left_align_Price_Watch_table.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'center')])])
display(left_align_Price_Watch_table)


# In[173]:


Price_Watch_table.to_csv("Price Watch.csv",index =None)


# In[ ]:





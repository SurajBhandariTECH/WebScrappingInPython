#!/usr/bin/env python
# coding: utf-8

# In[116]:



from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd                                               #for converting data into table
from IPython.core.display import HTML
HTML("<b>Rendered HTML</b>")

from bs4 import BeautifulSoup                                   #use for parsing into html


# In[117]:


url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=INFY&illiquid=0&smeFlag=0&itpFlag=0"


# In[118]:


driver = webdriver.Chrome(ChromeDriverManager().install()) #For installing chromeDriver
driver.get(url)                                            #get the url page
import time
time.sleep(5)


# In[119]:


action = ActionChains(driver)
html = driver.page_source              
soup = BeautifulSoup(html,"html.parser")         #parse the page source into html

time.sleep(7)


# In[120]:


Face_value0 = soup.find("span",attrs={"id":'faceValue0'}).text
Symbol0 = soup.find("span",attrs={"id":'symbol0'}).text
LTP = soup.find("span",attrs={"id":'lastPrice0'}).text
Percentage_change0 = soup.find("span",attrs={"id":'pChange0'}).text
Traded_Value0 = soup.find("span",attrs={"id":'tradedValue0'}).text
Traded_Volume0 = soup.find("span",attrs={"id":'tradedVolume0'}).text
VWAP0 = soup.find("span",attrs={"id":'vwap0'}).text
Ex_Date0 = soup.find("span",attrs={"id":'exDate0'}).text
Corporate_action = soup.find("span",attrs={"id":'corporateAction0'}).text
Qty_Traded = soup.find("span",attrs={"id":'quantityTraded0'}).text
Deliverable_Qty = soup.find("span",attrs={"id":'deliveryQuantity0'}).text 
Percentage_Delivery_Qty_to_Traded_Qty = soup.find("span",attrs={"id":'deliveryToTradedQuantity0'}).text
Security_VaR = soup.find("span",attrs={"id":'securityVar0'}).text
VaR_Margin = soup.find("span",attrs={"id":'varMargin0'}).text
Applicable_Margin_Rate = soup.find("span",attrs={"id":'applicableMargin0'}).text
Extreme_Loss_Rate = soup.find("span",attrs={"id":'extremeLossMargin0'}).text


# In[121]:


Peer_Information_name_List =['Symbol','----------FUNDAMENTALS----------DATA','Face value','LTP','Percentage change','Traded Value','Traded Volume',
                        'VWAP','----------RATIO ANALYSIS----------DATA','Ex Date','Corporate action','----------RISK PROFILE----------DATA',
                        'Qty. Traded','Deliverable Qty.',
                        'Percentage Delivery Qty .to Traded Qty.','SecurityVaR',
                        'VaR Margin','Applicable Margin Rate','Extreme Loss Rate']

Peer_stock_information_list = [Symbol0,'',Face_value0,LTP,Percentage_change0,Traded_Value0,Traded_Volume0,
                          VWAP0,'',Ex_Date0,Corporate_action,'',Qty_Traded,Deliverable_Qty,
                          Percentage_Delivery_Qty_to_Traded_Qty,Security_VaR,
                          VaR_Margin,Applicable_Margin_Rate,Extreme_Loss_Rate]


# In[122]:


peer_dictionary = {'PEER COMPARISION':Information_name_List,"VALUES":stock_information_list }


# In[131]:


Peer_Stock_Information_Df = pd.DataFrame(peer_dictionary)


# In[133]:


left_align_peer_Stock_table = Peer_Stock_Information_Df.style.set_properties(**{'text-align':"left"})
left_aligned_peer_stock_df = left_align_peer_Stock_table.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'center')])])
display(left_aligned_peer_stock_df)


# In[134]:


Stock_Information_Df.to_csv("Peer Comparision.csv",index=None)


# In[ ]:





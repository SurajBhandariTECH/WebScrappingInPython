#!/usr/bin/env python
# coding: utf-8

# In[1]:



from webdriver_manager.chrome import ChromeDriverManager         #use to install the webdriver for chrome and store in cache 
from selenium import webdriver                                   #RUN THE WEBDRIVER eg chormedriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd                                               #for converting data into table,create dataFrames
from IPython.core.display import HTML
HTML("<b>Rendered HTML</b>")

from bs4 import BeautifulSoup    


# In[2]:


url = "https://www1.nseindia.com/companytracker/cmtracker.jsp?symbol=INFY&cName=cmtracker_nsedef.css#"


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


# In[50]:


#company Information

result = soup.find('div',attrs={'id': 'compInfo'})
table_rows = result.find_all('tr')
l = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    l.append(row)
    
order_book_table = pd.DataFrame(l, columns=["Infosys Limited"])
order_book_table = order_book_table.drop([0], axis=0)


# In[51]:


order_book_table_left_align = order_book_table.style.set_properties(**{'text-align': 'left'})


# In[52]:



  
left_aligned_order_df = order_book_table_left_align.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'center')])])
  


# In[53]:


display(left_aligned_order_df)


# In[84]:


order_book_table.to_csv("Company Information.csv",index = None)


# In[54]:


#corporate action

Corporate_result = soup.find('div',attrs={'id': 'corpAction'})
tablerow = Corporate_result.find_all('tr')
corporate_list = []


for tr in tablerow:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    corporate_list.append(row)
    
Corporate_Table_info = pd.DataFrame(corporate_list, columns=['Ex-Date','','','','Purpose'])
c = Corporate_Table_info.drop([0], axis=0)


# In[66]:


display(Corporate_Table_info)


# In[85]:


Corporate_Table_info.to_csv("corporate information.csv",index = None)


# In[80]:


#announcement
announcement_result = soup.find('div',attrs={'id': 'annoucement'})
trow = announcement_result.find_all('tr')
announcement_list = []


for tr in trow:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    announcement_list.append(row)

announcement_Table_info = pd.DataFrame(announcement_list, columns=['','ANNOUNCEMENTS',''])
announcement_Table_info = announcement_Table_info.drop([0], axis=0)


# In[81]:


announcement_Table_info


# In[86]:


announcement_Table_info.to_csv("announcements.csv",index = None)


# In[ ]:





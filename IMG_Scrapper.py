#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import logging
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[ ]:





# In[2]:


query = "elon musk"
#url = https://www.google.com/search?q=query&tbm=isch&ved=2ahUKEwjoxZO7tdWAAxVloekKHa1aDHYQ2-cCegQIABAA&oq=elon+musk&gs_lcp=CgNpbWcQAzIECCMQJzIKCAAQigUQsQMQQzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIFCAAQgAQyBQgAEIAEUMoDWMoDYIUOaABwAHgAgAHQAYgBnwOSAQMyLTKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=VZbWZKjHCeXCpgettbGwBw&bih=707&biw=1536&rlz=1C1CHBF_enIN958IN958


# In[3]:


response=requests.get(f"https://www.google.com/search?q={query}&tbm=isch&ved=2ahUKEwjoxZO7tdWAAxVloekKHa1aDHYQ2-cCegQIABAA&oq=elon+musk&gs_lcp=CgNpbWcQAzIECCMQJzIKCAAQigUQsQMQQzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIFCAAQgAQyBQgAEIAEUMoDWMoDYIUOaABwAHgAgAHQAYgBnwOSAQMyLTKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=VZbWZKjHCeXCpgettbGwBw&bih=707&biw=1536&rlz=1C1CHBF_enIN958IN958")


# In[4]:


response


# In[5]:


soup=BeautifulSoup(response.content,"html.parser")


# In[6]:


soup


# In[7]:


image_tags=soup.find_all("img")


# In[8]:


image_tags


# In[9]:


del image_tags[0]


# In[10]:


image_tags


# In[11]:


len(image_tags)


# In[12]:


response = requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ91bYeYuNi93Snai-G61-ct5IkXUEpoeW1RpiOFFuRWggNeJf-7uN0OZsy5XI&s").content


# In[13]:


response


# In[ ]:





# In[ ]:





# In[14]:


save_dir = "images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


# In[15]:


for i in image_tags:
    print(image_tags.index(i))


# In[18]:


for i in image_tags:
    for i in image_tags:
        
        image_url=i['src']
        image_data = requests.get(image_url).content
    with open(os.path.join(save_dir,f"{query}_{image_tags.index(i)}.jpg"),"wb") as f:
        f.write(image_data)
                          


# In[ ]:





# In[ ]:





# In[ ]:





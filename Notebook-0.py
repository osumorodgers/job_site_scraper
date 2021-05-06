#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from bs4 import BeautifulSoup

URL = 'https://www.brightermonday.co.ke/jobs?sort_by=latest'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


# In[7]:


### Finding element by id
results = soup.find(class_='top-jobs-if-containerb')


# In[9]:


job_elems = results.find_all('div', class_='top-jobs__card--border-bottom top-jobs__card')


# In[13]:


for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h3', class_='wrapper--inline-flex')
    company_elem = job_elem.find('div', class_='if-content-panel')
    location_elem = job_elem.find('div', class_='top-jobs__content')
    employment_type = job_elem.find('div', class_= 'top-jobs__content')
    dep = job_elem.find('div', 'top-jobs__content-meta')
    print(title_elem)
    print(company_elem.text)
    print(location_elem.text)
    print(employment_type.text)
    print(dep.text)
    print()


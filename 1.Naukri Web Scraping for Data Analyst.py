#!/usr/bin/env python
# coding: utf-8

# # OBJECTIVE : 
#     To write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.
#     This task will be done in following steps:
#     1. first get the webpage https://www.naukri.com/
#     2. Enter “Data Analyst” in “Skill,Designations,Companies” field and enter “Bangalore” in “enter the location”   field.
#     3. Then click the search button.
#     4. Then scrape the data for the first 10 jobs results you get.
#     5. Finally create a dataframe of the scraped data.
#     Note- All of the above steps have to be done in code. No step is to be done manually.

# In[1]:


#importing required libraries.
import pandas as pd
import selenium
from selenium import webdriver


# In[2]:


#connecting the web driver.
driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver-v0.29.0-win64\geckodriver.exe')


# In[3]:


driver.get('https://www.naukri.com/')


# In[4]:


#finding and filling the title and location of the required job using automation.
search_job = driver.find_element_by_id('qsb-keyword-sugg')
search_job.send_keys('Data Analyst')
search_loc = driver.find_element_by_xpath('//input[@id="qsb-location-sugg"]')
search_loc.send_keys('Banglore')


# In[5]:


#finding and clicking the search button using automation.
search_btn = driver.find_element_by_xpath("//div[@class='search-btn']")
search_btn.click()


# In[6]:


#creating the list.
Job_title=[]
Job_location=[]
Comapany_name=[]
Experience_required=[]


# In[20]:


#extracting job title.
title_tags = driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")


# In[21]:


title_tags


# In[22]:


for i in title_tags:
    title=i.text
    Job_title.append(title)
Job_title


# In[23]:


#extracting the location tags.
location_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span")
location_tags


# In[24]:


for i in location_tags:
    location=i.text
    Job_location.append(location)
Job_location


# In[25]:


#extracting the comapany names.
company_tags= driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_tags


# In[26]:


for i in company_tags:
    company=i.text
    Comapany_name.append(company)
Comapany_name


# In[27]:


#extracting the Experience tags
exp_tags = driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span")
exp_tags


# In[28]:


for i in exp_tags:
    exp=i.text
    Experience_required.append(exp)
Experience_required


# In[29]:


#checking the length of the extracted lists.
print(len(Experience_required),len(Comapany_name),len(Job_location),len(Job_title))


# In[30]:


#creating a data frame.
Jobs_DataAnalyst=pd.DataFrame({})
Jobs_DataAnalyst['Job_Title'] = Job_title[0:10]
Jobs_DataAnalyst['Location'] = Job_location[0:10]
Jobs_DataAnalyst['Company_Name'] = Comapany_name[0:10]
Jobs_DataAnalyst['Experience_required'] = Experience_required[0:10]


# In[31]:


Jobs_DataAnalyst


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from textblob import TextBlob


# In[2]:


df= pd.read_csv('netflix1.csv')


# In[3]:


df


# In[4]:


director_df = pd.DataFrame()
director_df['directors'] = df['director'].str.split(',', expand= True).stack()


# In[5]:


directors = director_df['directors'].value_counts().reset_index()
directors.columns= ['directors','total count']


# In[8]:


directors = directors[directors['directors'] != 'Not Given']


# In[9]:


directors = directors.sort_values(by= 'total count', ascending = False)


# In[12]:


top5director = directors.head()
barchart = px.bar(top5director,x = 'total count', y= 'directors', title = 'Top Directors on netflix')
barchart.show()


# # Pie Chart

# In[13]:


x= df.groupby(['rating']).size().reset_index(name = 'count')
print(x)


# In[16]:


piechart = px.pie(x, values = 'count', names = 'rating', title = 'Distribution of ratings on Netflix')
piechart.show()


# # Analyse the content produced on netflix based on years

# In[17]:


df1 = df[['type', 'release_year']]


# In[20]:


df1= df1.rename(columns= {"release_year":"Release Year", "type":"Type"})


# In[22]:


df2 = df1.groupby(['Release Year', 'Type']).size().reset_index(name = 'total count')


# In[25]:


df2= df2[df2['Release Year']>=2000]
graph = px.line(df2, x= 'Release Year', y= 'total count', color = 'Type', title = 'Trend Of Content Produced On Netflix Every Year')
graph.show()


# In[ ]:





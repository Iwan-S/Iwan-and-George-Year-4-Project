#!/usr/bin/env python
# coding: utf-8

# # Finding corrected parallax values
# ****

# In[1]:


import pandas as pd


# In[6]:


def ScreamExtractor(File):
    FILENAME = pd.read_csv(f'{File}', sep=' ')
    return FILENAME


# In[9]:


def Offset(Column='ZPCORR_PARALLAX_GAIA'):
    Directory = 'C:/Users/georg/Documents/GitHub'
    File = ScreamExtractor(f'{Directory}/get_gaia/results/sample.ascii')
    if Column == 'All':
        return File
    else:
        return File[Column]


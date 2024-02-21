#!/usr/bin/env python
# coding: utf-8

# # Gaussianness
# ****

# In[1]:


import corner
from dynesty import NestedSampler, utils
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


#%matplotlib notebook
π = np.pi
Colour = plt.style.use('tableau-colorblind10')


# In[12]:


def Model(x, p):
    
    return p

def logLikelihood(p, x):
    p = Model(x, p)
    μ1, σ1, μ2, σ2, Mix = p
    logPDF1 = norm.logpdf(x, loc=μ1, scale=σ1) + np.log(1-Mix)
    logPDF2 = norm.logpdf(x, loc=μ2, scale=σ2) + np.log(Mix)
    logPDF = np.logaddexp(logPDF1, logPDF2)
    
    return sum(logPDF)


# Busy life, moving on

# In[33]:

def UltraMagnus(u):
    x = np.array(u)
    x[0] = 1*x[0] + 1.5
    x[1] = 0.2*x[1] + 0.01
    x[2] = 1*x[2] + 1.5
    x[3] = 0.2*x[3] + 0.01
    
    return x

def Birdie(Data, Dimensions, Plots=False):
    Sampler = NestedSampler(logLikelihood, UltraMagnus, ndim=Dimensions, logl_args=[Data], nlive=2000)

    Sampler.run_nested()

    Results = Sampler.results
    
    Samples = Results.samples_equal()
    
    if Plots:
        corner.corner(Samples, labels=['Mean 1', 'Sigma 1', 'Mean 2', 'Sigma 2', 'Mixture']);

        ax = sns.histplot(Data, kde=True, stat='density')
        ax.axvline(μ[0], color='green', label='Mean')
        ax.axvline(μ[0]+σ[0], color='green', linestyle='--', label='$\pm$ σ', alpha=0.6)
        ax.axvline(μ[0]-σ[0], color='green', linestyle='--', alpha=0.6)

        ax.axvline(μ[1], color='red', label='Mean')
        ax.axvline(μ[1]+σ[1], color='red', linestyle='--', label='$\pm$σ', alpha=0.6)
        ax.axvline(μ[1]-σ[1], color='red', linestyle='--', alpha=0.6)

        Fuzz = np.linspace(-1, 13, No[1])
        for f in Samples[::10]:
            plt.plot(Fuzz, norm.pdf(Fuzz, f[0], f[1]), color='yellow', alpha=0.1)

        ax.legend()
    
    return Samples


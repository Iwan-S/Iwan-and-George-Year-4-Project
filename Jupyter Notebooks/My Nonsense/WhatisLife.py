#!/usr/bin/env python
# coding: utf-8

# # Gaussian Mixture Model

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[9]:


def Rotator(x, y, Centre, θ):
    π = np.pi
    x1 = x-Centre[0]
    y1 = y-Centre[1]
    Length = np.sqrt((x1)**2 + (y1)**2)
    α = []
    
    for a in range(len(Length)):
        Angle = np.arcsin(y1[a]/Length[a])
        if x1[a] > 0 and y1[a] > 0:
            α.append(Angle)
        elif x1[a] < 0 and y1[a] > 0:
            α.append(π-Angle)
        elif x1[a] < 0 and y1[a] < 0:
            α.append(π+np.abs(Angle))
        else:
            α.append(2*π-np.abs(Angle))
    
    β = np.array(α)-θ
    for b in range(len(β)):
        if β[b] < 0:
            β[b] += 2*π
    
    x2 = []
    y2 = []
    for c in range(len(Length)):
        Sign = 1
        if β[c] > π/2 and β[c] < 1.5*π:
            Sign = -1
        x2.append(Sign*Length[c]*np.abs(np.cos(β[c]))+2)
        y2.append(Length[c]*np.sin(β[c])+2)
    
    return x2, y2


# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 12:24:50 2021

@author: Eyan
"""

# There are two primary types of machine learning algorithms
# Classification algorithm and Regression algorithm
# Classification is used to predict a value based on the series of previous value
# In a form of possibility

import numpy as np
import torch
import torchvision
import math
import random

learning_rate = 1e-6

def predict_int(value_array):
    x = (max(value_array))
    y = (min(value_array))
    z = np.linspace(y,x,10).sum()
    z = z/10
    return z

a = {23, 23.2, 32.5, 15.7}
print(predict_int(a))

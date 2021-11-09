# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 12:24:50 2021

@author: Eyan
"""

# There are two primary types of machine learning algorithms
# Classification algorithm and Regression algorithm
# Regression is used to predict a discrete value based on the one upperbound and one underbound value
# In a form of integer (or float sometime)

import numpy as np
import torch
import torchvision
import math
import random

learning_rate = 1e-6

def predict_int(upperbound, underbound):
    z = np.linspace(underbound,upperbound,10).sum()
    z = z/10
    return z

a = 34
b = 12
print(predict_int(a,b))

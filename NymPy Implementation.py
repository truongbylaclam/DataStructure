# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:54:12 2021

@author: Eyan
"""

import numpy as np
import math

# Polynomial solving

# Square Polynomial solving function

x = np.linspace(2,7,num = 5)
y = np.sin(x)


print(x)
print(y)

y_two = np.square(x-y).sum()
print(y_two)

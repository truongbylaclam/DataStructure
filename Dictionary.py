# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:46:56 2021

@author: Eyan
"""

# Dictionary
# Holding data as key-value pairs is important especially in distributed algorithms. In
# Python, a collection of these key-value pairs is stored as a data structure called a dictionary.
# This is very simiar to Hash
bin_colors ={
 "manual_color": "Yellow",
 "approved_color": "Green",
 "refused_color": "Red"
 }
print(bin_colors)

# How to access the element with its key in Dictionary
print(bin_colors.get("approved_color"))
# Another way to do it
print(bin_colors["refused_color"])

# To update the element with the given key

bin_colors["manual_color"] = "Orange"
print(bin_colors["manual_color"])

# 

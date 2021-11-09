# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 21:03:44 2021

@author: Eyan
"""

# Sets
# A set is defined as a collection of elements that can be of different types.

dog = {'Tail', 'Furry', 3.0, "Loyal to their owner"}
cat = {'Tail', 'Furry', 1.0, "Playful and cute"}
print(dog)
print(dog|cat)
print(dog&cat)

Friend = {'Hangout', 'Hobby', 'Party', 'Adventure', 'Caring'}
Couple = {'Love', 'Affection', 'Date', 'Adventure', 'Caring', 'Wholesome'}
countryside = {'Peaceful', 'Quiet', 'Forest', True}
city = {'Chaotic', 'Burstling', 'Metro', False}

print(countryside|city)
print(Friend|Couple)

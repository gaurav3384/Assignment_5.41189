# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 22:16:21 2018

@author: gauravkgupta
"""

def moving_window_avg(input, window_size):
    res =[]
    for x in range(0, len(input)-window_size+1):
        sum = 0
        for y in range(x,x+window_size):
            sum += sum + input[y]
        res.append(sum/window_size)
    return res;

moving_window_avg([1,2,3,4,5,6,7,8,9,10],2)
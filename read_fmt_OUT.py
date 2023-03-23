#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 10:32:27 2023

@author: anandarupmukherjee
"""
import numpy as np


# FUNCTION TO FORMAT THE OUTPUTS 

def listify_dictionarify(arr_val, header):
    my_list=arr_val.split()
    new_list=my_list[-5:]
    merged="_".join(str(i) for i in my_list[:-5])
    new_list.insert(0,merged)
    my_dict = dict(zip(header, new_list))
        
    return my_dict




with open('2023-02-20_Overall_Process_AP.out', 'r') as file:
    # Read the lines and store them in a list
    lines = file.readlines()
    # Create a numpy array from the list of lines
    arr = np.array(lines)



header=arr[14].split()
tat=arr[17].split()


for i in range(18,54):
    print(listify_dictionarify(arr[i], header))
    print("--------------------------")









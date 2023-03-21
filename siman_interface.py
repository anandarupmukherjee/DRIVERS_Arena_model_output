# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:56:19 2023

@author: am2910
"""

import subprocess
import pandas as pd


software = r"C:\Program Files\Rockwell Software\Arena\siman.exe"
target_file = r"C:\Users\am2910\Desktop\Digital_hospitals_python\2023-02-20_Overall_Process_AP.p"

resp=subprocess.run([software,target_file], stdout=subprocess.PIPE)
resp.stdout

out=open('2023-02-20_Overall_Process_AP.out')
print(out.readlines())
out.close()

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:43:00 2019

@author: Henry_B
"""
import os
import shutil
def move_out_folders():
    path = "c:/work/sphere/data/lfw"
    for filepath,_,filenames in os.walk(path):
        for filename in filenames:
            with  open(os.path.join(filepath, filename), "rb") as f:
                x = f.read()
                with open(os.path.join(path, filename), "wb") as out:
                    out.write(x)
def remove_folders():                    
    path = "c:/work/sphere/data/lfw"
    for filepath,_,filenames in os.walk(path):
        print(filepath)
        if not path==filepath:
            shutil.rmtree(filepath)
remove_folders()
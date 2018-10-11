# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 13:36:16 2018

@author: Admin
"""
#Funktion der laver dynamisk gennemsnit
#Jeg er ikke heæt tilfreds med start og slut
import numpy as np

def dynm_genm(stien,genm):
    l = len(stien[0,:])
    for i in range(l):
        x = 0
        y = 0
        
        if i >= (len(stien[0,:])-genm):  #hvis det er et af de sidste tal, så erstattes de tomme tal med pmål.
            x = sum(stien[0,i:l]) + (genm+i-l)*(stien[0,l-1])
            y = sum(stien[1,i:l]) + (genm+i-l)*(stien[1,l-1])
    
        elif i < genm: #hvis det er et af de først tal, så erstattes de tomme tal med pstart.
            x = sum(stien[0,0:i]) + (genm-i)*(stien[0,0])
            y = sum(stien[1,0:i]) + (genm-i)*(stien[1,0])
    
        else:
            x = sum(stien[0,i:(i+genm)])
            y = sum(stien[1,i:(i+genm)])
            
        stien[0,i] = x/genm
        stien[1,i] = y/genm
    return (stien)
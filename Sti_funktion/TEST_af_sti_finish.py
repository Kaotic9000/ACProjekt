# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 13:32:36 2018

@author: Admin
"""

#test af sti
import numpy as np
import matplotlib.pyplot as plt
from sti_finish import sti #tager input sti(pstart,pmål,leng,fac)
from dynamisk_gennemsnit import dynm_genm #tager input dynm_genm(array der har 2 dim, genm)

genm = 4   #8
leng1 = 200  # længden af test vektoren
fac1 = 3  # Upløftet i en fraktor... gør udsving størrer
start = np.array([10,4])
mål = np.array([30,20])




wat = sti(start,mål,leng1,fac1)
wat1 = dynm_genm(wat,genm)


plt.plot(wat[0,:],wat[1,:],'r',start[0],start[1],'*',mål[0],mål[1],'*')

plt.plot(wat1[0,:],wat1[1,:],'r',start[0],start[1],'*',mål[0],mål[1],'*')
plt.ylabel('wat')
plt.show()


print("Teoretisk start og slut")
print(start,mål)
print("Udregnet start slut")
print(wat1[0,0],wat1[1,0],wat1[0,len(wat[0,:])-1],wat1[1,len(wat[0,:])-1])

#Jeg er ikke helt tilfred med midlingen, den laver lidt for lineære start og slut...
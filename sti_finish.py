# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:31:15 2018

@author: Admin
"""
import numpy as np
def sti(pstart,pmål,leng,fac):
    #lAVER EN TEST VECTOR der starter i (0,0)!!!!!!
    stien = np.array([np.zeros(leng),np.zeros(leng)])
    stien1 = np.array([np.random.rand(leng)**fac,np.random.rand(leng)**fac]) # en random testvektore
    for i in range(len(stien1[0,:])):# den bliver accumuleret
        if i == 0:
            stien1[0,0] = 0
            stien1[1,0] = 0
        else:
            stien1[:,i] = stien1[:,i-1] + stien1[:,i]
    ######
    l_sti = len(stien1[1,:])-1
    skal_ned = np.sqrt(stien1[0,l_sti]**2+stien1[1,l_sti]**2)
    stien1 = stien1/skal_ned
          
          
    ø_ran = np.arctan((stien1[1,l_sti]-stien1[1,0])/(stien1[0,l_sti]-stien1[0,0])) # den random vectors vinkel
   #########################
    
    ø_lin = np.arctan((pmål[1]-pstart[1])/(pmål[0]-pstart[0]))
    l_lin = np.sqrt((pmål[1]-pstart[1])**2+(pmål[0]-pstart[0])**2)
    
    dø = ø_lin - ø_ran
    #rotation
    if pmål[0]<pstart[0]: #Ved ikke hvorfor rotationen ikke bare fungere, men er nødt til at have foskellige scenarier
        stien[0,:] = (l_lin) * (stien1[0,:]*np.cos(dø) - stien1[1,:]*np.sin(dø)) + pmål[0]
        stien[1,:] = (l_lin) * (stien1[0,:]*np.sin(dø) + stien1[1,:]*np.cos(dø)) + pmål[1]
    else:
        stien[0,:] = (l_lin) * (stien1[0,:]*np.cos(dø) - stien1[1,:]*np.sin(dø)) + pstart[0]
        stien[1,:] = (l_lin) * (stien1[0,:]*np.sin(dø) + stien1[1,:]*np.cos(dø)) + pstart[1]        
    
    #print(stien[0,0],stien[1,0],stien[0,l_sti],stien[1,l_sti])
    #plt.plot(stien1[0,:],stien1[1,:])
    #plt.show()

    return (stien)

#########################################################

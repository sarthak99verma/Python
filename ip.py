# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:38:51 2019

@author: Asus
"""

data=open('D:/python/modules-cloud-master/week1/abc.log').readlines()
blocked=['wwe','twitter','facebook']
for entry in data:
    var =entry.split('::')
    if var[-1].split('.')[1] in blocked:
            print ('ip-->',var[3],'      user:',var[1],'     using-->',var[-1].split('.')[1])

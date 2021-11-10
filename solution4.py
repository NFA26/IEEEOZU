# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 16:57:30 2021

@author: NFA26
"""


def position(a,b):
    grid=[]
    
    for i in range(8):         
        for j in range(8):
            grid.append((i,j))    
    
    posible_locations=[(a-2,b-1),(a-2,b+1),(a+2,b-1),(a+2,b+1),
                       (a-1,b+2),(a-1,b-2),(a+1,b-2),(a+1,b+2)]    
        
    real_locations=[]
    
    for k in posible_locations:       
        if k in grid:
            real_locations.append(k)
        
    return real_locations

print(position(2, 2))
print(position(0, 0))
print(position(3, 4))
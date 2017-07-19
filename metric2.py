# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 20:51:07 2017

@author: Madhura Kashikar
"""

import re


data=[]
list1=[]

insert=[]
delete=[]
ins=[]
delt=[]


with open('C:/Users/Madhura Kashikar/Desktop/file2.txt','r') as f:
    for line in f:
         if re.match('[a-z0-9]+', line) is not None:
             data=line.split()
             if len(data[0]) < 7:   #because 7 is the shortest for git hash that can ever be
             
                 list1.append(data)



print("\n", list1)



for item in range(len(list1)):
    if list1[item][2] == 'README.md' or list1[item][2]=='README.md~':
        ins.append(list1[item][0])
        delt.append(list1[item][1])
    else:
        insert.append(list1[item][0])
        delete.append(list1[item][1])
        
        
#==============================================================================
# print(ins)
# 
# print(delt)
#  
# print(insert)
# 
# print(delete)  
#==============================================================================

lines_inserted=0 
read_del=0
read_inserted=0
lines_deleted=0


    
for ele in range(len(ins)):
    #k=int(ins[ele])
    read_inserted= read_inserted+ int(ins[ele])
for i in range(len(delt)):
    read_del= read_del + int(delt[i])
    
for j in range(len(insert)):
    lines_inserted=lines_inserted+ int(insert[j])
    
for l in range(len(delete)):
    lines_deleted=lines_deleted + int(delete[l])
        
total_lines_inserted= lines_inserted - read_inserted 

total_lines_removed= lines_deleted - read_del

print("Total inserted lines by author are", total_lines_inserted)

print("Total lines removed by author are", total_lines_removed)


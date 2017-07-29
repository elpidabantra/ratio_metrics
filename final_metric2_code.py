# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 09:37:41 2017

@author: Madhura Kashikar
"""
from collections import Counter




data=[]
insert=0
deleted=0
k=[]
author=[]
ins_count=0
del_count=0
insert_count=[]
delete_count=[]
icounts=[author,insert_count]
dcounts=[author,delete_count]
counti=0
countd=0




with open('C:/Users/Madhura Kashikar/Desktop/gitlog5.txt','r') as f:
    for line in f:
         if "Author:" in line:
             data=line.split()
             term=data[-1]
             #print("\n author name",term)
             
             
         if "README.md" in line:
             k=line.split()
             string=k[-1]
             insert=string.count('+')
             deleted=string.count('-')
         else:
             insert=0
             deleted=0
             
         if ".py" in line:
             ln=line.split()
             #print(ln)
             strng=ln[-1]
             ins_count=strng.count('+')
             del_count=strng.count('-')
         else:
             ins_count=0
             del_count=0
          
         counti=ins_count-insert
         countd=del_count-deleted
         
         if not author and not insert_count:
             author.append(term)
             insert_count.append(counti)
             delete_count.append(countd)
             #print(author)
             #print(insert_count)
         elif term not in author:
             author.append(term)
             insert_count.append(counti)
             delete_count.append(countd)
         elif term in author:
             loc=author.index(term)
             insert_count[loc]= counti+ insert_count[loc]
             delete_count[loc]=countd+delete_count[loc]
             
             
         
dictoi=dict(zip(author, insert_count)) 
#print(dictoi)
#print(author,delete_count)
dictod=dict(zip(author, delete_count))
#print(dictod)          
         
count1= Counter(dictoi)

count2=Counter(dictod)


count1=dict(count1)
count2=dict(count2)             
           

a = {k: v / total for total in (sum(count1.values()),) for k, v in count1.items()}
b={l: m / total for total in (sum(count2.values()),) for l, m in count2.items()}    

print("\n The ratio of number of lines inserted: \t", a)
print("\n The ratio of number of lines deleted \t",b)
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 14:15:23 2017

@author: Madhura Kashikar
"""


import pygit2
import re
import string
import pygit2
import subprocess
import re
from collections import Counter
import pandas as pd
#import subprocess

    
repo = pygit2.Repository('C:/Users/Madhura Kashikar/Desktop/Trial/Python')
print(repo.path)
print(repo.workdir)

print("\n")

commit = repo[repo.head.target]
name_a=[]
commit_list=[]
last = repo[repo.head.target]
emaila=[]
email_u=[]
data=[]
email=[]
cid=[]
author=[]
author_name=[]


for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
    
    author_name.append(commit.author.name) #get the commit author name
    emaila.append(commit.author.email) #get the commit author email
    name_a = list(set(author_name)) #create a new list containing only unique author names
    commit_list.append(commit.tree_id.hex)#commit ids
    email_u=list(set(emaila))#list containing unique email ids
 
#create a data frame for all the data obtained

log_list = pd.DataFrame(
    {'author name': author_name,
     'email id': emaila,
     'commit id': commit_list
    })
    
function_written=[]
function_edited=[]
author_edit=[]
author_write=[]
#in order to calculate metrics for eac hauthor we need the pacthes with author names

#==============================================================================
#iterate the list and data frame reversly so as to print the patch from first commit first

#===The below written code generates the text file for the diff===========================================================================
#==============================================================================
for index, row in log_list[::-1].iterrows():
       item=row['email id']
       for emailid in email_u:
           if emailid == item:
               commit_id=row['commit id']
               diff=repo.diff(commit_id)
               with open("finalgitdiffpatchforpythonrepository2.txt", "a") as f:
                  # print("\n author name",row['author name'],file=f)
                   print("\n commit id",row['commit id'], file=f)
                   print("\n emailid",row['email id'],file=f)
                   print("\n",diff.patch,file=f) #generates diff pacth from the diff object obtained from pygit2 and this output is saved in text file, otherwise it takes too long to save it in memory.
                   print("\n **********************************************************************NEW DIFF ********************************************************",file=f)
 
#==============================================================================
#the below written code produces the ratio

#==============================================================================
class_written=[]
class_edited=[]
author_clsse=[]
author_clssw=[]
with open('finalgitdiffpatchforpythonrepository2.txt','r') as f:
#     
     for line in f:
         if 'emailid' in line:
             k=line.split()
             
             email.append(k[-1])
#         
         if "+def" in line:
             sent=line.split()
             func=sent[1]
             if func in function_written:
                 function_edited.append(func)
                 author_edit.append(k[-1])
                 #print("\n The functions edited are::",function_edited)
             else:
                 function_written.append(func)
                 author_write.append(k[-1])
                 #print("the functions written are::", function_written)
         elif "+class" in line:
             
             sentence=line.split()
             clss=sentence[1]
             if clss in class_written:
                 class_edited.append(clss)
                 author_clsse.append(k[-1])
             else:
                 class_written.append(clss)
                 author_clssw.append(k[-1])
             
count1= Counter(author_write)
 
count2=Counter(author_edit)
 
count3=Counter(author_clssw)
count4=Counter(author_clsse)
# 
# 
# 
# 
count1=dict(count1)
count2=dict(count2)
count3=dict(count3)
count4=dict(count4)
# 
# 
a = {k: v / total for total in (sum(count1.values()),) for k, v in count1.items()}
b={l: m / total for total in (sum(count2.values()),) for l, m in count2.items()}
# 
c = {r: s / total for total in (sum(count1.values()),) for r, s in count3.items()}
d={u: q / total for total in (sum(count2.values()),) for u, q in count4.items()}
# 
print("\n The ratio for each author in terms of functions written is:\n \t",a)
# 
print("\n The ratio for each author in terms of functions edited is:\n \t",b)
# 
print("\n The ratio for each author in terms of class written is:\n \t",c)
#
print("\n The ratio for each author in terms of class edited is:\n \t",d)           
#             
# 
# # keys_author = {}
# # for i, v in enumerate(email_u):
# #     
# #         keys_author[v]=i
# #     
# #         
# # print(keys_author)        
# 
# 
# 
#==============================================================================

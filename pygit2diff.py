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


repo = pygit2.Repository('C:/Users/Madhura Kashikar/Desktop/Trial/tacotron')
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

#in order to calculate metrics for eac hauthor we need the pacthes with author names

#==============================================================================
#iterate the list and data frame reversly so as to print the patch from first commit first

for index, row in log_list[::-1].iterrows():
     item=row['email id']
     for emailid in email_u:
         if emailid == item:
             commit_id=row['commit id']
             diff=repo.diff(commit_id)
             with open("finalgitdiffpatch.txt", "a") as f:
                 print("\n author name",row['author name'],file=f)
                 print("\n commit id",row['commit id'], file=f)
                 print("\n emailid",row['email id'],file=f)
                 print("\n",diff.patch,file=f) #generates diff pacth from the diff object obtained from pygit2 and this output is saved in text file, otherwise it takes too long to save it in memory.
                 print("\n **********************************************************************NEW DIFF ********************************************************",file=f)
                 
#==============================================================================
            
keys_author = {}
for i, v in enumerate(email_u):
    
        keys_author[v]=i
    
        
print(keys_author)        

#write code to match keys
#write code for the metric

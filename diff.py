# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 23:00:49 2017

@author: Madhura Kashikar
"""

import pygit2
import re
import string
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


for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
    
    name_a.append(commit.author.name)
    emaila.append(commit.author.email)
    name_a = list(set(name_a))
    commit_list.append(commit.tree_id.hex)
    email_u=list(set(emaila))
    



# for x, y in zip(commit_list, commit_list[1:]):
#     diff=repo.diff(x,y)
#     patches=[p for p in diff]
#     print("\n \t",patches)
#     print("\n \t",diff.patch)

    
for x in commit_list:
    diff=repo.diff(x)
    textdata=diff.patch #this line gives us patch of the code. We need to parse this textData.
    print("\n the data type of diff is:", type(textdata))


   
  
    
    
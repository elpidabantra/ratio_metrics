# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 23:21:02 2017

@author: Madhura Kashikar
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 23:10:38 2017

@author: Madhura Kashikar
"""

import pygit2
import subprocess


repo = pygit2.Repository('C:/Users/Madhura Kashikar/Desktop/Trial/tacotron/')
print(repo.path)
print(repo.workdir)

print("\n")

commit = repo[repo.head.target]
name_a=[]
commit_list=[]
last = repo[repo.head.target]




for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
    
    name_a.append(commit.author.name)
    print(name_a)
    name_a = list(set(name_a))
    commit_list.append(commit.tree_id.hex)

num=len(name_a)
print("The num is",num)

num1=len(commit_list)
print(num1) 

#name="ryan"


print("\n")
print("\n The authors for the repository are::",name_a)

#==============================================================================
for i in range(num):    
     print(name_a[i])
    
     subprocess.Popen("git log  --author=%s --numstat --oneline" %name_a[i] ,shell='True',cwd='C:/Users/Madhura Kashikar/Desktop/Trial/tacotron/',stdout=open('C:/Users/Madhura Kashikar/Desktop/gitlog10.txt','w'))
    
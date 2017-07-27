

# -*- coding: utf-8 -*-

"""
Created on Wed Jul 26 13:18:20 2017
@author: Elpida Bantra
"""

import pygit2
import re
import string
import pygit2
import subprocess
import re
from collections import Counter
import pandas as pd
import sys
import os
import tokenize
import io



    
repo = pygit2.Repository('/Users/elpidabantra/Desktop/quilt')
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



imported_items = []


for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
    
    author_name.append(commit.author.name) #get the commit author name
    emaila.append(commit.author.email) #get the commit author email
    name_a = list(set(author_name)) #create a new list containing only unique author names
    commit_list.append(commit.tree_id.hex)#commit ids
    email_u=list(set(emaila))#list containing unique email ids


log_list = pd.DataFrame(
    {'author name': author_name,
     'email id': emaila,
     'commit id': commit_list
    })
    
function_written=[]
function_edited=[]
import_written=[]
import_edited=[]
author_edit=[]
author_write=[]

class_written=[]
class_edited=[]
author_clsse=[]
author_clssw=[]

author_imp_edited = []
author_imp_write=[]


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
 

denominator_ratio1 = 0

numerator_list1 = []

denominator_ratio3 = 0

numerator_list3 = []

list_of_authors = []



for word in author_name:
  if word not in list_of_authors:
    list_of_authors.append(word)








with open('finalgitdiffpatchforpythonrepository2.txt','r') as f:
  for line in f:  
         if 'emailid' in line:
             k=line.split()
             
             email.append(k[-1])   
         if "+import " in line:
             sen=line.split()
             imp=sen[1]
             if imp in import_written:
                 import_edited.append(imp)
                 author_imp_edited.append(k[-1])

             else:
                 import_written.append(imp)
                 author_imp_write.append(k[-1])

         if "+def" in line:

             sent=line.split()
             func=sent[1]
             if func in function_written:
                 function_edited.append(func)
                 author_edit.append(k[-1])
             else:
                 function_written.append(func)
                 author_write.append(k[-1])

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

count5=Counter(author_imp_write)
count6=Counter(author_imp_edited)



count1=dict(count1)
count2=dict(count2)
count3=dict(count3)
count4=dict(count4)

count5=dict(count5)
count6=dict(count6)



ff3 = open("ratios_metric1-3.txt", 'w')

sys.stdout = ff3


a = {k: v / total for total in (sum(count2.values()),) for k, v in count2.items()}

b={l: m / total for total in (sum(count4.values()),) for l, m in count4.items()}

c = {r: s / total for total in (sum(count6.values()),) for r, s in count6.items()}

d={u: q / total for total in (sum(count1.values()),) for u, q in count1.items()}

e = {r: s / total for total in (sum(count3.values()),) for r, s in count3.items()}

f={u: q / total for total in (sum(count5.values()),) for u, q in count5.items()}
# 
print("\n The ratio of in total functions used by each contributor is:\n \t",a)
# 
print("\n The ratio of in total functions used by each contributor is:\n \t",b)
# 
print("\n The ratio of in total functions used by each contributor is::\n \t",c)
#
print("\n The ratio of different functions wriiten by each contributor is:\n \t",a)
# 
print("\n The ratio of different classes wriiten by each contributor is:\n \t",b)
# 
print("\n The ratio of different imports by each contributor is::\n \t",c)
     



ff3.close()



  

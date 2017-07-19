# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 13:41:52 2017

@author: Madhura Kashikar
"""


import pygit2
import subprocess
import re
from collections import Counter


 

repo = pygit2.Repository('C:/Users/Madhura Kashikar/Desktop/Trial/ZeroNet')
print(repo.path)
print(repo.workdir)

print("\n")

commit = repo[repo.head.target]
name_a=[]
commit_list=[]
last = repo[repo.head.target]
email_id=[]



for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
    
    name_a.append(commit.author.name)
    #print(name_a)
    name_a = list(set(name_a))
    commit_list.append(commit.tree_id.hex)
    email_id.append(commit.author.email)
    email_id=list(set(email_id))

num=len(name_a)
#print(num)
print(email_id)
num1=len(commit_list)
#print(num1) 
print(len(email_id))


print("\n")
#print("\n The authors for the repository are::",name_a)


#subprocess.Popen("git log",cwd='C:/Users/Madhura Kashikar/Desktop/Trial/ZeroNet',shell='False',stdout=open('C:/Users/Madhura Kashikar/Desktop/metric4test.txt','w'))

k=[]
a=[]
author=[]
email=[]
cid=[]  

data=[]
author_edit=[]
author_write=[]
temp=[]
function_written=[]
function_edited=[]
sent=[]
author_name=[]
  
with open('C:/Users/Madhura Kashikar/Desktop/metric4test.txt','r',encoding="utf8") as f:
    
    for line in f:
         if re.match('^commit', line) is not None:
             a=line.split()
             cid.append(a[1])
                
         if re.match('^Author',line) is not None:
            k=line.split()
            author.append(k[1])
            email.append(k[-1])
            


#==============================================================================
# for i in reversed(range(len(cid))):
# #     
#     subprocess.Popen("git show %s" %cid[i],cwd='C:/Users/Madhura Kashikar/Desktop/Trial/ZeroNet',shell='False',stdout=open('C:/Users/Madhura Kashikar/Desktop/testdoc1.txt','a'))
# # 
#==============================================================================
#==============================================================================

with open('C:/Users/Madhura Kashikar/Desktop/testdoc1.txt','r',encoding="ISO-8859-1") as f:
    
    for line in f:
        if re.match('^Author', line) is not None:
             data=line.split()                     
             author_name.append(data[-1])
             
             
                     #print(data[1:len(data)])
        elif "+def" in line:
            sent=line.split()
            func=sent[1]
            if func in function_written:
                function_edited.append(func)
                author_edit.append(data[-1])
                #print("\n The functions edited are::",function_edited)
            else:
                function_written.append(func)
                author_write.append(data[-1])
                #print("the functions written are::", function_written)
                
                



count1= Counter(author_write)

count2=Counter(author_edit)


count1=dict(count1)
count2=dict(count2)
Rofw={}

a = {k: v / total for total in (sum(count1.values()),) for k, v in count1.items()}
b={l: m / total for total in (sum(count2.values()),) for l, m in count2.items()}

print("\n The ratio for each author in terms of functions written is:\n \t",a)

print("\n The ratio for each author in terms of functions edited is:\n \t",b)


f = open("C:/Users/Madhura Kashikar/Desktop/blah.txt", "w")
   
subprocess.Popen("git shortlog -s -n",cwd='C:/Users/Madhura Kashikar/Desktop/Trial/ZeroNet/',stdout=open('C:/Users/Madhura Kashikar/Desktop/coms.txt','w'))             

#==============================================================================
# #==============================================================================
# # 
# while p.poll() is not  None:
#      l = p.stdout.readline() # This blocks until it receives a newline.
#      print (l.split('\t'))
# # # When the subprocess terminates there might be unconsumed output 
# # # that still needs to be processed.
# # #z= p.stdout.read().decode('ascii')
# z= p.stdout.read().strip().split()
# print(z)
#==============================================================================
#==============================================================================


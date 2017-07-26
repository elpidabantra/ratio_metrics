
# -*- coding: utf-8 -*-

"""
Created on Wed Jul 26 13:18:20 2017
@author: Elpida Bantra
"""

import sys
import pygit2
import re
import string
import subprocess
import os
import pandas as pd
import tokenize
import io
from collections import Counter



# the first thing that we have to do is to print in a file with the name
# commit_details.txt the repository details: the names of the authors by 
# commenting order and the number of the corresponing commit, we just have 
# to give the name of the repository that we 
# want to examine in the line 19


repository_path = '/Users/elpidabantra/Desktop/tacotron'

fc = open("commit_details.txt", 'w')
sys.stdout = fc


repo = pygit2.Repository(repository_path)


kr = subprocess.Popen('git log --author --oneline --shortstat',shell='False') #can be used to run the commandline command
print(kr)
commit = repo[repo.head.target]
commit.message

last = repo[repo.head.target]
for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
    print("The commit message is",commit.message)
    print(commit.commit_time)
    print("Committed by",commit.author.name, commit.author.email)
    print("\n")



fc.close()



# the next step of our code is to write a file with name 
# commit_by_author.txt, which includes only the names of the authors by
# commiting order  







fc = open("commit_by_author.txt", 'w')
sys.stdout = fc


repo = pygit2.Repository(repository_path)

kr = subprocess.Popen('git log --author --oneline --shortstat',shell='False') #can be used to run the commandline command
commit = repo[repo.head.target]
commit.message

last = repo[repo.head.target]


for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
    print(commit.author.name)


fc.close()

# the next step of our code is to write a file noa (number_of_authors)
# and print there the list of authors and the length of this list



fn = open("number_of_authors.txt", 'w')
sys.stdout = fn


list_of_authors = []




with open('commit_by_author.txt') as f:
	for word in f:
		if word not in list_of_authors:
			list_of_authors.append(word)

for i in list_of_authors:
	print(i)

print(list_of_authors)


f.close()


fn.close()



# After this we open the initial commit details file and
# with text analysis we create a file with name commits_number_by_order.txt
# in which are included two lists. The first one gives the numbers of the commits
# and the second one the corresponding authors.
# now we want to create equal to the numer of the authors lists and fill 
# them with the commit numbers of the author




list_of_contributors = []
list_of_commits = []

document_text = open('commit_details.txt', 'r')
text_string = document_text.read().lower()
text_string = str(text_string)
match_pattern1 = re.findall(r'\b[0-9A-Fa-f]{10,12}\b', text_string)
match_pattern2 = re.findall(r'\b[a-z]{10,12}\b', text_string)
counter = 0
words = text_string.split()
for i,w in enumerate(words):
    if w == "committed":
        list_of_contributors.append(words[i+2])


for word in match_pattern1:
    list_of_commits.append(word)
    counter = counter +1
document_text.close()

f1 = open("commits_number_by_order.txt", 'w')
sys.stdout = f1  

print(list_of_commits)
print(list_of_contributors)

        
f1.close()











####################################     ##########################


# function to remove the comments from the source code files in order to do
# text analysis on them


"""
def remove_all_comments(text_string):
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    io_obj = io.StringIO(text_string)
    out = ""
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        ltext = tok[4]
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        if token_type == tokenize.COMMENT:
            pass
        elif token_type == tokenize.STRING:
            if prev_toktype != tokenize.INDENT:
                if prev_toktype != tokenize.NEWLINE:
                    if start_col > 0:
                        out += token_string
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    return out
"""

f13test = open("testaki.txt", 'w')
sys.stdout = f13test

print(list_of_authors)

f13test.close()





repo = pygit2.Repository(repository_path)
commit_list=[]
last = repo[repo.head.target]

f1 = open("lists_of_commit_numbers.txt", 'w')
sys.stdout = f1

for kk in range(0,len(list_of_authors)):
	count = 0

	with open('commit_by_author.txt') as f2:
		list_of_commits_numbers = []
		for word in f2:
			count += 1
			if word == list_of_authors[kk]:
				list_of_commits_numbers.append(count)
		#print(list_of_authors[kk])
		#print(list_of_commits_numbers)
		for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
			commit_list.append(commit.tree_id.hex)
		for i in list_of_commits_numbers:
			subprocess.Popen('git diff HEAD %s' %commit_list[i-1],shell='True',cwd=repository_path,stdout=open(str(list_of_authors[kk])+".txt", 'w'))
			#f3 = open(str(list_of_authors[kk])+"_without_comments.txt", 'w')
			#sys.stdout = f3
			#document_text = open(str(list_of_authors[kk])+".txt", 'r')
			#text_string = str(document_text.read().lower())
			#print(remove_all_comments(text_string))



	f2.close()


			

#f3.close()


			

f1.close()




########## TEXT ANALYSIS #######

denominator_ratio1 = 0

numerator_list1 = []

denominator_ratio3 = 0

numerator_list3 = []


for kk in range(0,len(list_of_authors)):

	author = str(list_of_authors[kk])

	

	list_of_functions = []
	list_of_classes = []
	imported_items=[]

	count_imports = {}
	count_different_imports = {}
	count_functions = {}
	count_different_functions = {}
	count_classes = {}
	count_different_classes = {}

	count_imports[author] = 0
	count_functions[author] = 0
	count_different_functions[author] = 0
	count_classes[author] = 0
	count_different_classes[author] = 0
	count_different_imports[author] = 0





	with open(str(list_of_authors[kk])+".txt", 'r') as ft:

		for line in ft:
			line = str(line)
			if "+def " in line:
				if line.split("def") in list_of_functions:
					count_functions[author] = count_functions[author] + 1
				else:
					count_functions[author] = count_functions[author] + 1
					count_different_functions[author] = count_different_functions[author] + 1
					list_of_functions.append(line.split("def"))
			if "+class " in line:
				if line.split("class") in list_of_classes:
					count_classes[author] = count_classes[author] + 1
				else:
					list_of_classes.append(line.split("class"))
					count_classes[author] = count_classes[author] + 1
					count_different_classes[author] = count_different_classes[author] + 1

	

	with open(str(list_of_authors[kk])+".txt", 'r') as document_text:
		text_string = str(document_text.read().lower())
		words = text_string.split()
		for i,w in enumerate(words):
			if w == "+from " or w=="+import ":
				if words[i+1] in imported_items:
					count_imports[author] = count_imports[author] + 1
				else:
					imported_items.append(words[i+1])
					count_imports[author] = count_imports[author] + 1
					count_different_imports[author] = count_different_imports[author] + 1

	

	ff = open(str(list_of_authors[kk])+"source_code_analysis1.txt", 'w')
	sys.stdout = ff




	print("the number of functions for the given author is given in the below line")
	print(count_functions[author])
			#print("the functions that he wrote are given in the list below")
			#print(list_of_functions)
	print("the number of imports by the given author is given in the below line")
	print(count_imports[author])
			#print("the imported items are given below")
			#print(imported_items)
	print("the number of classes by the given author is given in the below line")
	print(count_classes[author])
			#print("the names of the classes are given below")
			#print(list_of_classes)

	print("the total numerator of this ratio is")
	print(int(count_functions[author])+int(count_imports[author])+int(count_classes[author]))

	numerator_list1.append(int(count_functions[author])+int(count_imports[author])+int(count_classes[author]))
	denominator_ratio1 = denominator_ratio1 + int(count_functions[author])+int(count_imports[author])+int(count_classes[author])
	

	ff.close()



	ff3 = open(str(list_of_authors[kk])+"source_code_analysis3.txt", 'w')
	sys.stdout = ff3


	print("the number of functions for the given author is given in the below line")
	print(count_different_functions[author])
	print("the functions that he wrote are given in the list below")
	print(list_of_functions)
	print("the number of imports by the given author is given in the below line")
	print(count_different_imports[author])
	print("the imported items are given below")
	print(imported_items)
	print("the number of classes by the given author is given in the below line")
	print(count_different_classes[author])
	print("the names of the classes are given below")
	print(list_of_classes)
	print("the total numerator of this ratio is")
	print(int(count_different_functions[author])+int(count_different_imports[author])+int(count_different_classes[author]))

	numerator_list3.append(int(count_different_functions[author])+int(count_different_imports[author])+int(count_different_classes[author]))
	denominator_ratio3 = denominator_ratio3 + int(count_different_functions[author])+int(count_different_imports[author])+int(count_different_classes[author])
	

	ff3.close()




ff = open("metric1_ratios.txt", 'w')
sys.stdout = ff


for i in range(0,len(numerator_list1)):
	print(list_of_authors[i])
	print(numerator_list1[i]/denominator_ratio1)

ff.close()


ff = open("metric3_ratios.txt", 'w')
sys.stdout = ff


for i in range(0,len(numerator_list3)):
	print(list_of_authors[i])
	print(numerator_list3[i]/denominator_ratio3)
ff.close()









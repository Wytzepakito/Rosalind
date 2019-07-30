#! /usr/bin/python37
"""
Author: Wytze Gelderloos
Date: 30-7-2019
Overlap Graphs
This function takes a list of DNA sequences and outputs an adjacency list
All overlap between the ends of DNA sequences can only occur once.
"""


file = open("rosalind_grph.txt", "r")
string = file.read()
string_list= string.split(">")

string_list.pop(0)

## reading the string obtained from file into a list of lists
superstring_list=[]
for string in string_list:
    all_str = string.split("\n")
    superstring = "".join(all_str[1:])
    superstring_list.append([all_str[0],superstring])
## formatting that list of lists into a dictionary
string_dic = {}
for item in superstring_list:
    string_dic[item[0]] = [item[1]]
## iteraing through the dic two times
for key,values in string_dic.items():
    for key2, values2 in string_dic.items():
        if key != key2 and len(values) >= 1 and len(values2) >= 1:
            ## if the start of the dictionary is equal to the end of another
            if values[0][:3]== values2[0][-3:]:
                ## print
                print(key2, key)
                
    
print(string_dic)


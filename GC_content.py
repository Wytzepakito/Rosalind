#! /usr/bin/python37
"""
Author: Wytze Gelderloos
Date: 29-7-2019
GC content
This script reads a few fasta entries from file and prints out the name of the
entry with the highest GC-content with its percentage GC content.
"""


file = open("Rosalind_gc.txt", "r")
string = file.read()
string_list= string.split(">")

string_list.pop(0)

superstring_list=[]
for string in string_list:
    all_str = string.split("\n")
    superstring = "".join(all_str[1:])
    superstring_list.append([all_str[0],superstring])

GC_list=[]
for string in superstring_list:
    print(string[0])
    G_con= string[1].count("G")
    C_con= string[1].count("C")
    GC_con = (G_con+C_con)/len(string[1])
    GC_list.append(GC_con*100)


print(string_list[GC_list.index(max(GC_list))].split("\n")[0])
print(max(GC_list))




"""
Author: Wytze Gelderloos
Date:

"""

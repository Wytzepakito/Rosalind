"""
Author: Wytze Gelderloos
Date: 30-7-2019
RNA secondary structure

"""

import math

string = """
>Rosalind_1779
GCGGAUAUUGAGCUCGCGGAUGUUCUCGUUCGCACCACGGCUGAAGAAUACACACUGCACACGUAUAGGGUCCUAUGCGC
"""

dic_comp = {"A" : "U", "U" : "A", "G": "C", "C" : "G"}

string_list =  string.split("\n")
string_list.remove("")

seq = string_list[1]

G_count = 0
C_count = 0
A_count = 0
U_count = 0

for i in seq:
    if i == "G":
        G_count += 1
    if i == "C":
        C_count += 1
    if i == "A":
        A_count += 1
    if i == "U":
        U_count += 1
supernum = 1
for i in range(1, C_count+1):
    supernum = supernum*i
supernum2 = 1
for i in range(1, A_count+1):
    supernum2 = supernum2*i
super_num = math.factorial(C_count)
super_num2 = math.factorial(A_count)

super_func = super_num * super_num2

super_coded = supernum * supernum2

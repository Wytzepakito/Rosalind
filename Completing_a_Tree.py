#! /usr/bin/python37
"""
Author: Wytze Gelderloos
29-7-2019
Completing a Tree
The main realization which is needed for this exercise is that the shortest
tree with n nodes and no cycles has n- 1 edges. Thus the only thing that is
necessary is to subtract the edges already there from the nodes in the tree
and you are left with the edges needed to make the smallest tree + 1 .
"""



file = open("Rosalind_pmch.txt", "r")
string = file.read()
branches = string.split("\n")
count = branches[0]
branches.remove(count)
branches.remove("")
print(branches)
count = int(count)


answer = count - len(branches) - 1

print("The answer to this exercise is {}".format(answer))

    

    

            
        
    
            

#! /usr/bin/python37
"""
Author: Wytze Gelderloos
Date: 29-7-2019
Calculating expected offspring.
This script calculates the expected number of offspring having the dominant
phenotype. Looking to Mendel's diagrams will give the proper answer for this
question.
"""

string= "18852 19128 19528 18742 17855 19195"



numbers = list(map(int,string.split(" ")))

new_pop=0

new_pop += numbers[0]*2
new_pop += numbers[1]*2
new_pop += numbers[2]*2
new_pop += numbers[3]*2*0.75
new_pop += numbers[4]*2*0.5
new_pop += numbers[5]*2*0



print(new_pop)

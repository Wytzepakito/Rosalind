"""
Author: Wytze Gelderloos
Date: 30-7-2019
Recurrence relationship
This script basicly does the Fibonacci sequence with each number increasing
with 2 instead of 1.
"""


def recurrence(n,k):
    no1 = 1
    no2 = 1
    listnos= []
    for i in range(n-2):
        newno = no1*k+no2
        listnos.append(newno)
        no1 = no2
        no2 = newno
    return listnos
        
        
        
        
sum_list = recurrence(35,2)

print(sum_list)





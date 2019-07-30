#! /usr/bin/python37
"""
Author: Wytze Gelderloos
Date: 29-7-2019
Partial permutations
The main realization for this problem is that if we would list all
permutations of a set of 7 it would be 7!. Thus if we would need to
choose 7 from 84 options we'll have 77 options to choose from in the
final pick.
This is the following formula n!/((n-k)!).

"""
import math

n = 84

k = 9
partial_perms = math.factorial(n)/ math.factorial(n-k)
mod_mil = partial_perms % 1000000

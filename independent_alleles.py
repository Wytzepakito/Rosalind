#! /usr/bin/python37
"""
Author: Wytze Gelderloos
Date: 29-7-2019
Independent alleles

"""

from scipy.stats import binom

k = 5

p = 0.25
n = 2 ** k
thresh = 9

print(n)
print((1-binom.cdf(thresh,n,p))+binom.pmf(thresh,n,p))

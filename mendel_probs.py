#! /usr/bin/python37
"""
Author: Wytze Gelderloos
Date: 29-7-2019
Mendel's First Law
This script takes three integers representing the amount of dominant homozygous
, heterozygous and recessive homozygous. It gives a float from 0 to 1 for the
probability of two random animals of this population mating and producing a
offspring expressing the dominant phenotype.
"""

input_list = [ 21, 19, 25]
## assigning the first integer of input list as dominant group
dom= input_list[0]
## assigning the second integer of input list as heterozygous group
het = input_list[1]
## assigning the third integer of input list as recessive group
res = input_list[2]
total = dom + het + res
## mating of dominant with a dominant indivdual
dom_dom_prob =  dom/total * (dom-1)/(total-1)
## mating of dominant with heterozygous
dom_het_prob = (dom/total * het/(total-1)) + (het/total * dom/(total-1))
## mating of heterozygous with heterozygous
het_het_prob = (het/total * (het-1)/(total-1))*0.75
## mating of dominant with recessive
dom_res_prob = (dom/total * res/(total-1)) + (res/total * dom/(total-1))
## mating of heterozygous with recessive
het_res_prob = ((het/total * res/(total-1) + (res/total * het/(total-1)))) * 0.5
 ## recessive with recessive does not lead to a dominant phenotype in any way

## adding up the probabilities
probs =  dom_dom_prob+dom_het_prob+het_het_prob+dom_res_prob + het_res_prob

print(probs)

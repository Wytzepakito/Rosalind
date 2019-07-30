"""
Author: Wytze Gelderloos
Date: 30-7-2019
Protein motifs
This script no longer works since some entries no longer exist.

"""
from urllib.request import urlopen
import regex as re
prot_string = """
P39873_RNBR_BOVIN
Q47A87
Q5FMJ3
A6NM15
P13473_LMP2_HUMAN
P19246_NFH_MOUSE
P05231_IL6_HUMAN
Q55AB5
P13838_LEUK_RAT
P21810_PGS1_HUMAN
P01044_KNH1_BOVIN
P17404_CHM1_BOVIN
"""
## get entires
master_prots = prot_string.split("\n")
## first entry is an empty string
master_prots.pop(0)
## last entry as well
master_prots.pop(len(master_prots)-1)
master_dic={}
for prot in master_prots:
    ## format the URL with the entry inside
    url = "http://www.uniprot.org/uniprot/" + prot + ".fasta"
    response = urlopen(url)
    print(url)
    fasta = response.read().decode("utf-8", "ignore")
    prot_seq = re.findall("[A-Z\n]{5,}$",fasta)[0]

    master_dic[prot] = prot_seq.replace("\n", "")



for key, item in master_dic.items():
    iter = re.finditer(r"N[^P][ST][^P]", item)
    indices = [m.start(0)+1 for m in iter]
    if len(indices)>=1:
        print(key)
        print(" ".join(map(str,indices)))

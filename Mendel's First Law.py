# Mendel's first law

# Example:  2 2 2
# 2 homozygous dominant (AA), 22 heterozygous (Aa), and 2 homozygous recessive (aa)
# P(dominant) = (P(AA + AA) + P(AA + Aa) + P(Aa + Aa) + P(Aa + aa) + P(AA + aa)) / C(6,2)
# = (1 + 4 + 1 * 0.75 + 4 * 0.5 + 4) / (6! / 2! * 4!)
# = 0.78333

import os
os.chdir('C:\\Users\\Terry Tang\\Desktop\\Python3.3\\Rosalind_bioinformatics')

import sys
import math


def c_combination(total, select):
    return math.factorial(total)/(math.factorial(select)*math.factorial(total-select))


if __name__=='__main__':
    with open('rosalind_iprb.txt','r') as fin:
        hod, he, hor = map(int, fin.readline().rstrip().split(' '))

    p_hod = c_combination(hod, 2) * 1
    p_he = c_combination(he, 2) * 0.75
    p_hod_he = (c_combination(hod, 1) * c_combination(he, 1)) * 1
    p_hod_hor = (c_combination(hod, 1) * c_combination(hor, 1)) * 1
    p_he_hor = (c_combination(he, 1) * c_combination(hor, 1)) * 0.5

    p = (p_hod + p_he + p_hod_he + p_hod_hor + p_he_hor) / c_combination(hod + he + hor, 2)

    print(p)

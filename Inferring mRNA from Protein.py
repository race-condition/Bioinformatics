import os
'''
RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}


freq={}
for key in RNA_CODON_TABLE:
    if RNA_CODON_TABLE[key] in freq:
         freq[RNA_CODON_TABLE[key]]=freq[RNA_CODON_TABLE[key]]+1
    else:
         freq[RNA_CODON_TABLE[key]]=1

table ={
 'K'    :   {'AAA',  'AAG'},                    
 'N'    :   {'AAC',  'AAT'} ,               
 'T'    :   {'ACA',  'ACC', 'ACG',   'ACT'},            
 'R'    :   {'AGG',  'AGA',  'CGA',  'CGC',  'CGG',  'CGT'},
 'S'    :   {'AGC',  'AGT',  'TCA',  'TCC',  'TCG',  'TCT'},
 'I'    :   {'ATA',  'ATC',  'ATT'},        
 'M'    :   {'ATG'},                        
 'Q'    :   {'CAA',  'CAG'},                    
 'H'    :   {'CAC',  'CAT'},                    
 'P'    :   {'CCA',  'CCC',  'CCG',  'CCT'},            
 'L'    :   {'CTA',  'CTC',  'CTG',  'CTT',  'TTA',  'TTG'},
 'E'    :   {'GAA',  'GAG'},                    
 'D'    :   {'GAC',  'GAT'},                    
 'A'    :   {'GCA',  'GCC',  'GCG',  'GCT'},            
 'G'    :   {'GGC',  'GGA',  'GGG',  'GGT'},            
 'V'    :   {'GTA',  'GTC',  'GTG',  'GTT'},            
 'Y'    :   {'TAC',  'TAT'},                    
 'C'    :   {'TGC',  'TGT'},                    
 'W'    :   {'TGG'},                    
 'F'    :   {'TTC',  'TTT'},                    
}

we get the codon's freqence table as follows:
'''
codons = {'A':4, 'R':6, 'N':2, 'D':2, 'C':2, 'Q':2, 'E':2, 'G':4, 'H':2, 
          'I':3, 'L':6, 'K':2, 'M':1, 'F':2, 'P':4, 'S':6, 'T':4, 'W':1, 
          'Y':2, 'V':4, 'STOP':3}

def infer(seq):
    global codons

    n = 3
    for aa in seq:
        n *= codons[aa]
    print (n%1000000)


import os
os.chdir('C:\\Users\\Terry Tang\\Desktop\\Python3.3\\Rosalind_bioinformatics')
file=open('rosalind_grph.txt','r')
lines = file.readlines()


raw_sample = []
for line in lines:
    line = line.rstrip()
    raw_sample.append(line)


DNA={}
dna_key=''

for dna in raw_sample:
    if dna[0]=='>':
        dna_key=dna[1:]
        DNA[dna_key]=''
    else:
        DNA[dna_key]+=dna

first={}
last={}

for dna_key in DNA:
    dna_str=DNA[dna_key]
    last3=dna_str[-3]+dna_str[-2]+dna_str[-1]
    first3=dna_str[0]+dna_str[1]+dna_str[2]
    first[dna_key]=first3
    last[dna_key]=last3

for key1 in last:
    for key2 in first:
        if key1!=key2:
            if first[key2]==last[key1]:
                output=key1+' '+key2+'\n'
                print(key1,key2)
                
    


import os
os.chdir('C:\\Users\\Terry Tang\\Desktop\\Python3.3\\Rosalind_bioinformatics')
file=open('rosalind_gc.txt','r')
raw_samples=file.readlines()
file.close()

samples={}
cur_key=''

for elem in raw_samples:
    if elem[0]=='>':
        cur_key=elem[1:].rstrip()
        samples[cur_key]=''
    else:samples[cur_key]+=elem.rstrip()

for cur_key in samples:
    s=samples[cur_key]
    gc=float(((s.count('G')+s.count('C'))/len(s))*100)
    print(cur_key)
    print(gc)

import os
os.chdir('C:\\Users\\Terry Tang\\Desktop\\Python3.3\\Rosalind_bioinformatics')
file=open('rosalind_HAMM.txt','r')
s1=file.readline().strip()
s2=file.readline().strip()

hamming_distance=0
for i in range(len(s1)):
    if s1[i]==s2[i]:
        hamming_distance=hamming_distance
    else:
        hamming_distance=hamming_distance+1
print(hamming_distance)


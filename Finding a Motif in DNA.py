import os
os.chdir('C:\\Users\\Terry Tang\\Desktop\\Python3.3\\Rosalind_bioinformatics')
file=open('rosalind_subs.txt','r')
s=file.readline().rstrip()
t=file.readline().rstrip()


def locations(s,t):
    for i in range(len(s)):
        if s[i:i+len(t)]==t: 
            print(i+1)
'''
def locations(s,t):
     tl = len(t)
     for i, n in enumerate(s):
         if s[i:i+tl] == t:
             print(i+1)
     
'''


'''

with open(input_file) as file:
    dna1 = file.readline().strip()
    dna2 = file.readline().strip()
i = dna1.find(dna2)
while i != -1:
    print i + 1, 
    i = dna1.find(dna2, i + 1)


'''

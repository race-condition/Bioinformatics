import os
os.chdir('C:\\Users\\Terry Tang\\Desktop\\Python3.3\\Rosalind_bioinformatics')
file=open('rosalind_cons.txt','r')

fileout = open('CONS_output.txt','w')

lines = file.readlines()

seqs = []
for line in lines:
    line = line.rstrip()
    seqs.append(line)

# make nested lists for columns in seqs
transseq =  [[row[i] for row in seqs] for i in range(len(seqs[0]))]

a = []
c = []
g = []
t = []
cons = ''
for pos in transseq:
    a.append(pos.count('A'))#collect frequency of A in each sublist(each column)
    c.append(pos.count('C'))
    g.append(pos.count('G'))
    t.append(pos.count('T'))

    counta = pos.count('A')
    countc = pos.count('C')
    countg = pos.count('G')
    countt = pos.count('T')

    if counta == max(counta,countc,countg,countt):
        cons += 'A'
    elif countc == max(counta,countc,countg,countt):
        cons += 'C'
    elif countg == max(counta,countc,countg,countt):
        cons += 'G'
    elif countt == max(counta,countc,countg,countt):
        cons += 'T'

astr = 'A:'
cstr = 'C:'
gstr = 'G:'
tstr = 'T:'

for x in a:
    astr = astr + ' ' + str(x) # make a row such that A: 5 1 0 0 5 5 0 0
for x in c:
    cstr = cstr + ' ' + str(x)
for x in g:
    gstr = gstr + ' ' + str(x)
for x in t:
    tstr = tstr + ' ' + str(x)

print (cons)
print (astr)
print (cstr)
print (gstr)
print (tstr)

cons += '\n'
astr += '\n'
cstr += '\n'
gstr += '\n'


fileout.write(cons)
fileout.write(astr)
fileout.write(cstr)
fileout.write(gstr)
fileout.write(tstr)

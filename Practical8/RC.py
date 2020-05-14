# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#read the sequence
seq='ATGCGACTACGATCGAGGGCCAT'
seq=','.join(seq) 
cdna=''
#turn the sequence into a list
list=seq.split(',')
#get the complementary sequence
for i in list:
    if i=='A':
        cdna="T"+cdna
    elif i=='C':
        cdna="G"+cdna
    elif i=='G':
        cdna="C"+cdna
    elif i=='T':
        cdna="A"+cdna
# output 
print(cdna)


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

seq='ATGCGACTACGATCGAGGGCCAT'
seq=','.join(seq) 
dna={}
cdna=''
list=seq.split(',')
for i in list:
    if i=='A':
        cdna="T"+cdna
    elif i=='C':
        cdna="G"+cdna
    elif i=='G':
        cdna="C"+cdna
    elif i=='T':
        cdna="A"+cdna
        
print(cdna)


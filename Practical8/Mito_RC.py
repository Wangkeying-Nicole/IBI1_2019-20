# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:37:06 2020

@author: 86158
"""
#import library
import re
count=0
m=0
num={}
temp=input('please input a filename:')
#import file, and create a yfile for output
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as xfile:
 with open(temp,'w') as yfile:
  for line in xfile:
      if line.startswith('>'):#start reading
          cdna=''
          seq=''
          if re.search('Mito:',line):# sequences of mitochondria genes 
           m=m+1
           write=re.findall(r'gene:(.+) gene_biotype:',line)
           name=write[0]
           out='name:'+name+'\n'
           yfile.write(out)
           #read and output lengh of the sequence
           while True:
              line=xfile.readline()
              if not line:
                  out='lenth:'+str(count)
                  num[m]=count
                  yfile.write(out)
                  break
              if line.startswith('>'):
                  out='lenth:'+str(count)+'\n'
                  yfile.write(out)
                  num[m]=count
                  count=0
                  break
              count=count+len(line)-1
              seq=seq+line#read the original sequence
           #get the complementary sequences 
           seq=','.join(seq) 
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
           yfile.write(cdna+'\n')#output cdna
       


           
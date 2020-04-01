# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:37:06 2020

@author: 86158
"""
import re
count=0
m=0
num={}
temp=input('please input a filename:')

with open(temp,'r') as xfile:
 with open('mito_RC.fa','w') as yfile:
  for line in xfile:
      if line.startswith('>'):
          cdna=''
          result='>'
          seq=''
          if re.search('Mito:',line):
           m=m+1
           write=re.findall(r'gene:(.+) gene_biotype:',line)
           name=write[0]
           n=20-len(name)
           out='name:'+name+'\n'
           yfile.write(out)
           result=out
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
              seq=seq+line
           result=result+out
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
           yfile.write(cdna+'\n')
           print(result[:-1])
           print(cdna+'\n')


           
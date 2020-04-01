# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:23:03 2020

@author: 86158
"""
import re
count=0
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as xfile:
 with open('mito_gene.fa','w') as yfile:
  for line in xfile:
      if line.startswith('>'):
          if re.search('Mito:',line):
           write=re.findall(r'gene:(.+) gene_biotype:',line)
           name=write[0]
          
           out='name:'+name+'\n'
           yfile.write(out)
           while True:
              line=xfile.readline()
              if not line:
                  out='lenth:'+str(count)
                  yfile.write(out)
                  break
              if line.startswith('>'):
                  out='lenth:'+str(count)+'\n'
                  yfile.write(out)
                  count=0
                  break
              count=count+len(line)-1

                  
                  
              
       
          
          
          
         

              
                  
                  


# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:23:03 2020

@author: 86158
"""
#import necessary library
import re

count=0#count the length
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as xfile:
 with open('mito_gene.fa','w') as yfile:
  for line in xfile:
      #read start 
      if line.startswith('>'):
         if re.search('Mito:',line):#judge to read or not
           write=re.findall(r'gene:(.+) gene_biotype:',line)
           name=write[0]#catch the name
        
           out='name:'+name+'\n'
           yfile.write(out)
           seq=''
           while True:
              line=xfile.readline()
              if not line:#finish reading the file——>output
                  out='lenth:'+str(count)
                  yfile.write(out)
                  yfile.write(seq)
                  break
              if line.startswith('>'):# come to a new item, last item finish——>output
                  out='lenth:'+str(count)+'\n'
                  yfile.write(out)
                  yfile.write(seq)
                  count=0
                  break
              count=count+len(line)-1#count the length
              seq=seq+line#record (add up) the sequence


                  
                  
              
       
          
          
          
         

              
                  
                  


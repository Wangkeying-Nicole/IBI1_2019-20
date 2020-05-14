# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:07:34 2020

@author: 86158
"""

# Input:	A	list	of	10	values:	
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
#sequence the lengths in order
gene_lengths.sort()
#remove the longest and the shortest(0,8)
del(gene_lengths[0])
del(gene_lengths[8])
print(gene_lengths)#output the list after removing

#making boxplot
#import libraries
import numpy as np
import matplotlib.pyplot as plt
n=8
#giving parameters
plt.boxplot(gene_lengths,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
            )
#print the plot
plt.show()

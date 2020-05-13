# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:25:14 2020

@author: 86158
"""
#input necessary library
import pandas as pd
#input 3 protein sequence
human='MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
mouse='MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
random='WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'

#read the "BLOSUM62 matrix.csv" as a dataframe
matrix=pd.read_csv("BLOSUM62matrix.csv")

#set up a function to find the amino acid(aa) in the matrix
def find_row_num(aa):
    j=0
    while True:
        if matrix.iloc[j,0]!=aa:
            j+=1#position j not the amino acid we need, then move on
        if matrix.iloc[j,0]==aa:
            break#find the amino acid
    return j#result of the function

#comparison of two sequences that you want to compare
temp1=input('please input human/mouse/random:' )
seq1=locals()[temp1]
temp2=input('please input human/mouse/random:' )
seq2=locals()[temp2]

#calculate the hamming distance
distance=0 #set initial distance as zero
for i in range(len(seq1)): #compare each amino acid one by one 
    if seq1[i]!=seq2[i]:
        distance+=1 #add a score 1 if amino acids are different 
percent=(len(seq1)-distance)/len(seq1)

score=0#variable for storing the blosum score
alignment=''#variable for storing the BLAST-like visual alignment
for i in range(len(seq1)):
    aa1=seq1[i]
    aa2=seq2[i]
#use the function to retrieve the score according to 2 amino acids from seq1 and seq2
    score_plus=matrix.loc[find_row_num(aa2),aa1]
#calculate the total score
    score+=score_plus
#calculate the BLAST-like visual alignment
    if aa1==aa2:
        alignment+=aa1
    elif score_plus>=0:
        alignment+='+'
    else:
        alignment+=" "

#print out the result
print("the hamming distance of two sequence is "+str(distance))
print(str(percent*100)+"%"+" of the amino acids are identical.")
print("the blosum62 score is "+str(score))
print("seq1:"+seq1)
print("#vis:"+alignment)
print("seq2:"+seq2)
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:06:45 2020

@author: 86158
"""
# import necessary libraries
import xml.dom.minidom
import pandas as pd
# document object
DOMTree=xml.dom.minidom.parse('go_obo.xml')
# root element
collection=DOMTree.documentElement
# list of 'term' elements
terms=collection.getElementsByTagName('term')
defs=[]
is_a=[]
dic={}
for term in terms:
    Defs=term.getElementsByTagName('def')
    Ids=term.getElementsByTagName('id')[0]
    Is_as=term.getElementsByTagName('is_a')
    #read the is_a, put them in a list(two:1 list for 1 item, generate the list together)
    for x in Is_as:
        is_a.append(x.childNodes[0].data)
    dic[Ids.childNodes[0].data]=is_a[:]
    is_a.clear()
    for definition in Defs:#list out definition data in a list 
        defstr=definition.getElementsByTagName('defstr')[0]
        defs.append(defstr.childNodes[0].data)    
a=[]#count and mark the number of items with "autophagosome"
for x in range(len(defs)):
    if 'autophagosome' in defs[x]:
        a.append(x)
#store the information for output(id,name,definition)
ids=[]
names=[]
d=[]
for i in a:
    IDs=terms.item(i).getElementsByTagName('id')[0]
    ids.append(IDs.childNodes[0].data)
    NAMEs=terms.item(i).getElementsByTagName('name')[0]
    names.append(NAMEs.childNodes[0].data)
    d.append(defs[i])
    
# count the childnode 
childnode = []
for i in ids:
    m = []
    count = 0
    for j in dic:
        if i in dic[j]:
            count += 1#count the element in the total
            m.append (j)
    n = m[:]
    inc = count
    while inc != 0 :#count the element in the single list, until there is no more list inside the list
        m = []
        inc = 0
        for k in n:
            for j in dic:
                if k in dic[j]:
                    count += 1
                    inc += 1
                    m.append (j)
        n = m[:]
    childnode.append (count)
    
#output
xfile=pd.DataFrame({'id':ids,'name':names,'definition':d,'childnodes':childnode})
xfile.to_excel('Autophagosome.xlsx',
               sheet_name='Autophagosome',
               columns=['id','name','definition','childnodes'])








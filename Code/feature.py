import os
from vocab import *
from countAllDocsInClassC import *
from countAllDocsExceptClassC import *
from calculate import *

folder_list=os.listdir(r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\Training5')
root=r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\Training5'

vocab=create_vocab(folder_list,root)
vocab=list(set(vocab))
vocab=vocab[:100]
#print len(vocab)
#print vocab


count=0
for dir in folder_list:
    folder_path=os.path.join(root,dir)
    ls=[]
    for word in vocab :
        nfirst,n11=countAllDocsInClassC(folder_path,word) 
        n01=nfirst-n11
        nsecond,n10=countAllDocsExceptClassC(root,folder_list,folder_path,word)
        n00=nsecond-n10
        #print word,nfirst,nsecond,n11,n10,n01,n00
        value=calculate(n11,n10,n01,n00)
        ls.append((word,value))
        #print dir,word,"   ",n11,n10,n01,n00
    #print sorted(ls,key=lambda x:x[1])
    print
    print
    count=count+1
    if count>3:
        break
    
        
    

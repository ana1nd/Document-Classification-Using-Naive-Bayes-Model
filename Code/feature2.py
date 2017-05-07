import os
from extractVocab import *
from stemLemma import *
from calculate import *

folder_list=os.listdir(r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\BackUp\11111\Training')
root=r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\BackUp\11111\Training'

def getKey(item):
    return item[1]

classDict={}
i=0
for dir in folder_list :
    folder_path=os.path.join(root,dir)
    for root1,dirs,filenames in os.walk(folder_path):
        for f in filenames :
            text_doc=extractVocab(root1,f)  # type(text_c)=list
            text_doc_stemmed=stemLemma(text_doc)  #type(text_doc_stemmed)=list
            text_doc_stemmed=set(text_doc_stemmed)
            text_doc_stemmed=list(text_doc_stemmed)
            
            for word in text_doc_stemmed:
                if len(classDict)==0 or classDict.has_key(word)==False :
                    classDict[word]=[0]*20
                classDict[word][i]=classDict[word][i]+1
                classDict[word][19]=classDict[word][19]+1
    i=i+1
    print i,len(classDict)
i=0
last=19
feature=[]
for dir in folder_list:
    ls=[]
    folder_path=os.path.join(root,dir)
    for w in classDict.keys():
        n11=classDict[w][i]
        n10=classDict[w][last]-n11
        n01=100-n11
        n00=1800-(classDict[w][last]-n11)
        n=n11+n10+n01+n00
        value=calculate(n11,n10,n01,n00)
        ls.append((w,value))
    l=len(ls)
    ls=sorted(ls,key=getKey,reverse=True)
    feature=feature+ls
   #print len(feature)
    i=i+1

featureDict={}
feature=sorted(feature,key=getKey,reverse=True)
featureList=[]
for word in feature:
    if len(featureList)>=20000:
        break
    if len(featureDict)==0 or featureDict.has_key(word[0])==False:
        featureDict[word[0]]=word[1]
        featureList.append((word[0],word[1]))

print len(featureList)

        

            
        

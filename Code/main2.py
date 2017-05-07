''' 3-1-1'''

from __future__ import division
import os
from nltk import *
from math import *
from nltk.tokenize import wordpunct_tokenize
from stemLemma import *  # Lemmatizing and stemming the vocabulary
from vocab import *  # creates vocabulary
from countAllDocs import * # counts all documents
from text import * #concatenate All Docs of Class C
from collections import Counter

folder_list=os.listdir(r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\BackUp\10 fold\Training2')
root=r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\BackUp\10 fold\Training2'

vocab=create_vocab(folder_list,root)
#vocab=sorted(set(vocab))  (1)
vocab=list(vocab)
print len(set(vocab))
n=countAllDocs(folder_list,root)
# stemming and lemmatizing each word of the vocabulary
vocabStemmed=stemLemma(vocab)

words=Counter(vocabStemmed)
#words=featureDict
keyValuePair=words.most_common() # list of tuple(key,frequency) in reverse prder
mostFreqK=[]  #list of most frequent k-words with k=5000,10000,len(words)
classDict={} # it is a dictionary where each element is a (term,list)
prior=[] #prior probability of each class: /n
for i in xrange(0,len(words),1):
    mostFreqK.append(keyValuePair[i][0])
    classDict[keyValuePair[i][0]]=[]
##
##for i in featureDict.keys():
##    mostFreqK.append(i)
##    classDict[i]=[]

l=0
for dir in folder_list: # that is for each class
    folder_path=os.path.join(root,dir)
    text_c,nc=concatenateAllDocsofC(folder_path)  # type(text_c)=string
    doc=wordpunct_tokenize(text_c) #converts the string into tokens
    text_c_stemmed=stemLemma(doc)  #type(text_c_stemmed)=list
    #print dir," length=" , len(set(text_c_stemmed))
    text_c=" ".join(text_c_stemmed)  # list---->string conversion

    #print dir,text_c
    prior.append(nc/n)
    words_c=text_c.split()
    wordCount=Counter(words_c).most_common()
    mydict=dict(wordCount)

    biggerList=[]
    biggerDict={}
    countAllFreq=0

    for word in mostFreqK:
        value=0
        if mydict.has_key(word):
            value=log(mydict.get(word),10)+1
        countAllFreq=countAllFreq+pow(value,2)
        tuple_variable=(word,value)
        biggerList.append(tuple_variable)

    for word in mostFreqK:
        value=0
        if mydict.has_key(word):
            value=log(mydict.get(word),10)+1
        ratio=(value+1)/(countAllFreq+len(mostFreqK))  #smoothing is done here
        
        classDict[word].append(ratio)

    biggerDict=dict(biggerList)
    l=l+len(text_c)
    print dir,len(text_c),len(words_c)
print l
#print mostFreqK[:10]


def UseData():
    return classDict,prior

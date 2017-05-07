
''' 4-4-3 '''

from __future__ import division
import os
from nltk import *
from math import *
from nltk.tokenize import wordpunct_tokenize
from collections import Counter


from vocab import *  # creates vocabulary
from countAllDocs import *
from stemLemma import *
from text import *
import feature2


folder_list=os.listdir(r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\BackUp\10 fold\Training2')
root=r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\BackUp\10 fold\Training2'


vocab=create_vocab(folder_list,root)
print "len(set(vocab))=",len(set(vocab))
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


featureDict=feature2.classDict

l=0
var=0
for dir in folder_list :
    folder_path=os.path.join(root,dir)
    text_c,nc=concatenateAllDocsofC(folder_path)  # type(text_c)=string
    doc=wordpunct_tokenize(text_c) #converts the string into tokens
    text_c_stemmed=stemLemma(doc)  #type(text_c_stemmed)=list
    text_c=" ".join(text_c_stemmed)  # list---->string conversion

    #print dir,text_c
    prior.append(nc/n)
    words_c=text_c.split()
    wordCount=Counter(words_c).most_common()
    mydict=dict(wordCount)

    biggerList=[]
    biggerDict={}
    countAllFreq=0
    mx=-1
    for word in mostFreqK:
        if mydict.has_key(word):
            tf_word=mydict.get(word)
            mx=max(mx,tf_word)
            
    for word in mostFreqK :
        tf_word=0
        df_word=1
        idf_word=1
        if mydict.has_key(word):
            tf_word=mydict.get(word)
        if featureDict.has_key(word):
            df_word=featureDict[word][var]
        if df_word!=0:
            idf_word=log(pow(n/df_word,2),10)
        value=(0.5+((0.5*tf_word)/mx))*idf_word
        countAllFreq=countAllFreq+pow(value,2)
        tuple_variable=(word,value)
        biggerList.append(tuple_variable)

    for word in mostFreqK:
        tf_word=0
        df_word=1
        idf_word=1
        if mydict.has_key(word):
            tf_word=mydict.get(word)
        if featureDict.has_key(word):
            df_word=featureDict[word][var]
        if df_word!=0:
            idf_word=log(pow(n/df_word,2),10)
        value=(0.5+((0.5*tf_word)/mx))*idf_word
        ratio=(value+1)/(sqrt(countAllFreq)+len(mostFreqK))
        classDict[word].append(ratio)

    biggerDict=dict(biggerList)
    l=l+len(text_c)
    print dir,len(text_c),len(words_c)
    var=var+1

print l
        
def UseData():
    return classDict,prior






    

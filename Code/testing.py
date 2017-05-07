import os
from extractVocab import *
from main import *


root=r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\Testing'
folder_path=root

classDict,prior=UseData()

for i in xrange(0,19,1):
    print prior[i]

#print classDict


def findmax(score):
    max=-1
    index=-1
    for i in xrange(0,19,1):
        if score[i]>max:
            max=score[i]
            index=i
    return index


classCount={}

className=["autos","baseball","crypt","electronics","graphics","hockey","ibm_hardware","mac_hardware","med","misc","miscforsale","motorcycles","politics_guns","politics_mideast","politics_misc","religion_christian","religion_misc","space","windows"]
score=[None]*19 # to calculate the score of each class and then find max of all 
for root1,dirs,filenames in os.walk(folder_path):
    for f in filenames:
        w=extractVocab(root,f)
        #print f,type(w),len(w),len(set(w))
        for i in xrange(0,19,1):
            score[i]=prior[i]
            for term in w:
                value=0
                if classDict.has_key(term):
                    value=classDict[term][i]
                score[i]=score[i]+value
        number=findmax(score)
        if classCount.has_key(className[number]):
            classCount[className[number]]=classCount[className[number]]+1
        else:        
            classCount[className[number]]=1
        print f,len(w),number,className[number]
        #print




            
        
                

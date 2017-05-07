import os
from extractVocab import *
from main5 import *
#from main2 import *
#from main3 import *
from stemLemma import *
from answer import *


#folder_list=os.listdir(r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\Testing')
#root=r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\Testing'

folder_list=os.listdir(r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\BackUp\10 fold\Testing2')
root=r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\BackUp\10 fold\Testing2'


folder_path=root
classDict,prior=UseData()

#for i in xrange(0,19,1):
    #print prior[i]

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
checkAnswer={}


className=["autos","baseball","crypt","electronics","graphics","hockey","ibm_hardware","mac_hardware","med","misc","miscforsale","motorcycles","politics_guns","politics_mideast","politics_misc","religion_christian","religion_misc","space","windows"]

for i in className:
    checkAnswer[i]=0
    classCount[i]=0

score=[None]*19 # to calculate the score of each class and then find max of all 

for dir in folder_list:
    folder_path=os.path.join(root,dir)
    for root1,dirs,filenames in os.walk(folder_path):
        for f in filenames:
            w=extractVocab(root1,f)  # w is already list
            #doc=wordpunct_tokenize(text_c) #converts the string into tokens
            wStemmed=stemLemma(w)
            for i in xrange(0,19,1):
                score[i]=prior[i]
                for term in w:
                    value=0
                    if classDict.has_key(term):
                        value=classDict[term][i]
                    score[i]=score[i]+value
            number=findmax(score)

        
            if className[number]==answer[f]:
                checkAnswer[className[number]]=checkAnswer[className[number]]+1        

            if classCount.has_key(className[number]):
                classCount[className[number]]=classCount[className[number]]+1

            #print f,len(w),number,className[number],"     ",answer[f]
sum=0
for class_var in checkAnswer:
    sum=sum+checkAnswer[class_var]
print checkAnswer
print
print classCount
print sum

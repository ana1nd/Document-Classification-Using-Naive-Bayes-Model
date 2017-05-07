import nltk
def stemLemma(v): #this v is a type list
    wnl=nltk.WordNetLemmatizer()
    porter=nltk.PorterStemmer()
    ls=[]
    for i in xrange(0,len(v),1):
	word1=wnl.lemmatize(v[i])
	word2=porter.stem(word1)
	ls.append(word2)
    #ls=set(ls)  (2)
    ls=list(ls)
    return ls  #return list 
    
    

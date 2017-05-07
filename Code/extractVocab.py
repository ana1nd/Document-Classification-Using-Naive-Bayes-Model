import os
from nltk.tokenize import wordpunct_tokenize


def extractVocab(root,f):
    log=open(os.path.join(root,f),'r')
    lines=log.readlines()
    str="".join(lines)
    doc=wordpunct_tokenize(str)
    return list(set(doc))

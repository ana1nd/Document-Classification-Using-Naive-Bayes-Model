import os
from nltk.tokenize import wordpunct_tokenize

def create_vocab(folder_list,root):
    data=""
    for dir in folder_list:
        folder_path=os.path.join(root,dir)
        for root1,dirs,filenames in os.walk(folder_path):
            for f in filenames:
                log=open(os.path.join(root1,f),'r')
                lines=log.readlines()
                str="".join(lines)
                data=data+str

    doc=wordpunct_tokenize(data)    
    return list(doc)

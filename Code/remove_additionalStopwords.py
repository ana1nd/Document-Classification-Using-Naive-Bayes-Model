# Removes from additional stopwords from all files over a directory
# Removes all those tokens which are of length less then 3

from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
import os
stops=stopwords.words('english')
stops=set(stops)
new_list=['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','*','^','`','0','1','2','3','4','5','6','7','8','9','$','%','&','#','subject','+','|',chr(244),chr(253),chr(228)]
stops.update(new_list)

folder_list=os.listdir(r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\Training')
root=r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\Training'

for dir in folder_list:
    folder_path=os.path.join(root,dir)
    for root1,dirs,filenames in os.walk(folder_path):
        for f in filenames:
            log=open(os.path.join(root1,f),'r+')
            data=""
            lines=log.readlines()
            str="".join(lines)
            doc=wordpunct_tokenize(str)
            for j in doc:
                if j not in stops:
                    if len(j)>=3:
                        flag=0
                        for k in new_list:
                            if k in j:
                                flag=1
                                break
                        if flag==0:
                            data=data+j+" "
            log.seek(0)
            log.write(data)
            log.truncate()
            log.close()
        

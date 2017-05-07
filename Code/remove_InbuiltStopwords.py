from nltk.corpus import stopwords
import os
stops=stopwords.words('english')
stops=set(stops)
#indir=r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\windows'
indir=r'C:\Users\Anand Namdev\Downloads\mini_newsgroup_clean\windows'
for root,dirs,filenames in os.walk(indir):
    for f in filenames:
        log=open(os.path.join(root,f),'r+')
        data=""
        lines=log.readlines()
        for i in lines:
            str=i.split()
        for j in str:
            if j not in stops:
                data=data+j+" "
        log.seek(0)
        log.write(data)
        log.truncate()
        log.close()

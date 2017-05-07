import os
indir=r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\windows'
for root,dirs,filenames in os.walk(indir):
    for f in filenames:
        log=open(os.path.join(root,f),'r+')
        data=""
        lines=log.readlines()
        for i in lines:
            str=i.strip()
            for j in str:
                data=data+j.lower()
        log.seek(0)
        log.write(data)
        log.close()

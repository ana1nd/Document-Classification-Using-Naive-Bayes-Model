import os
def concatenateAllDocsofC(folder_path):
    data=""
    for root1,dirs,filenames in os.walk(folder_path):
        for f in filenames:
            log=open(os.path.join(root1,f),'r')
            lines=log.readlines()
            str="".join(lines)
            data=data+str
        return data,len(filenames)

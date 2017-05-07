import os

folder_list=os.listdir(r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\Training')
root=r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\Training'

for dir in folder_list:
    folder_path=os.path.join(root,dir)
    for root1,dirs,filenames in os.walk(folder_path):
        for f in filenames:
            log=open(os.path.join(root1,f),'r+')
            data=""
            lines=log.readlines()
            for i in lines:
                str=i
                str=str.replace('>',' ')
                str=str.replace('<',' ')
                str=str.replace('\n',' ')
                str=str.replace(':',' ')
                str=str.replace('-',' ')
                str=str.replace('^',' ')
                str=str.replace('/',' ')
                str=str.replace('_',' ')
                str=str.replace('+',' ')
                str=str.replace('=',' ')
                str=str.replace('|',' ')
                #str=str.replace('\\',' ')
                str=str.replace('\\',' ')
                data=data+str
            log.seek(0)
            log.write(data)
            log.close()
            

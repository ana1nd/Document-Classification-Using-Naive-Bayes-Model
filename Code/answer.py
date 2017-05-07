import os

answer={}
folder_list=os.listdir(r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\BackUp\11111\Training')
root=r'C:\Users\Anand Namdev\Downloads\Compressed\datasets machine learning\mini_newsgroup_clean\BackUp\11111\Training'


for dir in folder_list :
    folder_path=os.path.join(root,dir)
    for root1,dirs,filenames in os.walk(folder_path):
        for f in filenames:
            answer[f]=dir
            


def UseAnswer():
    return answer
            

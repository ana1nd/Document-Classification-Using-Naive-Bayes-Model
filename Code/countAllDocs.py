import os
def countAllDocs(folder_list,root):    # counts all docs in all classes
    sum=0
    for dir in folder_list:
        folder_path=os.path.join(root,dir)
        for root1,dirs,filenames in os.walk(folder_path):
            sum=sum+len(filenames)
    return sum

with open(r'C:\Users\Anand Namdev\Downloads\53315','r+') as f:
    data=""
    lines=f.readlines()
    for i in lines:
        str=i
        stt=str.replace('>',' ')
        str=str.replace('<',' ')
        str=str.replace(':',' ')
        str=str.replace('\n',' ')
        str=str.replace('-',' ')
        data=data+str
    
    f.seek(0)
    f.write(data)
    #f.truncate(0)
    f.close()

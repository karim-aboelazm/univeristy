file = open("D:\\Uni\\src\\stu.txt",'r',encoding='utf-8')

for i in file:
    if len(i)>1:
        i= i.replace("\n","").split(',')
 
file.close()

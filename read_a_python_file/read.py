#import csv library for read a csv file
import csv

dict1=dict()
#opening a text file for reading 
with open("a.txt") as doc:
    read =csv.reader(doc,delimiter=':')
    for i in read:
        print(i)
        #for skip comment line 
        if(i[0][0]=='#'):
             continue
        else:
            dict1[i[0]]=i[3]
#printing dictnary items    
for i,z in dict1.items():
    print (i+' = '+z)



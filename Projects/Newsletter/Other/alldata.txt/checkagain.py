import numpy as np
import pandas as pd
all_data=pd.read_csv('dataaa.csv')
email=all_data['Email Address']
new=email.to_list()
newf=[]
for i in new:
    newf.append(i)
print(len(newf))
newdata=open('finaaaaaal_email.txt','w')
for i in newf:
    try:
        newdata.writelines(f"{i[:-1]}\n")
    except:
        print (i)
newdata.close()
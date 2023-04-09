import numpy as np
import pandas as pd
raw_data=open('college_mail_database.txt','r')
enrollment=[]
name=[]

while True:
    student_info=raw_data.readline()
    if len(student_info)==0:
        break
    elif len(student_info)==1:
        pass
    else:
        print (student_info)
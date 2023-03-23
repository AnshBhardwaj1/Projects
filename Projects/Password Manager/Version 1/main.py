from Encryptor import *
from Decryptor import *
code=int(input("What is your code : "))
what=input("Do you wanna add passwords or view passwords : ")
what=what.lower()
if what=='view':
    f=open("PDataBase.txt",'r')
    while True:
        line = f.readline()
        if not line:
            break
        d_line=decrypt(line[:-1],code)
        print(d_line)
    f.close()
elif what=='add':
    new_pass=open("PDataBase.txt",'a')
    n=int(input("How many passwords do you have : "))
    for i in range(n):
        passs=input("what is your password : ") 
        e_pass=encrypt(passs,code)
        new_pass.writelines(f'{e_pass}\n')
    new_pass.close()
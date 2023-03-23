from Encryptor import *
from Decryptor import *
class Password:
    def __init__(self,website,username,pword) -> None:
        self.website=website
        self.username=username
        self.pword=pword

    def __str__(self) -> str:
        return (f'{self.website}\n{self.username}\n{self.pword}')
    
code=int(input("what is your code : "))
what=input("Do you wanna add passwords or view passwords : ")
what=what.lower()
if what=='view':
    what=input("which website : ")
    f=open("DataBase.txt",'r')
    while True:
        line = f.readline()
        if not line:
            break
        d_line=decrypt(line[:-1],code)
        if what==d_line:
            print (d_line)
            user_ = f.readline()
            print (decrypt(user_[:-1],code))
            pass_ = f.readline()
            print (decrypt(pass_[:-1],code))
            exit()
        else:
            pass
    f.close()
elif what=='add':
    new_pass=open("DataBase.txt",'a')
    n=int(input("How many passwords do you have : "))
    for i in range(n):
        web=input("Which website is it : ")
        p_word=input("what is your username : ")
        u_name=input("what is your password : ") 
        e_pass=encrypt(p_word,code)
        e_web=encrypt(web,code)
        e_name=encrypt(u_name,code)
        pass1=Password(e_web,e_name,e_pass)
        data=pass1
        new_pass.writelines(f'{pass1}')
    new_pass.close()
old=open('database.txt','r')
new=open('databasenew.txt','a')
while True:
    o_mail=old.readline()
    print (o_mail)
    if not o_mail:
        break
    new.writelines(f"{o_mail[:-2]}\n")
old.close()
new.close()
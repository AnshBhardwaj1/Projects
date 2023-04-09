data_all=open('college_mail_database.txt','r')
data_all=data_all.readlines()
mail_fin=[]
da=open('final_mail.txt','w')
for i in data_all:
    end_gone=(i[:-4])
    fin=end_gone[2:]
    mail_fin.append(fin)
    da.writelines(f"{fin}\n")
da.close()
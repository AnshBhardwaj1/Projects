from click import clear
def Choose (dir):
    fdata=open(f'{dir}','r')
    import random
    names=[]
    while True:
        name = fdata.readline()
        if not name:
            break
        else:    
            names.append(name[:-1])
    num=random.randint(0,len(names)-1)
    fdata.close()
    return (names[num])
name=Choose('5 Hangman/data.txt')
#print (name)
comp=list(name)
compcopy=list(name)
unsolved=[]
hangman=list("HANGMAN")
wrong=-1
for i in comp:
    unsolved.append("X")
while True:
    if unsolved!=comp:
        inp=input("what is your guess : ")
        inp=inp.lower()
        if inp in comp:
            while True:
                if ' ' in compcopy:
                    space=comp.index(' ')
                    compcopy[space]=' '
                    unsolved[space]=' '
                if inp in compcopy:
                    ind=compcopy.index(inp)
                    compcopy[ind]=' '
                    unsolved[ind]=inp
                else:
                    break
            clear()
        else:
            wrong+=1
            clear()
            try:
                hangman[wrong]='x'
                if hangman==['x', 'x', 'x', 'x', 'x', 'x', 'x']:
                    print ("Sorry you lost")
                    print (f"The word was {name}")
                    break
                else:
                    pass
            except:
                print ("You have lost")
        print (*unsolved)
        print (*hangman)
    else:
        print ("Congrats you won")
        print (f"The word was {name}")
        break
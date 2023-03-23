import string
def letter_decrypt(str):
    word=str[3:-3]
    word=word[-1]+word
    word=word[:-1]
    return (word)
def ceaser_decrypt(str,code):
    def dec(let,c):
        global code
        code=c
        alphabet=list(string.ascii_lowercase)
        num=alphabet.index(let)
        return (alphabet[num-c])
    alphabet=list(string.ascii_lowercase)
    alphabet.extend(alphabet)
    code=code%26
    str_lis=list(str)
    code_lis=[]
    for k in range(len(str_lis)):
        code_lis.append(code)
    final=list(map(dec,str_lis,code_lis))
    #print (final)
    final_str=''
    for i in final:
        final_str=final_str+i
    return (final_str)

def decrypt(str,code):
    d_str=ceaser_decrypt(str,code)
    return letter_decrypt(d_str)
if __name__=="__main__":
    #og_str=input("What do you want to encrypt : ")
    og_str="zlxoticibsexbkbeqc"
    print (letter_decrypt(og_str))
    print (decrypt(og_str,1))
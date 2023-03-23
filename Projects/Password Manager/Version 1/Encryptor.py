import random
import string
def letter_encrypt(word):
    alphabet=list(string.ascii_lowercase)
    e_word=word+word[0]
    e_word=e_word[1:]
    for m in range(3):
        ran=random.randint(0,25)
        e_word=e_word+alphabet[ran]
        e_word=alphabet[25-ran]+e_word
    return (e_word)

def ceaser_encrypt(str,code):
    def inc(let,c):
        global code
        code=c
        alphabet=list(string.ascii_lowercase)
        alphabet.extend(alphabet)
        num=alphabet.index(let)
        return (alphabet[num+c])
    alphabet=list(string.ascii_lowercase)
    alphabet.extend(alphabet)
    code=code%26
    str_lis=list(str)
    code_lis=[]
    for k in range(len(str_lis)):
        code_lis.append(code)
    final=list(map(inc,str_lis,code_lis))
    #print (final)
    final_str=''
    for i in final:
        final_str=final_str+i
    return (final_str)
def encrypt(str,code):
    passw=letter_encrypt(str)
    return ceaser_encrypt(passw,code)


if __name__=="__main__":
    og_str=input("What do you want to encrypt : ")
    #print(letter_encrypt(og_str))
    print(encrypt(og_str,1))
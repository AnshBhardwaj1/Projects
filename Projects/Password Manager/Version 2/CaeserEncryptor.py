import string
def ceaser_encrypt(str,code):
    def inc(let,c):
        global code
        code=c
        alphabet=list(string.ascii_lowercase)
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
    final_str=''
    for i in final:
        final_str=final_str+i
    return (final_str)
if __name__=="__main__":
    print(ceaser_encrypt('hello',3))



n=int(input(""))
n_inp=n
nums=[]
nums.append(n_inp)
while True:
    if n==1:

        print (*nums)
        break
        
    if n%2==0:
        n=n/2
        n=int(n)
    else:
        n=(3*n)+1
    
    nums.append(n)
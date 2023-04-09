inp_list=[1,2,3]
print([[i,j,k] for i in inp_list for j in inp_list for k in inp_list if i!=j and j!=k and i!=k])
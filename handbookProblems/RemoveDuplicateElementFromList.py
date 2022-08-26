#4 Remove all duplicates from the list

l = [1, 5, 3, 6, 3, 5, 6, 1]
print("Tha original list is :"+str(l))

res=[]
for i in l:
    if i not in res:
        res.append(i)
print("Tha list after removing is:"+str(res))
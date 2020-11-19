l1=['loku','meda','venkata']
l2=[1,2,3]
p=dict(zip(l1,l2))
print(p)




d={}
for i in l1:
    for j in l2:
        d[i]=j
        l1.remove(i)
print(d)

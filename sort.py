from sys import argv
l=[]
a=[]
b=' '
t=0
for i in argv[1:]:
    l.append(i)
for j in range(0,len(l)):
    for k in range(j+1,len(l)):
        if (l[j] > l[k]):
            t=l[j]
            l[j]=l[k]
            l[k]=t
for o in l:
    if o not in a:
        a.append(o)
        q=b.join(a)
print(q,end=' ')


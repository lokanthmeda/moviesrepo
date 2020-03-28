from sys import argv
l=[]
for i in argv[1:]:
    l.append(i)
for j in l:
    a=j
    output=''
    for k in a:
        if k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            output=output+k
        else:
             m=ord(k)
             a=m-32
             output=output+chr(a)
    print(output,end=' ')
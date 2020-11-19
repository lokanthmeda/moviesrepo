opne_list = ['[','{','(']
close_list = [']','}',')']
def balanced (st):
    s=[]
    for i in st:
        if i in opne_list:
            s.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(s)>0) and (opne_list[pos]==s[len(s)-1])):
                s.pop()
            else:
                return 'unbalanced'
    if len(s) == 0:
        return 'balanced'
    else:
        return 'unbalanced'
st = "{[]{()}}"
print(balanced(st))
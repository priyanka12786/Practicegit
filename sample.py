a = 'aaaabbbccccaaaaaadddd'
l = []
l.append(a[0])
for i in a:
    if l[-1] == i:
        continue
    else:
        l.append(i)
print(l)

g = 0
st = ""
for j in l:
    a = a[g:]                                     #['a', 'b', 'c', 'a', 'd']              a = 'aaaabbbccccaaaaaadddd'
    g = 0
    for i in a:
        if i == j:
            g = g+1
        else:
            break
    st = st+j+str(g)
print(st)










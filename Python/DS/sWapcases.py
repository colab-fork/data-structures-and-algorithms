A = 'ShahidZ  2'
L = []
for i in A:
    if i.islower() == True:
        L.append(i.upper())
    elif i.isupper() == True:
        L.append(i.lower())
    else:
        L.append(i)
print("".join(L))

def accum(s):
    lst = []
    for i,c in enumerate(s):
        s = ''
        for i in range(0,i+1):
            s += c
        lst.append(s)
    print(lst)
    lst1 = [i.capitalize() for i in lst]

    print("-".join(lst1))

accum("HbideVbxncC")
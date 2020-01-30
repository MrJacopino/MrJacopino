from ast import literal_eval
mainlist=[[]]
line=[]
f=a=o=0
with open('listtxt.txt') as f:
    mainlist = [list(literal_eval(line)) for line in f]
while a!=1:
    n=int(input(mainlist[o][0]+': '))
    if n==1:
        a=int(mainlist[o][3])
        if a==1:
            print(mainlist[o][5])
        o=int(mainlist[o][1])
    else:
        a=int(mainlist[o][4])
        if a==1:
            print(mainlist[o][6])
        o=int(mainlist[o][2])

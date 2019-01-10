pob=[]
clas=[]
ball=[]
pobalg=str()
pobgeom=str()
italg=int(0)
itgeom=int(0)
f = open('mat_dv.txt')
for line in f:
    s=line.split()
    rez=int(int(s[3])+int(s[4]))
    classs=str(s[2])
    ima=str(s[0]+' '+s[1])
    if(clas.count(classs)==0):
        clas.append(classs)
        pob.append(ima)
        ball.append(rez)
    else:
        c=clas.index(classs)
        if(rez>ball[c]):
            pob[c]=ima
            ball[c]=rez
        elif(rez==ball[c]):
            pob[c]=pob[c]+ima

    alg=int(s[3])
    geom=int(s[4])
    ima1=str(s[0]+' '+s[1]+' '+s[2])

    if(italg<alg):
        pobalg=ima1
        italg=alg
    elif(italg==alg):
        pobalg=pobalg+' '+ima1

    if(itgeom<geom):
        itgeom=geom
        pobgeom=ima1
    elif(itgeom==geom):
        pobgeom=pobgeom+' '+ima1


for i in range(0,len(pob)):
    print(clas[i],'',ball[i],'',pob[i])
print()
print("алгебра :")
print(pobalg)
print()
print("геометрия :")
print(pobgeom)



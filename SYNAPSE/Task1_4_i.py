import random
def simulateMatch(a,b,c,d,nam1,nam2,b1,b2,li,sc,a1,a2):  #heigher elo,lower elo,lower elo tenacity,heigher elo tenacity,heigher elo name,lower elo name,heigher elo boring,lower elo boring
    k=0
    l=0
    if ((a-b)>=100):
        k=li.index(nam1,a1,a,d,b1) 
        sc[k]=sc[k]+1
        return sc #"Courage the Cowardly Dog",25,1000.39,1000,False
    
    elif ( ((a-b)<100 ) and ((b1==True) or (b2==True)) ) :
        k=li.index(nam1,a1,a,d,b1)
        l=li.index(nam2,a2,b,c,b2)
        sc[k]=sc[k]+0.5
        sc[l]=sc[l]+0.5
        return sc
    
    elif ((a-b)>50 and (a-b)<100):
        r=[1,2,3,4,5,6,7,8,9,10]
        num=random.choice(r)
        if (num*c>a):
            l=li.index(nam2,a2,b,c,b2)
            sc[l]=sc[l]+1
            return sc
        else:
            k=li.index(nam1,a1,a,d,b1)
            sc[k]=sc[k]+1
            return sc
        
    elif (a-b)<=50:
        if (d>c):
            l=li.index(nam2,a2,b,c,b2)
            sc[l]=sc[l]+1
            return sc
        elif (c>d):
            k=li.index(nam1,nam1,b1)
            sc[k]=sc[k]+1
            return sc

list=[["Courage the Cowardly Dog",25,1000.39,1000,False],["Princess Peach",23,945.65,50,True],["Walter White",50,1650.73,750,False],["Rory Gilmore",16,1700.87,500,False],["Anthony Fantano",37,1400.45,400,True],["Beth Harmon",20,2500.34,150,False]]
score=[0,0,0,0,0,0]
z=1
for i in range(6):
    a=0.00
    b=0.00
    c=0
    d=0
    nam1=""
    nam2=""
    b1=""
    b2=""
    for k in range(6):
        if(i!=k):
            if(int(list[i][2])>=int(list[k][2])): 
                a=list[i][2]
                b=list[k][2]
                c=list[k][3]
                d=list[i][3]
                nam1=list[i][0]
                nam2=list[k][0]
                b1=list[i][4]
                b2=list[k][4]
                age1=list[i][1]
                age2=list[k][1]
            else:
                b=list[i][2]
                a=list[k][2]
                d=list[k][3]
                c=list[i][3]
                nam2=list[i][0]
                nam1=list[k][0]
                b2=list[i][4]
                b1=list[k][4]
                age2=list[i][1]
                age1=list[k][1]
            s=simulateMatch(a,b,c,d,nam1,nam2,b1,b2,list,score,age1,age2)
            print(s)
import random
class ChessPlayer:
    name=["Courage the Cowardly Dog","Princess Peach","Walter White","Rory Gilmore","Anthony Fantano","Beth Harmon "]
    age=[25,23,50,16,37,20]
    elo=[1000.39,945.65,1650.73,1700.97,1400.45,2500.34]
    tenacity=[1000,50,50,750,500,400,150]
    isBoring_factor=["False","True","False","False","True","False"]
    sc=[0,0,0,0,0,0]

    def simulateMatch(a,b,t1,t2,b1,b2,s,el):
        if ((a-b)>=100):
            k=el.index(a) 
            s[k]=s[k]+1
            return s #"Courage the Cowardly Dog",25,1000.39,1000,False
    
        elif ( ((a-b)<100 ) and ((b1==True) or (b2==True)) ) :
            k=el.index(a)
            l=el.index(b)
            s[k]=s[k]+0.5
            s[l]=s[l]+0.5
            return s
    
        elif ((a-b)>50 and (a-b)<100):
            r=[1,2,3,4,5,6,7,8,9,10]
            num=random.choice(r)
            if (num*t2>a):
                l=el.index(b)
                s[l]=s[l]+1
                return s
            else:
                k=el.index(a)
                s[k]=s[k]+1
                return s
            
        elif (a-b)<=50:
            if (t2>t1):
                l=el.index(b)
                s[l]=s[l]+1
                return s
            elif (t1>t2):
                k=el.index(a)
                s[k]=s[k]+1
                return s
    
    for i in range(6):
        for k in range(6):
            if (i!=k):
                if (elo[i]>elo[k]):
                    aT=elo[i]
                    bT=elo[k]
                    t1T=tenacity[i]
                    t2T=tenacity[k]
                    b1T=isBoring_factor[i]
                    b2T=isBoring_factor[k]
                else:
                    bT=elo[i]
                    aT=elo[k]
                    t2T=tenacity[i]
                    t1T=tenacity[k]
                    b2T=isBoring_factor[i]
                    b1T=isBoring_factor[k]
                simulateMatch(aT,bT,t1T,t2T,b1T,b2T,sc,elo,k)

    print(l)

    

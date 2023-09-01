import random
class ChessPlayer:
    name=["Courage the Cowardly Dog","Princess Peach","Walter White","Rory Gilmore","Anthony Fantano","Beth Harmon "]
    age=[25,23,50,16,37,20]
    elo=[1000.39,945.65,1650.73,1700.97,1400.45,2500.34]
    tenacity=[1000,50,50,750,500,400,150]
    isBoring_factor=["False","True","False","False","True","False"]
    sc=[0.0,0.0,0.0,0.0,0.0,0.0]

    def simulateMatch(n,a,e,t,b,s):
        for i in range (6):
            for k in range (6):
                if (i!=k):
                    if ((e[i]-e[k])>100):
                        s[i]=s[i]+1
                    if ((e[k]-e[i])>100):
                        s[k]=s[k]+1

                    elif ( (abs(e[i]-e[k])<100 ) and ((b[i]==True) or (b[k]==True)) ):
                        s[k]=s[k]+0.5
                        s[i]=s[i]+0.5
                
                    elif (abs(e[i]-e[k])>50 and abs(e[i]-e[k])<100):
                        r=[1,2,3,4,5,6,7,8,9,10]
                        num=random.choice(r)
                        if (e[i]>e[k]):
                            if ((num*(t[k])) >= e[i]):
                                s[k]=s[k]+1
                            else:
                                s[i]=s[i]+1
                        else:
                            s[i]=s[i]+1
                        
                    elif abs(e[i]-e[k])<50:
                        if (t[k]>t[i]):
                            s[k]=s[k]+1
                        elif (t[i]>t[k]):
                            s[i]=s[i]+1
        return s
    
    o=simulateMatch(name,age,elo,tenacity,isBoring_factor,sc)

    from tabulate import tabulate
    mydata=[]
    # assign data
    for k in range(6):
        mydata.append([name[k],o[k]])
    
    # create header
    head = ["Name", "Score"]
    
    # display table
    print(tabulate(mydata, headers=head, tablefmt="grid"))
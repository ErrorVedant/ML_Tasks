lst=['0001', '0011', '0101', '1011', '1101', '1111']
num=[]
for k in range(len(lst)):
    a=int(lst[k])
    sum=0
    for i in range(4):
        r=a%10
        sum=sum+r*pow(2,i)
        a=int(a/10)
    num.append(sum)

num.sort()
print(num)

sT=0
for k in range(len(num)):
    sT=sT+num[k]
sT=sT/2

for z in range(len(num)-2):
    t1=0
    t2=0
    d=abs(sT-num[t1]-num[t2])
    # print(len(num))
    for k in range(len(num)):
        for i in range(len(num)):
            if (i!=k):
                if (abs(sT-num[k]-num[i])<=d) and (num[k]+num[i]<=sT):
                    d=sT-num[k]-num[i]
                    t1=k
                    t2=i
                    s=num[k]+num[i]
    # print(s)
    # print(t1)
    # print(t2)
    if(t1>t2):
        num.pop(t1)
        num.pop(t2)
    elif(t2>t1):
        num.pop(t2)
        num.pop(t1)
    num.append(s)
    num.sort()
    print(num)

y=num[1]-num[0]
print(f"Therefore the diffrence is {y}")
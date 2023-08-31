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
print(num)

for z in range(len(num)-2):
    t1=0
    t2=0
    s=num[0]+num[1]
    # print(len(num))
    for k in range(len(num)):
        for i in range(len(num)):
            if(k!=i):
                j=num[k]+num[i]
                if (s>=j):
                    s=num[k]+num[i]
                    t1=k
                    t2=i
    # print(s)
    # print(t1)
    # print(t2)
    num.pop(t2)
    num.pop(t1-1)
    num.append(s)
    print(num)


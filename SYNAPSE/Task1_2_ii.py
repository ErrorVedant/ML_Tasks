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
    s=num[0]+num[2]
    num.pop(0)
    num.pop(2)
    num.append(s)
    num.sort()
    print(num)


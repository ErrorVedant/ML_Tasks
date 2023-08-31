# R=input("Enter the number of rows")
# r=int(R)
# encoded_lists=[]
# for i in range(r):
#     C=input(f"Enter the number of colm in row {1+i}")
#     c=int(C)
#     for k in range(c):
#         encoded_lists.append(int(input(f"({i},{k}) element:")))  #append is used to add element and extend is used to combine 2 lists

encoded_lists=[[1,2,3,4,6],[5,7,8,9,15],[12,14,16,18],[10,11,12,13,16,17,18,20]]

def explode_chains(a):
    sub=[]
    for i in range(len(a)):
        for k in range(1,len(a[i])):
            u=0
            u=a[i][k]-a[i][k-1]
            sub.append(u)
        print(sub)
        l=0
        t=0

        for k in range(len(sub)):
            while(sub[k]==1):
                l=l+1
                t=k

        if (l>=2):
            del a[l-(t+1):t+1]

        sub=[]
    print(a)

explode_chains(encoded_lists)
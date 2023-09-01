encoded_list = [[1,2,3,4,6],[5,7,8,9,15],[12,14,16,18],[10,11,12,13,16,17,18,20]]

def explode_chains(encoded_list):
    for lst in encoded_list:
        n = len(lst)
        for i in range(n-2):
            if ((n>2) and (lst[i+1] == lst[i]+1) and (lst[i+2] == lst[i+1]+1) ):
                lst.pop(i+2)
                lst.pop(i+1)
                lst.pop(i)
                n =n- 3
    return encoded_list

result = explode_chains(encoded_list)
print(result)
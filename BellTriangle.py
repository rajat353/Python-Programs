n=int(input("enter a number"))

list=[[1]]
temp=[];

for i in range(0,n):
    for j in range(0,i+1):
        if i==0 and j==0:
            continue
            
        if j==0 and i!=0:
            temp=[];
            temp.append(list[i-1][i-1])
            
            
        else:
            temp.append(list[i-1][j-1]+temp[j-1])
            
    if i!=0:
        list.append(temp)    

for i in range(0,n):
    print (list[i])
    i+=1

s=str(input())
q=int(input())
u=0
if len(s) in range(1,31) and q in range(1,11):
    temp1=str(s)
    k='h'
    
    for i in range(q):
        d,r=ord(input()),int(input())
        if d==76:
            for j in range(r):
                temp2=temp1[r:len(temp1)]
                temp2=temp2+temp1[0:r]
                
                
            k=k+str(temp2[0])
            print(k)
            temp1=str(temp2)
            print(temp1)
                                 
        elif d==82:
            for i in range(r):
                temp3=temp1[len(temp1)-1]
                temp1=temp3+temp1[0:len(temp1)-1]
                
                
            k=k+str(temp1[0])
            
            print(k)
            print(temp1)
    k=k[1:]
    print(k)
    for i in range(0,(len(s)-len(k))):
        temp=s[i:i+len(k)]
        if k==temp:
            u=1
            
    if u==1:
        print('YES')
    else:
        print('NO')
        
        
    

                
    
    
    

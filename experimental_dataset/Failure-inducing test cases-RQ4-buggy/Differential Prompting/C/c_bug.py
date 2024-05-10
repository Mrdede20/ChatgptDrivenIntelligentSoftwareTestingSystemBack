n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    maxx=max(l)
    m2=0
    for i in range(len(l)):
        if l[i]<maxx:
            m2=max(m2,l[i])
    if m2==0:
        m2=maxx
    if len(l)<2:
        print(l[0])
    else:
        for i in range(len(l)):
            if l[i]==maxx:
                l[i]=l[i]-m2
            else:
                l[i]=l[i]-maxx
        print(*l)
    
    
            
        
                
        

    
                  
                
            
        
            
        
        

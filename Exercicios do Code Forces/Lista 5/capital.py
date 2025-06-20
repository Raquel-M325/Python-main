a1,a2,a3,a4=map(int,input().split())
 
t1=a1*a4
t2=a2*a3
t3=a1*a3
t4=a2*a4
t5=a1*a2
t6=a3*a4
 
if t1==t2 or t3==t4 or t5==t6:
    print('S')
else:
    print('N')
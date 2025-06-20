a1=int(input())
a2=int(input())
a3=int(input())
 
t1=(a1*4)+(a2*2)
t2=(a1*2)+(a3*2)
t3=(a3*4)+(a2*2)
 
maior=t1
menor=t2
meio=t3
 
if t2>maior:
    maior=t2
if t3>maior:
    maior=t3
 
if t1<menor:
    menor=t1
if t3<menor:
    menor=t3
 
meio=t1+t2+t3-(maior+menor)
 
print(menor)
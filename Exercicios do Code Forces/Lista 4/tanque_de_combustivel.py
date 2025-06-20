c = int (input())
d = int(input())
t = int(input())

r = float(d/c)
if r < t:
    menor = r // t
    print ('{:.1f}'.format(menor))
else:
    rr = r - t
    print ('{:.1f}'.format(rr))
    
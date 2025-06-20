d = int(input())
v = int(input())
h = d // v
m = (d % v) * 60 // v
print ('{:02d}:{:02d}'.format(h,m))
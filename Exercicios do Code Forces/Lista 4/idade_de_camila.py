nv = int(input())
nm = int(input())
nn = int(input())

if nv > nm > nn:
    print (nm)
elif nv < nm < nn:
    print (nm)
elif nv == nm == nn:
    print (nm)
elif nv == nm < nn:
    print (nm)
elif nv == nm > nn:
    print (nm)
elif nm == nn < nv:
    print (nm)
elif nm == nn > nn:
    print(nm)
elif nv < nm == nn:
    print(nm)
elif nm > nv > nn:
    print (nv)
elif nm < nv < nn:
    print (nv)
elif nn == nv > nm:
    print (nv)
elif nn == nv < nm:
    print (nv)
elif nm > nn > nv:
    print (nn)
elif nm < nn < nv:
    print (nn)

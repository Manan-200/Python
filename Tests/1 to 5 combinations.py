counter = 0
print ("pairs of 1,2,3,4,5 are:")
for a in range (1,6):
    for b in range (1,6):
        for c in range (1,6):
            for d in range (1,6):
                for e in range (1,6):
                    if a + b + c + d + e == 15 and a*b*c*d*e == 120:
                        counter = counter + 1
                        print ((10000*a)+(1000*b)+(100*c)+(10*d)+(1*e),"counter:",counter)
#346/40/41
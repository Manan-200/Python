x = int(input("Enter number of pythagorean triplets needed:"))
counter = 0
for a in range (1,1000):
    for b in range (1,1000):
        for c in range (1,1000):
            if a**2 + b**2 == c **2 and counter <= x:
                counter += 1
                print (a,b,c,"Counter:",counter)
            elif counter == x:
                break

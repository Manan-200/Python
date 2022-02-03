vars = int(input("Enter number of variables(1 to 3):"))
lhs = (input("Enter LHS:"))
rhs = (input("Enter RHS:"))
print ("vals of x, y, z between -100 and 100:")
for x in range (-100,101):
        for y in range (-100,101):
                for z in range (-100,101):
                        LHS = eval(lhs)
                        RHS = eval(rhs)
                        if LHS == RHS and vars == 1:
                               print ("x:",x)
                        elif LHS == RHS and vars == 2:
                                print ("x:",x,"y:",y)
                        elif LHS == RHS and vars == 3:
                                print ("x:",x,"y:",y,"z:",z)
p=float(input("Enter the priciple amount"))
r=float(input("Enter the rate of interest"))
t=float(input("Duration in years"))

SI=(p*r*t)/100
CI=p*((1+(r/100))**t)

type=int(input("Simple interest or Compound interest(1/0)?"))

if type == 1:
    print("Simple interest is",SI)
    
elif type == 0:
    print ("Compound insterest is",CI)

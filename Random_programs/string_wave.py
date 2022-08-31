string = input("Enter string: ")
waves = int(input("Enter number of waves: "))
wavelength = 10
spaces = 0
for w in range(waves):
    for i in range(wavelength):
        for _ in range(spaces):
            print(" ", end="")
        print(string)
        spaces += 1
    for i in range(wavelength - 1):
        for _ in range(spaces):
            print(" ", end = "")
        print(string)
        spaces -= 1
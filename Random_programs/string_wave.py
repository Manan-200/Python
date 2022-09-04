string = input("Enter string: ")
waves = int(input("Enter number of waves: "))
wavelength = 10
counter = 0

def calc_spaces(wl, counter):
    pos = counter%(wl*2)
    spaces = wl - abs(wl - pos)
    return(spaces)

for i in range(waves):
    for counter in range(wavelength*2):
        spaces = calc_spaces(wavelength, counter)
        for _ in range(spaces):
            print(" ", end="")
        print(string)
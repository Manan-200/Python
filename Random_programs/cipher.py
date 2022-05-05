msg = input("Enter message to cipher: ")
ciphered = ""

for letter in msg:

    ciphered_letter = letter

    if ord(letter) >= ord("a") and ord(letter) <= ord("z"):
        dist = ord(letter) - ord("a")
        ciphered_letter = chr(ord("z") - dist)

    ciphered += ciphered_letter

print(f"Ciphered word is: {ciphered}")
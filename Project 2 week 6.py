encryptedText = input("Enter the encrypted text: ")
distance = int(input("Enter the distance value: "))
decryptedtext = ""
for ch in encryptedText:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < 32:
        cipherValue = 127 - (32 - cipherValue)
    decryptedtext += chr(cipherValue)
print("Plain text: ", decryptedtext)

gesloten_letters = {'A': 1, 'B': 2, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1}
uiteinden_letters = {'A': 2, 'C': 2, 'E': 3, 'F': 3, 'G': 2, 'H': 4, 'I': 2, 'J': 2, 'K': 4, 'L': 2, 'M': 2, 'N': 2, 'P': 1, 'Q': 2, 'R': 2, 'S': 2, 'T': 3, 'U': 2, 'V': 2, 'W': 2, 'X': 4, 'Y': 3, 'Z': 2}

a = input("Woord: ").upper()
b = 0
c = 0

for letter in a:
    # Controleer of de letter in de lijst met uiteinden staat
    if letter in uiteinden_letters:
        b += uiteinden_letters[letter]
    if letter in gesloten_letters:
        c += 1

print(c)     
print(b)

woord = input("woord: ")
verschuiving = int(input("verschuiving: "))
output = ''

alfabet1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in woord:
    if letter in alfabet1:
        index = alfabet1.index(letter)
        nindex = (index + verschuiving) % 26
        output += alfabet1[nindex]
    elif letter in alfabet:
        index = alfabet.index(letter)
        nindex = (index + verschuiving) % 26
        output += alfabet[nindex]

print(output)
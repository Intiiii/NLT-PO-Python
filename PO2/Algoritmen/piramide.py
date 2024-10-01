while True:
    hoogte = int(input("Hoe hoog moet de piramide zijn? "))
    if 1 <= hoogte <= 23:        
        for i in range(hoogte):
            b = hoogte-i-1
            a = i+2
            print("  "*b +"# "*a)
        break

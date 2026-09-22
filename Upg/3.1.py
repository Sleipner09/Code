minuter = float(input("Hur många minuter uppskattar du att kommer att ringa per månad"))

if minuter <= 33:
    print("Du bör välja abonemanget: Kontant")
    
elif minuter <= 66:
    print("Du bör välja abonemanget: Normal")
    
else:
    print("Du bör välja abonemanget: Plus")

tal_lista = []

while True:
    tal = float(input("Skriv in ett tal: "))
    
    if tal < 0: 
        break
    
    tal_lista.append(tal)

if tal_lista:
    största = max(tal_lista)
    minsta = min(tal_lista)
    print(f"Det strörsta talet är {största}")
    print(f"Det minsta talet är {minsta}")
else:
    print("inga positiva tal matades in")
    
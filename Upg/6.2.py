tal_lista = []

print("Mata in valfritt antal heltal (om klar = enter)")

while True:
    inmatning = input("Ange ett heltal: ")
    
    if inmatning == "":
        break
    
    tal_lista.append(int(inmatning))
    
antal_negativa = 0
for tal in tal_lista:
    if tal < 0:
        antal_negativa
        
print(f"\nDu matade in {len(tal_lista)} tal totalt.")
print(f"Antal tal som är mindre än noll: {antal_negativa}")

text = input("skriv in en text: ").strip().lower()

if len(text) > 0 and text[0] == text[-1]:
    print("Första och sista bokstaven är samma")
else:
    print("Första och sista bokstaven är inte samma")
    
    
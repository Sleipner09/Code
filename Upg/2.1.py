mätarställning = int(input("Vad är dagens mätarställning?"))
mätarställning_för_ett_år_sedan = int(input("Vad var mätarställningen för ett år sedan?"))
antal_liter_bensin = int(input("Hur många liter bensin har förbrukats under året?"))

antal_körda_mil = mätarställning - mätarställning_för_ett_år_sedan
förbrukning_per_mil = antal_liter_bensin / antal_körda_mil

print("mätarställning idag", mätarställning)
print("mätarställning för ett år sedan", mätarställning_för_ett_år_sedan)
print("antal körda mil", antal_körda_mil)
print("antal liter bensin", antal_liter_bensin)
print("förbrukning per mil", förbrukning_per_mil)

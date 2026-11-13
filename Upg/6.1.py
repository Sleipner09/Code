forsta_talet = 2
k = 3 
antal_tal = 10

talfoljd = [forsta_talet]

for i in range(antal_tal - 1):
    nasta_tal = talfoljd[-1] * k
    talfoljd.append(nasta_tal)

print(talfoljd)
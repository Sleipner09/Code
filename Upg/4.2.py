print(f"{'Tal':<6} {'Kvadrat':<10} {'kub':<10}")
print("-" * 28)

for tal in range(1, 13):
    kvadrat = tal ** 2
    kub = tal **3
    print(f"{tal:<6} {kvadrat:<10} {kub:<10}")
    
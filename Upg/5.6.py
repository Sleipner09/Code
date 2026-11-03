a = input("skriv ett svenskt datum som åå/mm/dd: ")
månad = a [3:5]
dag = a[6:]
år = a[:2]
s = "20" + månad + "-" + dag + "-" + år
print("Amerikanskt datum: " + s)

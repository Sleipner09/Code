ålder = int(input('hur gammal är du?'))

if ålder == 17:
    print('Du är lika gammal som de flesta i EE25')

if ålder != 43:
    print('Du är inte lika gammal som per')
else:
    print('Du är lika gammal som per')
    
if ålder <= 13:
    print('Du är väldigt ung')
elif ålder < 18:
    print('Du får inte ta körkort')
elif ålder > 18:
    print('Du får ta körkort')
elif ålder > 20:
    print('Du får handla på systembolaget.')
    
namn = input('vad är ditt namn')
    
if namn == 'Per':
    print('Kung')
elif namn == 'Pär':
    print('Så stavar man inte!')
else: print('Varför heter du inte Per?')

if ålder == 43 & namn == 'Per':
    print('Du måste vara Per Hagfors')
    
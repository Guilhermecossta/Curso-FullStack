clima = float(input('Qual a temperatura? '))
if clima < 15:
    print('Frio')
elif clima >= 15 and clima <= 30:
    print('Ameno')
else:
    print('Quente')
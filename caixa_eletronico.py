valor = int(input('Digite o valor em R$: '))
while True:
    if(valor >= 100):
        cedula100 = valor // 100
        valor = valor - cedula100 * 100
        print('Cédulas de 100: {}' .format(cedula100))
        if not valor:
            break
    if(valor >= 50):
        cedula50 = valor // 50
        valor = valor - cedula50 * 50
        print('Cédulas de 50: {}' .format(cedula50))
        if not valor:
            break
    if(valor >= 20):
        cedula20 = valor // 20
        valor = valor - cedula20 * 20
        print('Cédulas de 20: {}' .format(cedula20))
        if not valor:
            break
    if(valor >= 10):
        cedula10 = valor // 10
        valor = valor - cedula10 * 10
        print('Cédulas de 10: {}' .format(cedula10))
        if not valor:
            break
    if(valor >= 5):
        cedula5 = valor // 5
        valor = valor - cedula5 * 5
        print('Cédulas de 5: {}' .format(cedula5))
        if not valor:
            break
    if (valor >= 2):
        cedula2 = valor // 2
        valor = valor - cedula2 * 2
        print('Cédulas de 2: {}'.format(cedula2))
        if not valor:
            break
    if(valor):
        cedula1 = valor
        print('Cédulas de 1: {}' .format(cedula1))
        break
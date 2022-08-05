while True:
    print("""\n1. Decimal a Binario \n2. Binario a Decimal \n3. Salir""")
    opcion = int(input('\nIngrese el número de la opcion: '))
    list_bin = []
    list_dec = []
    binario = '\nEl número en binario es '
    decimal = '\nEl número en decimal es '
    dec = 0
    if opcion == 1:
        num = int(input('\nIngrese un número decimal para convertir a binario: '))

        while num > 0:
            if num % 2 == 0:
                num //= 2
                list_bin.insert(0,0)
            elif num % 2 == 1:
                num //= 2
                list_bin.insert(0,1)
        for i in list_bin:
            binario += str(i)
        print(binario)

    elif opcion == 2:
        num = int(input('\nIngrese un número binario para convertir a decimal: '))
#hacer un detector de que si un digito de la lista es mayor a uno que diga que no es un numero binario
        while True:
            list_dec.append(num%10) 
            num = int(num/10) 
            if num == 0:
                break
        for i , j in zip(range(0,len(list_dec)) , list_dec):
            if j > 1:
                print('\nIngrese un número decimal') 
            else:
                dec += (2**i) * j
        decimal += str(dec)
        print(decimal)
    elif opcion == 3:
        break
    else:
        print('Ingrese un número de opción valido')

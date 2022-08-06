from random import randint
list_pc = []

while True:
    i = randint(0,9) # se escoje un número del 0 al 9
    if i not in list_pc:
        list_pc.append(i) # si no esta en la lista, que se agrege, de otra forma que se repita el ciclo
    if len(list_pc) == 4: # hasta tener 4 dígitos diferentes
        break

while True:
    fijas = 0
    set_pc = set()
    set_us = set()
    list_us = []
    
    while True:
        num_us = int(input('\nIngrese un número de 4 dígitos, los cuales no pueden repetirse: '))

        while True:
            list_us.insert(0, num_us%10) # se coje el ultimo numero ingresado y se agrega en una lista
            num_us = int(num_us/10) # se elimina ese ultimo número ingresado hasta no tener ningun digito
            if num_us == 0:
                break
        if len(list_us) < 4: # esto mira si la lista tiene 3 digitos
            list_us.insert(0,0) # si si, le agrega un cero al inicio

        con = set(list_us)
        if len(con) != 4 or len(list_us) != 4: # se rectifica si no se repite ningun numero 
            list_us.clear() # si se repite algun numero que se borre la lista y que se vuelva a llenar
            print('\nError, el número debe ser de 4 dígitos que no se repitan') 
        
        else:
            break

    if list_us != list_pc:
        for i in range(0,4): # se verifica en cada una de los 4 indices de la lista
            u = list_us[i] # y se comparan para ver si hay algun valor igual con
            p = list_pc[i] # ese mismo indice
            if u == p:
                fijas += 1 # si si lo hay, que se sume uno a las fijas
            else:
                set_pc.add(list_pc[i]) # si no, que se agreguen a unos conjuntos
                set_us.add(list_us[i])
        a = set_pc & set_us # se mire si hay algun número en común entre esos conjuntos
        picas = len(a) # el número de valores similares es el número de picas
        print(f'\nPicas : {picas} , Fijas: {fijas}')
    else:
        print(f'\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\nGanaste, el número era {list_pc}\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n')
        break
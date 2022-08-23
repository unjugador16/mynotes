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

        num_us = input('\nIngrese un número de 4 dígitos, los cuales no pueden repetirse: ')

        cn = 0
        cs = 0
                        #==comandos==#
        if num_us == "clear": #un comando para salir xd
            cs = 1
            break
        if num_us == "numpc": #un comando para mostrar el numero del computador
            print(list_pc)
            cn = 1

        for i in num_us:
            try:
                i = int(i)
            except:
                if cn == 1:
                    continue
                else:
                    print(f"\nError, {i} no es un número")
            list_us.append(i)

        con = set(list_us)
        if len(con) != 4 or len(list_us) != 4: # se rectifica si no se repite ningun numero y que es de 4 digitos 
            if cn == 1:
                continue
            else:
                list_us.clear() # si se repite algun numero que se borre la lista y que se vuelva a llenar
                print('\nError, el número debe ser de 4 dígitos que no se repitan') 
        else:
            break
            
    if cs == 1:
        print('\nSaliendo...\n')
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
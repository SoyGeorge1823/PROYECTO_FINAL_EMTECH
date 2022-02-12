"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""
import os
from os import system
from lifestore_file import lifestore_sales, lifestore_products, lifestore_searches

###COMIENZA PUNTO 1
"""##--------------------------------Mayores ventas------------------------------------------##"""
def punto1():
    ventas_validas=[]; veces_vendido=[];

    veces_vendido=[sale[1]for sale in lifestore_sales ]



    i=0
    for venta in lifestore_products:
        ventas_validas.insert(i,[venta[0],venta[1],veces_vendido.count(venta[0]),venta[-2]]) ##ventas_validas=[ID,Nombre,Veces vendido,categoria]
        i=i+1
    
    ventas_validas.sort(key = lambda x : x[2]  )  
        

    print("Productos mas vendidos \n")
    for i in [-1,-2,-3,-4,-5]:
        print(f"ID:{ventas_validas[i][0]}\t Nombre: {ventas_validas[i][1]} \t Ventas: {ventas_validas[i][2]}")

    """
    """##--------------------------------Mayores búsquedas---------------------------------------##
    busquedas_validas=[]; veces_buscado=[];

    veces_buscado=[busqueda[1]for busqueda in lifestore_searches  ]

    i=0
    for busqueda in lifestore_products:
        busquedas_validas.insert(i,[busqueda[0],busqueda[1],veces_buscado.count(busqueda[0]),busqueda[-2]]) ##ventas_validas=[ID,Nombre,Veces vendido,categoria]
        ##
        i=i+1
    
    busquedas_validas.sort(key = lambda x : x[2]  )  
        

    print("Productos mas buscados \n")
    for i in [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]:
        print(f"ID:{busquedas_validas[i][0]}\t Nombre: {busquedas_validas[i][1]} \t Busquedas: {busquedas_validas[i][2]}")
##Categorias (PUNTO 1)
"""----------------------------------COMIENZA ESPACIO PARA SEGUNDO PUNTO (CATEGORIAS VENTAS)-##"""
def punto2():
    procesadores =[]; tarjetas_de_video =[]; tarjetas_madre=[]; discos_duros=[]; memorias_USB=[]; pantallas =[]; bocinas=[]; audifonos=[]; 

    ##ordenemos todos los productos por categoria contando las veces reseñadas y sumando el total de "puntos" obtenidos para encontrar el promedio del mismo 
    busquedas_validas= []
    veces_resenado=[ventas[1] for ventas in lifestore_sales ]
    calificacion=[ventas[2] for ventas in lifestore_sales ]

    ##vamos a llenar este para poder separar en categorias 
    i=0
    for busqueda in lifestore_products:
        busquedas_validas.insert(i,[busqueda[0],busqueda[1],veces_resenado.count(busqueda[0]),busqueda[-2]])
        i=i+1

    ##primer categoria
    categorias=[item[-2]for item in lifestore_products]
    categorias=list(dict.fromkeys(categorias))

    for item in busquedas_validas:
        if categorias[0]in item:
            procesadores.append(item[:3])
        elif categorias[1] in item:
            tarjetas_de_video.append(item[:3])
        elif categorias[2] in item:
            tarjetas_madre.append(item[:3])
        elif categorias[3] in item:
            discos_duros.append(item[:3])
        elif categorias[4] in item:
            memorias_USB.append(item[:3])
        elif categorias[5] in item:
            pantallas.append(item[:3])
        elif categorias[6] in item:
            bocinas.append(item[:3])
        elif categorias[7] in item:
            audifonos.append(item[:3])
    print("PROCESADORES MENOS VENDIDOS \n")
    procesadores.sort(key = lambda x : x[2]  ) 
    for i in [0,1,2,3,4]:
        print(f'ID: {procesadores[i][0]} \t Nombre: {procesadores[i][1]} \t Veces Vendido: {procesadores[i][2]} \t\n') 

    print("TARJETAS DE VIDEO MENOS VENDIDAS \n")
    tarjetas_de_video.sort(key = lambda x : x[2]  ) 
    for i in [0,1,2,3,4]:
        print(f'ID: {tarjetas_de_video[i][0]} \t Nombre: {tarjetas_de_video[i][1]} \t Veces Vendido: {tarjetas_de_video[i][2]} \t\n')

    print("TARJATAS MADRE MENOS VENDIDAS \n")
    tarjetas_madre.sort(key = lambda x : x[2]  ) 
    for i in [0,1,2,3,4]:
        print(f'ID: {tarjetas_madre[i][0]} \t Nombre: {tarjetas_madre[i][1]} \t Veces Vendido: {tarjetas_madre[i][2]} \t\n')     

    print("LOS DISCOS DUROS MENOS VENDIDOS \n")
    discos_duros.sort(key = lambda x : x[2]  ) 
    for i in [0,1,2,3,4]:
        print(f'ID: {discos_duros[i][0]} \t Nombre: {discos_duros[i][1]} \t Veces Vendido: {discos_duros[i][2]} \t\n')     

    print("MEMORIAS USB MENOS VENDIDAS \n")
    memorias_USB.sort(key = lambda x : x[2]  ) 
    for i in [0,1]:
        print(f'ID: { memorias_USB[i][0]} \t Nombre: { memorias_USB[i][1]} \t Veces Vendido: { memorias_USB[i][2]} \t\n')  

    print("PANTALLAS MENOS VENDIDAS \n")
    pantallas.sort(key = lambda x : x[2]  ) 
    for i in [0,1,2,3,4]:
        print(f'ID: { pantallas[i][0]} \t Nombre: { pantallas[i][1]} \t Veces Vendido: { pantallas[i][2]} \t\n')  

    print("BOCINAS MENOS VENDIDAS \n")
    bocinas.sort(key = lambda x : x[2]  ) 
    for i in [0,1,2,3,4]:
        print(f'ID: { bocinas[i][0]} \t Nombre: { bocinas[i][1]} \t Veces Vendido: { bocinas[i][2]} \t\n') 

    print("AUDIFONOS MENOS VENDIDOS \n")
    audifonos.sort(key = lambda x : x[2]  ) 
    for i in [0,1,2,3,4]:
        print(f'ID: { audifonos[i][0]} \t Nombre: { audifonos[i][1]} \t Veces Vendido: { audifonos[i][2]} \t\n') 

    
    """----------------------------------CATEGORIAS BUSQUEDAS------------------------------------"""

    procesadores =[]; tarjetas_de_video =[]; tarjetas_madre=[]; discos_duros=[]; memorias_USB=[]; pantallas =[]; bocinas=[]; audifonos=[]; 

    ##ordenemos todos los productos por categoria contando las veces reseñadas y sumando el total de "puntos" obtenidos para encontrar el promedio del mismo 
    busquedas_validas= []
    veces_buscado=[busqueda[1] for busqueda in lifestore_searches ]
    calificacion=[ventas[2] for ventas in lifestore_sales ]

    ##vamos a llenar este para poder separar en categorias 
    i=0
    for busqueda in lifestore_products:
        busquedas_validas.insert(i,[busqueda[0],busqueda[1],veces_buscado.count(busqueda[0]),busqueda[-2]])
        i=i+1

    ##primer categoria
    categorias=[item[-2]for item in lifestore_products]
    categorias=list(dict.fromkeys(categorias))

    for item in busquedas_validas:
        if categorias[0]in item:
            procesadores.append(item[:3])
        elif categorias[1] in item:
            tarjetas_de_video.append(item[:3])
        elif categorias[2] in item:
            tarjetas_madre.append(item[:3])
        elif categorias[3] in item:
            discos_duros.append(item[:3])
        elif categorias[4] in item:
            memorias_USB.append(item[:3])
        elif categorias[5] in item:
            pantallas.append(item[:3])
        elif categorias[6] in item:
            bocinas.append(item[:3])
        elif categorias[7] in item:
            audifonos.append(item[:3])

    procesadores.sort(key = lambda x : x[2]  ) 
    print("LOS PROCESADORES MENOS BUSCADOS \n")
    for i in range(9):##no existe un 10mo procesador 
        print(f'ID: {procesadores[i][0]} \t Nombre: {procesadores[i][1]} \t Veces Buscado: {procesadores[i][2]} \t\n') 


    tarjetas_de_video.sort(key = lambda x : x[2]  ) 
    print("LAS TARJETAS DE VIDEO MENOS BUSCADAS\n")
    for i in range(10):
            print(f'ID: {tarjetas_de_video[i][0]} \t Nombre: {tarjetas_de_video[i][1]} \t Veces Buscado: {tarjetas_de_video[i][2]} \t\n') 


    tarjetas_madre.sort(key = lambda x : x[2]  ) 
    print("LAS TARJETAS DE VIDEO MENOS BUSCADAS\n")
    for i in range(10):
        print(f'ID: {tarjetas_madre[i][0]} \t Nombre: {tarjetas_madre[i][1]} \t Veces Buscado: {tarjetas_madre[i][2]} \t\n')     

    discos_duros.sort(key = lambda x : x[2]  ) 
    print("LOS DISCOS DUROS MENOS BUSCADOS\n")
    for i in range(10):
        print(f'ID: {discos_duros[i][0]} \t Nombre: {discos_duros[i][1]} \t Veces Buscado: {discos_duros[i][2]} \t \n')     

    memorias_USB.sort(key = lambda x : x[2]  ) 
    print("LAS MEMORIAS USB MENOS BUSCADAS\n")
    for i in range(2):##no existen mas de 2 en la categoria 
        print(f'ID: { memorias_USB[i][0]} \t Nombre: { memorias_USB[i][1]} \t Veces Buscado:: { memorias_USB[i][2]} \t\n')  

    pantallas.sort(key = lambda x : x[2]  ) 
    print("LAS PANTALLAS MENOS BUSCADAS\n")
    for i in range(10):
        print(f'ID: { pantallas[i][0]} \t Nombre: { pantallas[i][1]} \t Veces Buscado: { pantallas[i][2]} \t\n')  

    bocinas.sort(key = lambda x : x[2]  ) 
    print("LAS BOCINAS MENOS BUSCADAS\n")
    for i in range(10):
        print(f'ID: { bocinas[i][0]} \t Nombre: { bocinas[i][1]} \t Veces Buscado: { bocinas[i][2]} \t\n') 

    audifonos.sort(key = lambda x : x[2]  ) 
    print("LOS AUDIFONOS MENOS BUSCADOS\n ")
    for i in range(10):
        print(f'ID: { audifonos[i][0]} \t Nombre: { audifonos[i][1]} \t Veces Vendido: { audifonos[i][2]} \t\n') 
###TERMINA EL PRIMER PUNTO SOLICITADO
###COMIENZA PUNTO 3
"""----------------------------------PRODUCTOS POR RESEÑA DE PRODUCTO------------------------##"""
# Diccionario de reviews por id"""ALIAS EL PUNTO 3""""
def products_por_resena():

    prods_reviews = {}
    for sale in lifestore_sales:
        prod_id = sale[1]
        review = sale[2]
        if prod_id not in prods_reviews.keys():
            prods_reviews[prod_id] = []
        prods_reviews[prod_id].append(review)


    id_rev_prom = {}
    for id, reviews in prods_reviews.items():
        # print(id, reviews)
        rev_prom = sum(reviews) / len(reviews)
        rev_prom = int(rev_prom*100)/100
        id_rev_prom[id] = [rev_prom, len(reviews)]

    # Para ordenar siempre es mas facil usar listas.
    dicc_en_list = []
    for id, lista in id_rev_prom.items():
        # print(id, rev_prom)
        rev_prom = lista[0]
        cant = lista[1]
        sub = [id, rev_prom, cant]
        dicc_en_list.append(sub)


    def seg_elemnto(sub):
        return sub[1]

    dicc_en_list = sorted(dicc_en_list, key=seg_elemnto, reverse=True)
    # dicc_en_list = sorted(dicc_en_list, key=lambda lista:lista[2], reverse=True)

    # for sublista in dicc_en_list:
    #     print(sublista)
    """PRODUCTOS CON LA PEOR RESEÑA"""
    print("PRODUCTOS POR LA RESEÑA MAS BAJA\n ")

    for sublista in dicc_en_list[-5:]:
        id, rev, num = sublista
        indice_lsp = id - 1
        prod = lifestore_products[indice_lsp]
        nombre = prod[1]
        nombre = nombre.split(' ')
        nombre = ' '.join(nombre[:4])
        
        print(f'El producto "{nombre}":\trev_prom: {rev}\t num de ventas: {num}\n')

        """PRODUCTOS CON LA MEJOR RESEÑA """
    print("PRODUCTOS POR LA RESEÑA MAS ALTA\n ")

    for sublista in dicc_en_list[:5]:
        id, rev, num = sublista
        indice_lsp = id - 1
        prod = lifestore_products[indice_lsp]
        nombre = prod[1]
        nombre = nombre.split(' ')
        nombre = ' '.join(nombre[:4])
        
        print(f'El producto "{nombre}":\trev_prom: {rev} \tnum de ventas: {num}\n')
###COMIENZA PUNTO 4 (TOTAL VENTAS)
# Ventas por categorias TOTALES
"""##----------------------------------VENTAS TOTALES Y PROM (MES)---------------------------##"""
# Dividir por meses las ventas
def ventas_totales_men():
# Dividir por meses las ventas
    id_fecha = [ [sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0 ]
    # Para categorizar usamos un diccionario
    categorizacion_meses = {}

    for par in id_fecha:
        # Tengo ID y Mes
        id = par[0]
        _, mes, _ = par[1].split('/')
        # Si el mes aun no existe como llave, la creamos
        if mes not in categorizacion_meses.keys():
            categorizacion_meses[mes] = []
        categorizacion_meses[mes].append(id)

    # mes : [ids de venta]

    # for key in categorizacion_meses.keys():
    #     print(key)
    #     print(categorizacion_meses[key])

    # crear dic
    mes_info = {}
    for mes, ids_venta in categorizacion_meses.items():
        lista_mes = ids_venta
        suma_venta = 0
        
        for id_venta in lista_mes:
            indice = id_venta - 1
            info_venta = lifestore_sales[indice]
            id_product = info_venta[1]
            info_prod = lifestore_products[id_product-1]
            precio = info_prod[2]
            suma_venta += precio
            
            prom= len(lista_mes)/30
            prom=round(prom, 2)
        
        mes_info[mes] = [suma_venta, len(lista_mes),prom]


    mes_ganancia_ventas = []

    for mes, datos in mes_info.items():
        ganancias,ventas, prom  = datos
        sub = [mes, ganancias,ventas,prom]
        mes_ganancia_ventas.append(sub)


    vent_tot = []
    for total in mes_ganancia_ventas:
        vent_tot.append(total[1])
    suma= 0
    for x in vent_tot:
        suma += x


    print("TOTAL ANUAL:",suma ,"\n")

    ord_mes = sorted(mes_ganancia_ventas)
    ord_ganancia = sorted(mes_ganancia_ventas, key=lambda x:x[1], reverse=True)
    ord_ventas = sorted  (mes_ganancia_ventas, key=lambda x:x[2], reverse=True)

    print("DATOS MENSUALES TOTALES \n")
    for producto in ord_mes:
            print(f'Mes: {producto[0]} \t Ganancias: {producto[1]} \t Productos vendidos: {producto[2]} \t Promedio ventas mensual: {producto[3]} \t\n  ') 

    print("LOS MESES CON MAS VENTAS SON  \n")
    for producto2 in ord_ganancia:
            print(f'Mes: {producto2[0]} \t Ganancias: {producto2[1]} \t Productos vendidos: {producto2[2]} \t \n  ') 



"""##--------------------------------LOGIN---------------------------------------------------##"""
def login():
    username="Admin"
    password='Admin'
    intentos=0; acceso=False

    Men_bienvenida= "BIENVENIDO A LIFESTORE \n\nPORFAVOR INGRESA TUS CREDENCIALES"
    print(Men_bienvenida)

    # Recibo constantemente sus intentos
    while not acceso:
        # Primero ingresa Credenciales
        usuario = input('Usuario: ')
        contras = input('Contrase;a: ')
        intentos += 1
        # Se valida con los detalles del usuario
        if usuario == username and contras == password:
            acceso = True
            print('Bienvenido',usuario, "\n")
            system("cls")
        else:
            print(f'Tienes {3 - intentos} intentos restantes')
            if usuario == username:
                print('Te equivocaste en la contrase;a')
            else:
                print(f'El usuario: "{usuario}" no esta registrado')
                
        if intentos == 3:
            print("Exediste la cantidad de intentos, Hasta Luego ")
            exit()


"""##--------------------------------Menu----------------------------------------------------##"""
def menu():
    login()
    while True:
        print('Que operacion desea hacer:')
        print('\t1. Realizar el punto 1 ("¿CUALES SON LOS PRODUCTOS CON MAYORES VENTAS Y MAYORES BUSQUEDAS?")\n')
        print('\t2. Realizar el punto 2 ("POR CATEGORIA, ¿CUALES SON LOS PRODUCTOS CON MENORESVENTAS Y BUSQUEDAS?)\n')
        print('\t3. Realizar el punto 3 (¿CUALES SON LOS PRODUCTOS CON MENORES Y MEJORES RESENAS?)\n')
        print('\t4. Realizar el punto 4 (¿CUALES SON LAS GANANCIAS TOTALES POR MES Y ANUAL?)\n')
        print('\t0. Salir')
        seleccion = input('> ')
        if seleccion == '1':
            punto1()
            os.system("pause")
            system("cls")

        elif seleccion == '2':
            punto2()
            os.system("pause")
            system("cls")

        elif seleccion == '3':
            products_por_resena()
            os.system("pause") 
            system("cls")

        elif seleccion == '4':
            ventas_totales_men()
            os.system("pause") 
            system("cls")         
                
        elif seleccion == '0':
            exit()
        else:
            print('Opcion invalida!')
            system("cls")
menu()







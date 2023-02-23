import os 

print('\r\n=================PRINCIPAL========================\r\n')
print('Lenguajes Formales y de Programación B+')
print('Kewin Maslovy Patzan Tzun')
print('202103206')
print('==================================================')
print('Presione cualquier tecla para continuar')
input()

lista_peliculas = []

class Pelicula:
    def __init__(self, nombre_pelicula, nombre_actor, ano_publicacion, genero_pelicula):
        self.nombre_pelicula = nombre_pelicula
        self.nombre_actor = nombre_actor
        self.ano_publicacion = ano_publicacion
        self.genero_pelicula = genero_pelicula

    def mostar_info(self):
        print('\nPelicula:', self.nombre_pelicula, '\nActores:', self.nombre_actor, '\nAño publicacion:', self.ano_publicacion, '\nGenero:', self.genero_pelicula)
    # Muestra las peliculas
    def mostrar_pelicula(self, contador):
        print(contador,'', self.nombre_pelicula)
    # Muestra los actores
    def mostrar_actores(self, contador):
        contador = 1
        for i in self.nombre_actor:
            print(contador, i.lstrip())
            contador += 1


    # Getters
    def get_nombre_pelicula(self):
        return self.nombre_pelicula
    
    def get_nombre_actor(self):
        return self.nombre_actor
    
    def get_ano_publicacion(self):
        return self.ano_publicacion
    
    def get_genero_pelicula(self):
        return self.genero_pelicula


def app():
    #Menu principal
    mostrar_menu()

    preguntar = True
    while preguntar:
        opcion = int(input('Eliga una opcion:\r\n'))
        if opcion == 1:
            print('-------------Cargar archivo--------------\n')
            leer_archivo(lista_peliculas)        
            for i in lista_peliculas:
                i.mostar_info()
            print('\n------Archivo cargado exitosamente------\n')
            preguntar = False
            app()
        elif opcion == 2:
            gestionar_peliculas()
            preguntar = False
        elif opcion == 3:
            filtrado_pelicula()
            preguntar = False
        elif opcion == 4:
            graphviz()
            preguntar = False
            app()
        elif opcion == 5:
            preguntar = False
            print('---------------------------------------------------')
            print('Finalizo la operacion, gracias por usar el programa.')
            break
        else:
            print('Opcion invalida')

def leer_archivo(lista):
    ruta = input('Introduzca la ruta del archivo que desea cargar: ')
    archivo = open(ruta, 'r') # lee la ruta del archivo insertado
    lineas = archivo.readlines()

    for i in lineas: # Guarda la informacion 
        contador = 1
        i = i.split(';')
        nombre_pelicula = None
        nombre_actor = None
        ano_publicacion = None
        genero_pelicula = None
        for j in i: # Separa la informacion por nombre, actor, año, genero
            if contador == 1:
                nombre_pelicula = j
            elif contador == 2:
                j = j.split(',')
                nombre_actor = j
            elif contador == 3:
                ano_publicacion = j
            elif contador == 4:
                genero_pelicula = j
            contador += 1

        pelicula = Pelicula(nombre_pelicula, nombre_actor, ano_publicacion, genero_pelicula) # Agrega la informacion guardada en una lista
        lista.append(pelicula)

    archivo.close()

def gestionar_peliculas():
    print('------Gestionar Peliculas------\r\n')
    menu_gestionar()
    preguntar = True

    while preguntar:
        opcion = int(input('Que opcion de gestion desea realizar?\r\n'))

        if opcion == 1:
            print('---------Peliculas------------\r\n')
            print('')
            contador = 1
            for i in lista_peliculas:
                i.mostrar_pelicula(contador)
                contador += 1
            print('')
            print('--------Gestion exitosa--------\r\n')
            menu_gestionar()
        elif opcion == 2:
            print('------Opciones de peliculas------\n')
            contador = 1
            for i in lista_peliculas:
                i.mostrar_pelicula(contador)
                contador += 1
            
            opcion = int(input('\r\nSelecciones la pelicula la cual desee ver los actores:\r\n'))

            print('------------Actores------------\r\n')
            print(lista_peliculas[opcion-1].mostrar_actores(contador))
            print('-------------------------------\r\n')            
            menu_gestionar()
        elif opcion == 3:
            app()
            break
        else:
            print('Opcion invalida')

def filtrado_pelicula():
    menu_filtrado()
    preguntar = True

    while preguntar:
        opcion = int(input('Que opcion de filtrado desea realizar\r\n'))

        if opcion == 1:
            print('-------------------------------\r\n') 
            opcion = input('Ingrese el nombre del actor:\r\n')
            
            print('------------Peliculas-----------\r\n')

            encontradas = False
            for i in lista_peliculas:
                for j in i.get_nombre_actor():
                    if opcion == j.strip():
                        print(i.get_nombre_pelicula())
                        encontradas = True
            if not encontradas:
                print('No se encontro ningun actor con ese nombre')

            menu_filtrado()
        elif opcion == 2:
            print('-------------------------------\r\n') 
            opcion = input('Ingrese el año de publicacion de la pelicula:\r\n')

            print('------------Peliculas-----------\r\n')
            
            encontradas = False
            for i in lista_peliculas:
                if opcion == i.get_ano_publicacion().lstrip():
                    print(i.get_nombre_pelicula())
                    encontradas = True
            if not encontradas:
                print('No se encontraron peliculas del año ingresado')
            print('-------------------------------\r\n') 

            menu_filtrado()    
        elif opcion == 3:
            print('-------------------------------\r\n') 

            opcion = input('Ingrese el género de la película:\r\n') 
            opcion_dos = opcion + '\n'

            print('-----------Peliculas----------\r\n')

            encontradas = False
            for i in lista_peliculas:
                 if i.get_genero_pelicula() == opcion_dos:
                    print(i.get_nombre_pelicula())
                    encontradas = True

            if not encontradas:
                print(f'No se encontraron películas del género {opcion}')
            
            print('-------------------------------\r\n') 

            menu_filtrado()
        elif opcion == 4:
            app()
            break
        else:
            print('Opcion invalida')

def graphviz():

    archivo = open('archivo.lfp', 'r')
    lineas = archivo.readlines()
    
    lista_peliculas = []
    for i in lineas:
        i = i.replace('\n','')
        i = i.split(';')
        
        x = {'Pelicula':i[0],'Actores':i[1],'Publicacion':i[2],'Genero':i[3]}
        lista_peliculas.append(x)

    archivo.close()

    archivoDOT = open('reporte_graphvis.dot', 'w')
    archivoDOT.write('digraph{ \n')
    archivoDOT.write('rankdir = TB; \n')
    archivoDOT.write('node[shape = record] \n')

    for i in lista_peliculas:
        archivoDOT.write(i['Pelicula'] + '[color = red, style = filled, label = "{' + i['Pelicula'] + '|' + i['Publicacion'] + '|' + i['Genero'] +'}"]\r\n')

    for i in lista_peliculas:
        for j in i['Actores'].split(','):
            archivoDOT.write(i['Pelicula'] + '->' + j.replace(' ', '') + '\n')

    archivoDOT.write('}\r\n')
    archivoDOT.close()
    os.system('dot.exe -Tpng reporte_graphvis.dot -o reporte.png')
    
def mostrar_menu():
    print('================MENU PRINCIPAL====================')
    print('')
    print('Seleccione una opcion:')
    print('1.Cargar archivos de entrada')
    print('2.Gestionar peliculas')
    print('3.Filtrado')
    print('4.Grafica')
    print('5.Salir')
    print('==================================================')

def menu_gestionar():
    print('------Opciones De Gestion------\r\n')
    print('1.Mostrar Peliculas')
    print('2.Mostrar Actores')
    print('3.Regresar al menu principal')
    print('-------------------------------')

def menu_filtrado():
    print('------Opciones De Filtado------\r\n')
    print('1.Filtrado por actor')
    print('2.Filtrado por año')
    print('3.Filtrado por genero')
    print('4.Regresar al menu principal')
    print('-------------------------------')

app()
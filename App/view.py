"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________
moviesfile = 'SmallMoviesDetailsCleaned.csv'
castingfile = 'MoviesCastingRaw-small.csv'
# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________
def printCompany(catalogo1, companyName):
    info = controller.getMoviesByCompany(catalogo1, companyName)
    if info:
        print('Compañia encontrada: ' + info['name'])
        print('Promedio: ' + str(info['vote_average']))
        print('Total de votos: ' + str(info['vote_count']))
        print('Total de peliculas: ' + str(lt.size(info['movies'])))
        iterator = it.newIterator(info['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print(movie['original_title'])
    else:
        print('No se encontro la compañia')

def printCountry(catalogo1, countryName):
    info = controller.getMoviesByCountry(catalogo1, countryName)
    if info:
        print('pais encontrado: ' + info['name'])
        print('Promedio: ' + str(info['vote_average']))
        print('Total de votos: ' + str(info['vote_count']))
        print('Total de peliculas: ' + str(lt.size(info['movies'])))
        iterator = it.newIterator(info['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print(movie['original_title'])
    else:
        print('No se encontro el pais')

def printGenre(catalogo1, genreName):
    info = controller.getMoviesByGenre(catalogo1, genreName)
    if info:
        print('genero encontrado encontrado: ' + info['name'])
        print('Promedio: ' + str(info['vote_average']))
        print('Total de votos: ' + str(info['vote_count']))
        print('Total de peliculas: ' + str(lt.size(info['movies'])))
        iterator = it.newIterator(info['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print(movie['original_title'])
    else:
        print('No se encontro el genero')

def printDirector(catalogo1, directorName):
    info = controller.getMoviesByDirector(catalogo1, directorName)
    if info:
        print('director encontrado: ' + info['name'])
        print('Promedio: ' + str(info['vote_average']))
        print('Total de votos: ' + str(info['vote_count']))
        print('Total de peliculas: ' + str(lt.size(info['movies'])))
        iterator = it.newIterator(info['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print(movie['original_title'])
    else:
        print('No se encontro el director')

def printActor(catalogo1, actorName):
    info = controller.getMoviesByActor(catalogo1, actorName)
    if info:
        print('actor encontrado: ' + info['name'])
        print('Promedio: ' + str(info['vote_average']))
        print('Total de votos: ' + str(info['vote_count']))
        print('Total de peliculas: ' + str(lt.size(info['movies'])))
        iterator = it.newIterator(info['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print(movie['original_title'])
        mayor=0
        quien=""
        for i in range (info['directors']['size']):
            element = lt.getElement(info['directors'], i)
            if int(element['veces'])> mayor:
                mayor=int(element['veces'])
                quien=element['name']
        print('director con mas colaboraciones: ' + quien)


    else:
        print('No se encontro el pais')

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Películas que pertenecen a una compañía de producción")
    print("4- Películas que se produjeron en un pais")
    print("5- Películas que se produjeron con un genero")
    print("6- Películas que se produjeron por un director")
    print("7- Películas que se produjeron por un actor")
    print("0- Salir")

# ___________________________________________________
#  Menu principal
# ___________________________________________________
def main():
    catalogo1=None
    
    while True:
        printMenu()
        
        inputs = input('Seleccione una opción para continuar\n')

        if int(inputs[0]) == 1:
            print("Inicializando Catálogo ....")
            catalogo1 = controller.initCatalog()      

        elif int(inputs[0]) == 2:
            print("Cargando información de los archivos ....")
            controller.loadData(catalogo1, moviesfile, castingfile)
            print('Peliculas cargadas: '+str(controller.moviesSize(catalogo1))+"  , y casting: " +str(controller.moviesSize(catalogo1)))
            
        elif int(inputs[0]) == 3:
            companyName = str(input('Escriba el nombre de la compañia de producción que desea consultar: '))
            printCompany(catalogo1, companyName)

        elif int(inputs[0]) == 4:
            countryName = str(input('Escriba el nombre del pais que desea consultar: '))
            printCountry(catalogo1, countryName)

        elif int(inputs[0]) == 5:
            genreName = str(input('Escriba el nombre del genero que desea consultar: '))
            printGenre(catalogo1, genreName)
                           
        elif int(inputs[0]) == 6:
            directorName = str(input('Escriba el nombre del director que desea consultar: '))
            printDirector(catalogo1, directorName)
                    
        elif int(inputs[0]) == 7:
            actorName = str(input('Escriba el nombre del actor que desea consultar: '))
            printActor(catalogo1, actorName)

        else:
            sys.exit(0)
    sys.exit(0)
main()
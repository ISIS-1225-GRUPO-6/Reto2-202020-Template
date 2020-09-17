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
import csv
from ADT import list as lt


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
def imprime_companias(compa_info):
    if compa_info:
        print('Compañia encontrada: ' + compa_info['name'])
        print('Promedio: ' + str(compa_info['vote_average']))
        print('Total de votos: ' + str(compa_info['vote_count']))
        print('Total de peliculas: ' + str(lt.size(compa_info['movies'])))
        iterator = it.newIterator(compa_info['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print(movie['original_title'])
    else:
        print('No se encontro la compañia')

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Películas que pertenecen a una compañía de producción")
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
            company_name = str(input('Escriba el nombre de la compañia de producción que desea consultar: '))
            compa_info = controller.getmoviesbycomp(catalogo1, company_name)
            imprime_companias(compa_info)

        elif int(inputs[0]) == 4:
            print()

        elif int(inputs[0]) == 5:
            print()
                        
        elif int(inputs[0]) == 6:
            print()
                    
        elif int(inputs[0]) == 7:
            print()
                
        elif int(inputs[0]) == 8:
            print()
        else:
            sys.exit(0)
    sys.exit(0)
main()

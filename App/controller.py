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

import config as cf
from App import model
import csv
from ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""
def loadCSVFile (file,cmpfunction):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    sep=";"
    lst = lt.newList("ARRAY_LIST",cmpfunction) #Usando implementacion arraylist
    #lst = lt.newList("SINGLE_LINKED",cmpfuntion) #Usando implementacion linkedlist   
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    
    return lst

def loadMovies():
    lst=loadCSVFile("Data/SmallMoviesDetailsCleaned.csv",comparaIds)
    print("Datos cargados, ",lst['size']," elementos cargados")
    return lst
def Aimprimir(lst):
    #print(lt.getElement(lst,1))
    listam=lt.newList('ARRAY_LIST',comparaIds)
    for i in range(lst['size']):
        elemento= lt.getElement(lst,i)
        titulo=(elemento['original_title'])
        fecha=(elemento['release_date'])
        prom=(elemento['vote_average'])
        votes=(elemento['vote_count'])
        lenguaje=(elemento['original_language'])
        agregar={'original_title': titulo,'release_date': fecha,'vote_average': prom,'vote_count': votes, 'original_language': lenguaje}
        lt.addLast(listam,agregar)
    elemento1=lt.getElement(listam,2)
    elemento2=lt.getElement(listam,1)
    print(elemento1['original_title']+", "+elemento1['release_date']+", "+elemento1['vote_average']+", "+elemento1['vote_count']+", "+elemento1['original_language'])
    print(elemento2['original_title']+", "+elemento2['release_date']+", "+elemento2['vote_average']+", "+elemento2['vote_count']+", "+elemento2['original_language']) 

def comparaIds (id, record):
    if int (id)== int (record['id']):
        return 0
    elif int (id) > int (record['id']):
        return 1
    return -1
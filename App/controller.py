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

from App.model import getMoviesByCountry, getMoviesByGenre
import config as cf
from App import model
import csv
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(catalog1, moviesfile, castingfile):
    """
    Carga los datos de los archivos en el modelo
    """
    loadmovies(catalog1, moviesfile)
    loadmoviesCasting(catalog1, castingfile)
    
def loadmoviesCasting(catalog,castingfile):
    castingfile = cf.data_dir + castingfile
    dialect = csv.excel()
    dialect.delimiter=";"
    input_file= csv.DictReader(open(castingfile, encoding='utf-8-sig'),dialect=dialect)
    for movie in input_file:
        model.addCasting(catalog,movie)
        if(movie['actor1_name']!="none"):
            model.addMovieByActor(catalog, movie['actor1_name'], movie)
        if(movie['actor2_name']!="none"):
            model.addMovieByActor(catalog, movie['actor2_name'], movie)
        if(movie['actor3_name']!="none"):
            model.addMovieByActor(catalog, movie['actor3_name'], movie)
        if(movie['actor4_name']!="none"):
            model.addMovieByActor(catalog, movie['actor4_name'], movie)
        if(movie['actor5_name']!="none"):
            model.addMovieByActor(catalog, movie['actor5_name'], movie)
        model.addMovieByDirector(catalog, movie['director_name'] , movie)

def loadmovies(catalog, moviesfile):
    #Carga cada una de las lineas del archivo de libros.
    #- Se agrega cada pelcula al catalogo de peliculas
    # - Por cada libro se encuentran sus autores y por cada
    #  autor, se crea una lista con sus libros

    moviesfile = cf.data_dir + moviesfile
    sep=";"  
    dialect = csv.excel()
    dialect.delimiter=sep
    
    with open(moviesfile, encoding="utf-8") as csvfile:
        input_file = csv.DictReader(csvfile, dialect=dialect)
        for movie in input_file:
            model.addmovie(catalog, movie)
            companias = movie['production_companies'].split(",") #info compañias
            genres = movie['genres'].split("|")
            countries = movie['production_countries'].split(",")
            for compania in companias:
                model.addMovieByCompany(catalog,compania,movie)
            for genre in genres:
                model.addMovieByGenre(catalog, genre.strip(), movie)
            for country in countries:
                model.addMovieByCountry(catalog, country.strip(), movie)

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def getMoviesByCompany (catalog, companyName):
    companyInfo = model.getMoviesByCompany(catalog, companyName)
    return companyInfo

def getMoviesByActor (catalog, actorName):
    actorInfo = model.getMoviesByActor(catalog, actorName)
    return actorInfo

def getMoviesByDirector (catalog, directorName):
    directorInfo = model.getMoviesByDirector(catalog, directorName)
    return directorInfo

def getMoviesByCountry (catalog, country):
    countryInfo = model.getMoviesByCountry(catalog, country)
    return countryInfo

def getMoviesByGenre (catalog, genre):
    genreInfo = model.getMoviesByGenre(catalog, genre)
    return genreInfo

def moviesSize(catalog):
    """Numero de libros leido
    """
    return model.moviesSize(catalog)


# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog

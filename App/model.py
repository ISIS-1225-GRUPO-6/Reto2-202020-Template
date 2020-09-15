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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'movies': None,
               'moviesIds': None,
               'actors': None,
                'directors': None,
               'moviesComp': None,
               'genres': None,
                'countries': None}
    lfactor=0.4
    tamaño=2011
    catalog['movies'] = lt.newList('SINGLE_LINKED', comparaIds)
    catalog['moviesIds'] = mp.newMap(tamaño,
                                   maptype='PROBING',
                                   loadfactor=lfactor,
                                   comparefunction=comparaMapMoviesIds)
    catalog['moviesComp'] = mp.newMap(tamaño,
                                   maptype='PROBING',
                                   loadfactor=lfactor,
                                   comparefunction=compareComp)
    catalog['directors'] = mp.newMap(tamaño,
                                   maptype='CHAINING',
                                   loadfactor=lfactor,
                                   comparefunction=compareDirectorsByName)
    catalog['actors'] = mp.newMap(tamaño,
                                  maptype='CHAINING',
                                  loadfactor=lfactor,
                                  comparefunction=compareActorsByName)
    catalog['genres'] = mp.newMap(tamaño,
                                 maptype='CHAINING',
                                 loadfactor=lfactor,
                                 comparefunction=compareGenres)
    catalog['countries'] = mp.newMap(tamaño,
                                 maptype='CHAINING',
                                 loadfactor=lfactor,
                                 comparefunction=compareCountry)
    return catalog
# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def addmovie(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['movies'], movie)
    #print(movie)
    mp.put(catalog['moviesIds'], movie['id'], movie)
    

def addComp(catalog, company_name, movie):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
    companias = catalog['moviesComp']
    existcomp = mp.contains(companias, company_name)
    if existcomp:
        entry = mp.get(companias, company_name)
        comp = me.getValue(entry)
    else:
        comp = newCompania(company_name)
        mp.put(companias, company_name, comp)
    lt.addLast(comp['movies'], movie)

    compaverage = comp['vote_average']
    movieaverage = movie['vote_average']
    if (compaverage == 0.0):
        comp['vote_average'] = float(movieaverage)
    else:
        comp['vote_average'] = (compaverage + float(movieaverage)) / 2


def newCompania(company_product):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'comp': "", "movies": None, "vote_average": 0}
    entry['comp'] = company_product
    entry['movies'] = lt.newList('SINGLE_LINKED', compareComp)
    return entry

def getmoviesbycomp(catalog, company_name):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    company_name = mp.get(catalog['moviesComp'], company_name)
    if company_name:
        return me.getValue(company_name)
    return None

def comparaIds (id, record):

    if int (id)== int (record['id']):
        return 0
    elif int (id) > int (record['id']):
        return 1
    return -1

def comparaMapMoviesIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareComp(Comp, entry):
    cpentry = me.getKey(entry)
    if (str(Comp) == str(cpentry)):
        return 0
    elif (str(Comp) > str(cpentry)):
        return 1
    else:
        return -1

def moviesSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['movies'])

def compareDirectorsByName(director, entry):
    directorentry = me.getKey(entry)
    if (director == directorentry):
        return 0
    elif (director > directorentry):
        return 1
    else:
        return -1
def compareActorsByName(name, entry):
    nameentry = me.getKey(entry)
    if (name == nameentry):
        return 0
    elif (name > nameentry):
        return 1
    else:
        return -1
def compareGenres(genre, entry):
    genreentry = me.getKey(entry)
    if (genre == genreentry):
        return 0
    elif (genre > genreentry):
        return 1
    else:
        return 0 

def compareCountry(country, entry):
    countryentry = me.getKey(entry)
    if (country == countryentry):
        return 0
    elif (country > countryentry):
        return 1
    else:
        return 0 
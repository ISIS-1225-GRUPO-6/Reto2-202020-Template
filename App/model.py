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
    "init"
    catalog = {'movies': None,
                'casting':None,
                'moviesIdsCasting':None,
               'moviesIds': None,
               'actors': None,
               'directors': None,
               'moviesComp': None,
               'genres': None,
               'countries': None}
    lfactor=0.4
    tamaño=2011
    catalog['movies'] = lt.newList('SINGLE_LINKED', comparaIds)
    catalog['casting'] = lt.newList('SINGLE_LINKED', comparaIds)
    catalog['moviesIdsCasting'] = mp.newMap(4011,
                                   maptype='PROBING',
                                   loadfactor=lfactor,
                                   comparefunction=comparaMapMoviesIds
                                   )
    catalog['moviesIds'] = mp.newMap(4011,
                                   maptype='PROBING',
                                   loadfactor=lfactor,
                                   comparefunction=comparaMapMoviesIds)
    catalog['moviesComp'] = mp.newMap(tamaño,
                                   maptype='CHAINING',
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
    lt.addLast(catalog['movies'], movie)
    mp.put(catalog['moviesIds'], movie['id'] , movie)
    
def addCasting(catalog, movie):
    lt.addLast(catalog['casting'], movie)
    mp.put(catalog['moviesIdsCasting'], movie['id'], movie)

def addMovieByCompany(catalog, companyName, movie):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
    companias = catalog['moviesComp']
    existcomp = mp.contains(companias, companyName)
    comp=None
    if existcomp:
        entry = mp.get(companias, companyName)
        comp = me.getValue(entry)
    else:
        comp = {'name':companyName, "movies": lt.newList('SINGLE_LINKED', compareComp),'votes':0.0 ,'vote_average': 0.0, 'vote_count': 0}
        mp.put(companias, companyName, comp)
    lt.addLast(comp['movies'], movie)
    comp['votes']+= float(movie['vote_average'])
    comp['vote_average']=comp['votes']/float(comp['movies']['size'])
    comp['vote_count']+=int(movie['vote_count'])

def addMovieByDirector(catalog,directorName,movie):
    directores = catalog['directors']
    existedirector = mp.contains(directores,directorName)
    director = None
    if existedirector:
        entry = mp.get(directores, directorName)
        director = me.getValue(entry)
    else:
        director = {'name': directorName, 'movies': lt.newList('ARRAY_LIST', compareDirectorsByName),'votes':0.0 ,'vote_average': 0.0, 'vote_count': 0}
        mp.put(directores, directorName, director)
    kv1=mp.get(catalog['moviesIds'],movie['id'])
    movie1= me.getValue(kv1)
    lt.addLast(director['movies'], movie1)
    movieavg = me.getValue(kv1)['vote_average']
    moviecount = me.getValue(kv1)['vote_count']
    director['votes']+=float(movieavg)
    director['vote_average']=director['votes']/float(director['movies']['size'])
    director['vote_count']+=int(moviecount)

def addMovieByCountry(catalog,countryName,movie):
    countries = catalog['countries']
    existcountry = mp.contains(countries,countryName)
    country=None
    if existcountry:
        entry = mp.get(countries, countryName)
        country = me.getValue(entry)
    else:
        country = {'name': countryName, 'movies': lt.newList('ARRAY_LIST', compareCountry),'votes':0.0 , 'vote_average': 0.0, 'vote_count': 0}
        mp.put(countries, countryName, country)
    lt.addLast(country['movies'], movie)
    country['votes']+=float(movie['vote_average'])
    country['vote_average']=country['votes']/float(country['movies']['size'])
    country['vote_count']+=int(movie['vote_count'])
    
def addMovieByGenre(catalog,genreName,movie):
    genres = catalog['genres']
    existgenre = mp.contains(genres,genreName)
    genre=None
    if existgenre:
        entry = mp.get(genres, genreName)
        genre = me.getValue(entry)
    else:
        genre = {'name': genreName, 'movies': lt.newList('ARRAY_LIST', compareGenres),'votes':0.0 , 'vote_average': 0.0, 'vote_count': 0}
        mp.put(genres, genreName, genre)
    lt.addLast(genre['movies'], movie)
    genre['votes']+=float(movie['vote_average'])
    genre['vote_average']=genre['votes']/float(genre['movies']['size'])
    genre['vote_count']+=int(movie['vote_count'])

def addMovieByActor(catalog,actorName,movie):
    actors = catalog['actors']
    existactor = mp.contains(actors,actorName)
    actor=None
    if existactor:
        entry = mp.get(actors, actorName)
        actor = me.getValue(entry)
    else:
        actor = {'name': actorName, 'movies': lt.newList('ARRAY_LIST', compareActorsByName), 'directors' :lt.newList('ARRAY_LIST', compareDirectorsByName), 'votes':0.0 , 'vote_average': 0.0, 'vote_count': 0}
        mp.put(actors, actorName, actor)
    kv1=mp.get(catalog['moviesIds'],movie['id'])
    movie1= me.getValue(kv1)
    lt.addLast(actor['movies'], movie1)
    movieavg = me.getValue(kv1)['vote_average']
    moviecount = me.getValue(kv1)['vote_count']
    actor['votes']+=float(movieavg)
    actor['vote_average']=actor['votes']/float(actor['movies']['size'])
    actor['vote_count']+=int(moviecount)
    director = actor['directors']
    namedic = movie['director_name']
    if director['size']==0 or director== None:
        lt.addFirst(director,{'name':namedic, 'veces':1})
    else:
        if existe(director,'name', namedic):
            for i in  range(director['size']):
                element = lt.getElement(director, i)
                if(element['name'] == namedic):
                    element['veces']+=1
                    break

        else:
            lt.addLast(director,{'name':namedic, 'veces':1})

# ___________________________________________________
#  Funciones para la comparacion y obtencion
#  de datos en los modelos
# ___________________________________________________   
def existe(lst, column, criteria ):
    for i in  range(lst['size']):
        element = lt.getElement(lst, i)
        if(element[column] == criteria):
            return True
            break
        else:
            return False

def getMoviesByCompany(catalog, companyName):
    companyName = mp.get(catalog['moviesComp'], companyName)
    if companyName:
        return me.getValue(companyName)
    return None

def getMoviesByDirector(catalog, directorName):
    directorName = mp.get(catalog['directors'], directorName)
    if directorName:
        return me.getValue(directorName)
    return None

def getMoviesByCountry(catalog, country):
    country = mp.get(catalog['countries'], country)
    if country:
        return me.getValue(country)
    return None

def getMoviesByGenre(catalog, genre):
    genre = mp.get(catalog['genres'], genre)
    if genre:
        return me.getValue(genre)
    return None

def getMoviesByActor(catalog, actorName):
    actorName = mp.get(catalog['actors'], actorName)
    if actorName:
        return me.getValue(actorName)
    return None

def comparaIds (id, record):

    if int (id)== int (record['id']):
        return 0
    elif int (id) > int (record['id']):
        return 1
    return -1

def comparaMapMoviesIds(id, entry):
    
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

def moviesSize(catalog):
    return lt.size(catalog['movies'])

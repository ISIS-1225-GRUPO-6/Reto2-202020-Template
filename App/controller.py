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
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(catalog, booksfile, tagsfile, booktagsfile):
    """
    Carga los datos de los archivos en el modelo
    """
    loadBooks(catalog, booksfile)
    loadTags(catalog, tagsfile)
    loadBooksTags(catalog, booktagsfile)


def loadBooks(catalog, booksfile):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada libro al catalogo de libros
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
    booksfile = cf.data_dir + booksfile
    input_file = csv.DictReader(open(booksfile))
    for book in input_file:
        model.addBook(catalog, book)
        authors = book['authors'].split(",")  # Se obtienen los autores
        for author in authors:
            model.addBookAuthor(catalog, author.strip(), book)


def loadTags(catalog, tagsfile):
    """
    Carga en el catalogo los tags a partir de la informacion
    del archivo de etiquetas
    """
    tagsfile = cf.data_dir + tagsfile
    input_file = csv.DictReader(open(tagsfile))
    for tag in input_file:
        model.addTag(catalog, tag)


def loadBooksTags(catalog, booktagsfile):
    """
    Carga la información que asocia tags con libros.
    Primero se localiza el tag y se le agrega la información leida.
    Adicionalmente se le agrega una referencia al libro procesado.
    """
    booktagsfile = cf.data_dir + booktagsfile
    input_file = csv.DictReader(open(booktagsfile))
    for tag in input_file:
        model.addBookTag(catalog, tag)


# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def booksSize(catalog):
    """Numero de libros leido
    """
    return model.booksSize(catalog)


def authorsSize(catalog):
    """Numero de autores leido
    """
    return model.authorsSize(catalog)


def tagsSize(catalog):
    """Numero de tags leido
    """
    return model.tagsSize(catalog)


def getBooksByAuthor(catalog, authorname):
    """
    Retorna los libros de un autor
    """
    authorinfo = model.getBooksByAuthor(catalog, authorname)
    return authorinfo


def getBooksByTag(catalog, tagname):
    """
    Retorna los libros que han sido marcados con
    una etiqueta
    """
    books = model.getBooksByTag(catalog, tagname)
    return books


def getBooksYear(catalog, year):
    """
    Retorna los libros que fueron publicados
    en un año
    """
    books = model.getBooksByYear(catalog, year)
    return books

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

def loadData(catalog,moviesfile):
    """
    Carga los datos de los archivos en el modelo
    """
    loadmovies(catalog, moviesfile)
    

def loadmovies(catalog, moviesfile):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada pelcula al catalogo de peliculas
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
    moviesfile = cf.data_dir + moviesfile
    sep=";"  
    dialect = csv.excel()
    dialect.delimiter=sep
    
    with open(moviesfile, encoding="utf-8") as csvfile:
        input_file = csv.DictReader(csvfile, dialect=dialect)
        for movie in input_file:
            model.addmovie(catalog, movie)
            compas = movie['production_companies'].split(",")  # Se obtienen los autores
            for compa in compas:
                model.addComp(catalog, compa.strip(), movie)

            

def getmoviesbycomp (catalog, company_name):
    compinfo = model.getmoviesbycomp(catalog, company_name)
    return compinfo

def moviesSize(catalog):
    """Numero de libros leido
    """
    return model.moviesSize(catalog)
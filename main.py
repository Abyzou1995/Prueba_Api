from typing import Union
from fastapi import FastAPI
import pandas as pd
import numpy as np
import json
import unicodedata

app = FastAPI()

Api1=pd.read_csv("API1.csv")
Api2=pd.read_csv("API2.csv")
Api3=pd.read_csv("API3.csv")
Api4=pd.read_csv("API4.csv")
Api5=pd.read_csv("API5.csv")
Api6=pd.read_csv("API6.csv")


@app.get("/")
def read_root():
    return {"Bienvenido al Proyecto Individual"}


@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes:str):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente'''
    if isinstance(mes, str):
        mes = mes.lower()
        mes = unicodedata.normalize('NFKD', mes).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        m = {
            'enero': 1,
            'febrero': 2,
            'marzo': 3,
            'abril': 4,
            'mayo': 5,
            'junio': 6,
            'julio': 7,
            'agosto': 8,
            'septiembre': 9,
            'octubre': 10,
            'noviembre': 11,
            'diciembre': 12
        }
        jum = Api1.cantidad[Api1["mes"] == m[mes]]
        jum = jum.tolist()
        respuesta = jum[0]
        return {'mes': mes, 'cantidad': respuesta}


@app.get('/peliculas_dia/{dia}')
def peliculas_dia(dia:str):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrebaron ese dia historicamente'''
    if isinstance(dia, str):
        dia = dia.lower()
        dia = unicodedata.normalize('NFKD', dia).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        d = {
            'lunes': 0,
            'martes': 1,
            'miercoles': 2,
            'jueves': 3,
            'viernes': 4,
            'sabado': 5,
            'domingo': 6
        }
        jum = Api2.cantidad[Api2["dia"] == d[dia]]
        jum = jum.tolist()
        respuesta = jum[0]

    return {'dia': dia, 'cantidad': respuesta}


@app.get('/franquicia/{franquiciax}')
def franquicia(franquiciax):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''


    if isinstance(franquiciax,str):
        franquiciax = franquiciax.lower()
        franquiciax = unicodedata.normalize('NFKD', franquiciax).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')

        ganancias = Api3["revenue"][Api3["belongs_to_collection"].str.contains(franquiciax)==True]
        respuesta1=ganancias.shape[0]
        respuesta2=ganancias.sum()
        respuesta3=ganancias.mean()

    return {'franquicia': franquiciax, 'cantidad': respuesta1, 'ganancia_total': respuesta2, 'ganancia_promedio': respuesta3}


@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais):
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''
    if isinstance(pais, str):
        pais = pais.lower()
        pais = unicodedata.normalize('NFKD', pais).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        ganancias = Api4["title"][Api4["production_countries"].str.contains(
            pais) == True]
        respuesta1 = ganancias.shape[0]

    return {'pais': pais, 'cantidad': respuesta1}


@app.get('/productoras/{productora}')
def productoras(productora:str):
    '''Ingresas la productora, retornando la ganancia toal y la cantidad de peliculas que produjeron'''
    if isinstance(productora, str):
        productora = productora.lower()
        productora = unicodedata.normalize('NFKD', productora).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        ganancias = Api5["revenue"][Api5["production_companies"].str.contains(
            productora) == True]
        respuesta2 = ganancias.shape[0]
        respuesta1=ganancias.sum()
    return {'productora': productora, 'ganancia_total': respuesta1, 'cantidad': respuesta2}


@app.get('/retorno/{pelicula}')
def retorno(pelicula:str):
    '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'''
    if isinstance(pelicula, str):
        pelicula = pelicula.lower()
        pelicula = unicodedata.normalize('NFKD', pelicula).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        ganancias = Api6[Api6["title"]==pelicula]
        respuesta1 = ganancias.budget.sum()
        respuesta2 = ganancias.revenue.sum()
        respuesta3 = ganancias["return"].sum()
        respuesta4 = ganancias["release_year"].astype(float)[0]

    return {'pelicula': pelicula, 'inversion': respuesta1, 'ganacia': respuesta2, 'retorno': respuesta3, 'anio': int(respuesta4)}

# ML


@app.get('/recomendacion/{titulo}')
def recomendacion(titulo: str):
    respuesta=titulo
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
    return {'lista recomendada': respuesta}

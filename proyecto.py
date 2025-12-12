"""
Práctica Unidades 1 y 2 — PROYECTOS II

Instrucciones generales:
- Este archivo se completará por etapas en distintas ramas de Git.
- NO cambies los nombres de las funciones ni sus parámetros.
- Puedes añadir funciones auxiliares si lo necesitas.
- Al finalizar, todas las funciones deben estar implementadas y probadas (puedes ejecutar tests propios).
"""

# === IMPORTS (añade otros si son necesarios) ===
import csv, json, os, random, math
from datetime import datetime
from typing import List, Dict, Optional
from warnings import catch_warnings

import numpy as np
import matplotlib.pyplot as plt
from pandas.core.arrays.categorical import contains
from scipy import optimize, integrate, interpolate
from setuptools.unicode_utils import try_encode
import pandas as pd


# 1) Básicos y cadenas
def sum_even(nums: List[int]) -> int:
    """Suma los enteros pares de la lista. Si no hay pares, devuelve 0."""
    suma = 0
    for n in nums:
        if n%2==0:
          suma = suma + n
    return suma

def normalize_str(s: str) -> str:
    """Devuelve s sin espacios al inicio/fin y en minúsculas."""
    return s.strip().lower()

def count_words(text: str) -> Dict[str,int]:
    """
    Devuelve un dict palabra->frecuencia.
    Reglas: separa por espacios; elimina . , ; : ! ? al final de cada token; ignora mayúsculas.
    """
    caracteres_no_validos = ['.',',',';',':','!','¡','¿','?']
    for caracter in caracteres_no_validos:
        text = text.replace(caracter, '')
    palabras = text.lower().split(' ')
    return {p:palabras.count(p) for p in palabras}

# 2) Ficheros y excepciones
def safe_divide(a: float, b: float) -> Optional[float]:
    """Devuelve a/b. Si b==0 o hay error, devuelve None."""
    try:
        return a/b
    except:
        return None

def read_csv_sum_revenue(path: str) -> float:
    """
    Lee un CSV con columnas units_sold y unit_price.
    Convierte a numérico; ignora NaN o negativos; suma units_sold*unit_price.
    """
    df_ventas = pd.read_csv(path)
    total = 0
    for i in range(0, len(df_ventas)):
        if pd.isna(df_ventas.loc[i,'units_sold'])  or pd.isna(df_ventas.loc[i,'unit_price']):
            pass
        else:
            try:
                df_ventas.loc[i,'units_sold'] = pd.to_numeric(str(df_ventas.loc[i,'units_sold']).replace(',','.'))
                df_ventas.loc[i,'unit_price'] = pd.to_numeric(str(df_ventas.loc[i,'unit_price']).replace(',','.'))
                if df_ventas.loc[i,'units_sold'] > 0 and df_ventas.loc[i,'unit_price'] > 0:
                    total = total + (df_ventas.loc[i,'units_sold'] * df_ventas.loc[i,'unit_price'])
            except:
                pass


    return total

def filter_customers_json(in_path: str, out_path: str) -> int:
    """
    JSON (lista de objetos con email y age).
    Escribe en out_path solo clientes con email que contenga '@' y age > 0.
    Devuelve el número de clientes escritos.
    :rtype: int
    """
    total_user = 0
    with open(in_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for user in data['users']:
        if '@' in user['email'] and user['age'] > 0:
            total_user = total_user + 1
            with open(out_path, "a", encoding="utf-8") as f:
                nombre = str.split(user['email'],'@')[0]
                f.write(nombre+'\n')
                f.close()
    f.close()
    return total_user

# 3) Comprensiones, random, datetime
def squares_of_odds(n: int) -> List[int]:
    """Lista de cuadrados de impares 1..n (ambos inclusive)."""
    return [num**2 for num in range(1, n + 1) if num % 2 != 0]

def random_color(seed: int) -> str:
    """Fija random.seed(seed) y retorna un color aleatorio de ['rojo','azul','verde']."""
    colores = ['rojo','azul','verde']
    random.seed(seed)
    return random.choice(colores)
    pass

def days_between(d1: str, d2: str) -> int:
    """Recibe fechas 'YYYY-MM-DD'. Devuelve abs(d2-d1) en días (entero)."""
    pass

# 4) NumPy
def numpy_vector_length(v: List[float]) -> float:
    """Norma Euclídea de v con NumPy."""
    pass

def numpy_minmax_scale(arr: List[float]) -> List[float]:
    """
    Normaliza a [0,1]. Si todos los valores son iguales, devuelve todos 0.0.
    """
    pass

# 5) SciPy
def scipy_root_cos_minus_x() -> float:
    """Raíz de f(x)=cos(x)-x con optimize.root, x0=0.5."""
    pass

def scipy_integral_sin() -> float:
    """Integral de sin(x) de 0 a pi con integrate.quad. Devuelve el área."""
    pass

def interp_linear(x: List[float], y: List[float], xq: float) -> float:
    """Interpolación lineal: devuelve f(xq) usando interpolate.interp1d."""
    pass

# 6) Visualización
def plot_line_time_series(xs: List[float], ys: List[float], out_path: str) -> bool:
    """
    Dibuja línea con título y etiquetas. Guarda en out_path y devuelve True si existe.
    """
    pass

def plot_bar(categories: List[str], values: List[float], out_path: str) -> bool:
    """Barras con etiquetas. Guarda y devuelve True si existe."""
    pass

def plot_scatter(x: List[float], y: List[float], out_path: str) -> bool:
    """Dispersión con grid y legend (usa label). Guarda y devuelve True si existe."""
    pass

# 7) POO
class Vector2D:
    """
    Implementa:
      - __init__(x, y)
      - __add__(other): suma vectorial, devuelve Vector2D
      - __eq__(other): igualdad por componentes
      - __repr__(): 'Vector2D(x=?, y=?)'
      - length(self) -> float: norma Euclídea
    """
    pass

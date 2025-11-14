"""
Módulo para resolver la Ecuación de Laplace usando el Método de Diferencias Finitas
con el algoritmo Gauss-Seidel.
"""

from .campo_estatico_mdf import LaplaceSolver2D

__version__ = "1.0.0"
__all__ = ['LaplaceSolver2D']
.. Campo Estático MDF documentation master file, created by
   sphinx-quickstart on Tue May 21 2024.

Bienvenido a la documentación de Campo Estático MDF
===================================================

Este proyecto implementa la solución numérica de la **Ecuación de Laplace** usando el **Método de Diferencias Finitas** (MDF) con el algoritmo **Gauss-Seidel**.

.. toctree::
   :maxdepth: 2
   :caption: Contenidos:

   campo_estatico_mdf

Ecuación de Laplace
-------------------

La **Ecuación de Laplace** en 2D se define como:

.. math::
   \nabla^2 V = \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} = 0

Método de Diferencias Finitas
-----------------------------

Usando el **Método de Diferencias Finitas**, la ecuación se discretiza como:

.. math::
   V_{i+1,j} + V_{i-1,j} + V_{i,j+1} + V_{i,j-1} - 4V_{i,j} = 0

Algoritmo Gauss-Seidel
----------------------

El método iterativo de **Gauss-Seidel** actualiza secuencialmente cada punto de la malla:

.. math::
   V_{i,j}^{(k+1)} = \frac{1}{4} \left( V_{i+1,j}^{(k)} + V_{i-1,j}^{(k+1)} + V_{i,j+1}^{(k)} + V_{i,j-1}^{(k+1)} \right)

Cálculo del Campo Eléctrico
---------------------------

El campo eléctrico se calcula como el gradiente negativo del potencial:

.. math::
   \vec{E} = -\nabla V = -\left( \frac{\partial V}{\partial x} \hat{i} + \frac{\partial V}{\partial y} \hat{j} \right)

Indices y Tablas
================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
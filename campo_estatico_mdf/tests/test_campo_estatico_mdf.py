import unittest
import numpy as np
import sys
import os

# Agregar el directorio padre al path para importar el módulo
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from campo_estatico_mdf import LaplaceSolver2D

class TestLaplaceSolver2D(unittest.TestCase):
    """Pruebas unitarias para la clase LaplaceSolver2D"""
    
    def test_caso_trivial(self):
        """
        Caso Trivial: Probar un caso donde la solución es obvia 
        (todas las fronteras a 0V, el resultado debe ser V=0 en toda la región interior).
        """
        solver = LaplaceSolver2D(N=10)
        solver.set_boundary_conditions(0.0, 0.0, 0.0, 0.0)
        
        iterations = solver.resolver(tolerance=1e-5, max_iter=1000)
        
        # Verificar que la solución es 0 en todos los puntos interiores
        np.testing.assert_array_almost_equal(solver.V, np.zeros((10, 10)), decimal=5)
        
        # Verificar que converge rápidamente
        self.assertLess(iterations, 1000)
    
    def test_convergencia(self):
        """
        Convergencia: Probar que el método converge para un conjunto simple 
        de condiciones de contorno (dos lados a 0V y dos lados a 10V) 
        dentro de un número razonable de iteraciones.
        """
        solver = LaplaceSolver2D(N=20)
        solver.set_boundary_conditions(left=0.0, right=10.0, top=0.0, bottom=0.0)
        
        iterations = solver.resolver(tolerance=1e-4, max_iter=5000)
        
        # Verificar que converge en un número razonable de iteraciones
        self.assertLess(iterations, 5000)
        
        # Verificar que se mantienen las condiciones de contorno
        self.assertEqual(solver.V[0, 0], 0.0)      # Esquina inferior izquierda
        self.assertEqual(solver.V[0, -1], 0.0)     # Esquina inferior derecha
        
        # Verificar que el borde derecho mantiene 10V (excluyendo esquinas)
        np.testing.assert_array_almost_equal(solver.V[1:-1, -1], 10.0, decimal=4)
        
        # Verificar que la solución no es trivial (no todos los puntos son cero)
        self.assertGreater(np.max(solver.V), 5.0)
    
    def test_calculo_campo_electrico(self):
        """
        Cálculo del Campo: Verificar que el cálculo del campo eléctrico es correcto 
        para un potencial conocido (si V es lineal, E debe ser constante).
        """
        solver = LaplaceSolver2D(N=10)
        
        # Crear un potencial lineal V = 2x + 3y
        x = np.linspace(0, 1, 10)
        y = np.linspace(0, 1, 10)
        X, Y = np.meshgrid(x, y)
        solver.V = 2 * X + 3 * Y  # V = 2x + 3y
        
        Ex, Ey = solver.calcular_campo_e()
        
        # Para V = 2x + 3y, E = -∇V = (-2, -3)
        # Verificar en puntos interiores (evitando bordes donde el gradiente es menos preciso)
        np.testing.assert_array_almost_equal(Ex[1:-1, 1:-1], -2.0, decimal=2)
        np.testing.assert_array_almost_equal(Ey[1:-1, 1:-1], -3.0, decimal=2)

if __name__ == '__main__':
    unittest.main()
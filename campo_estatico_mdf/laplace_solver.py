import numpy as np
from typing import Tuple

class LaplaceSolver2D:
    """
    Resuelve la ecuación de Laplace en 2D usando diferencias finitas
    """
    
    def __init__(self, n: int, boundary_conditions: dict):
        self.n = n
        self.V = np.zeros((n, n))
        self.boundary_conditions = boundary_conditions
        self._apply_boundary_conditions()
    
    def _apply_boundary_conditions(self):
        # Aplicar voltajes en los bordes
        if 'left' in self.boundary_conditions:
            self.V[:, 0] = self.boundary_conditions['left']
        if 'right' in self.boundary_conditions:
            self.V[:, -1] = self.boundary_conditions['right']
        if 'top' in self.boundary_conditions:
            self.V[0, :] = self.boundary_conditions['top']
        if 'bottom' in self.boundary_conditions:
            self.V[-1, :] = self.boundary_conditions['bottom']
    
    def solve_jacobi(self, tol: float = 1e-4, max_iter: int = 10000) -> int:
        """
        Resuelve usando método de Jacobi
        """
        V_old = self.V.copy()
        for iteration in range(max_iter):
            # Actualizar puntos interiores
            for i in range(1, self.n-1):
                for j in range(1, self.n-1):
                    self.V[i, j] = 0.25 * (V_old[i+1, j] + V_old[i-1, j] + 
                                          V_old[i, j+1] + V_old[i, j-1])
            
            # Verificar convergencia
            max_diff = np.max(np.abs(self.V - V_old))
            if max_diff < tol:
                return iteration + 1
            
            V_old = self.V.copy()
        
        return max_iter
    
    def calculate_electric_field(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calcula E = -grad V
        """
        Ey, Ex = np.gradient(self.V)
        return -Ex, -Ey
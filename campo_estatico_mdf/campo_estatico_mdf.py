import numpy as np
from typing import Tuple

class LaplaceSolver2D:
    """
    Resuelve la Ecuación de Laplace en 2D usando el Método de Diferencias Finitas
    con el método iterativo de Gauss-Seidel.
    
    Attributes:
        N (int): Tamaño de la malla (N x N)
        V (np.ndarray): Matriz del potencial eléctrico
        tolerance (float): Tolerancia para la convergencia
        max_iter (int): Número máximo de iteraciones
        h (float): Espaciado de la malla
    """
    
    def __init__(self, N: int = 50):
        """
        Inicializa el solver con una malla de N x N puntos.
        
        Args:
            N (int): Tamaño de la malla. Default es 50.
            
        Raises:
            ValueError: Si N es menor que 3
        """
        if N < 3:
            raise ValueError("El tamaño de la malla debe ser al menos 3x3")
        
        self.N = N
        self.V = np.zeros((N, N))
        self.tolerance = 1e-5
        self.max_iter = 10000
        self.h = 1.0 / (N - 1)  # Espaciado normalizado
    
    def set_boundary_conditions(self, left: float = 0.0, right: float = 0.0, 
                              top: float = 0.0, bottom: float = 0.0) -> None:
        """
        Establece las condiciones de contorno para los cuatro bordes.
        
        Args:
            left (float): Voltaje en el borde izquierdo. Default 0.0
            right (float): Voltaje en el borde derecho. Default 0.0
            top (float): Voltaje en el borde superior. Default 0.0
            bottom (float): Voltaje en el borde inferior. Default 0.0
        """
        # Borde izquierdo (x=0)
        self.V[:, 0] = left
        
        # Borde derecho (x=1)  
        self.V[:, -1] = right
        
        # Borde superior (y=1) - excluyendo esquinas
        if self.N > 2:
            self.V[-1, 1:-1] = top
        
        # Borde inferior (y=0) - excluyendo esquinas
        if self.N > 2:
            self.V[0, 1:-1] = bottom
        
        # Manejar esquinas explícitamente
        self.V[0, 0] = bottom    # Esquina inferior izquierda
        self.V[0, -1] = bottom   # Esquina inferior derecha
        self.V[-1, 0] = top      # Esquina superior izquierda
        self.V[-1, -1] = top     # Esquina superior derecha
    
    def resolver(self, tolerance: float = 1e-5, max_iter: int = 10000) -> int:
        """
        Resuelve la ecuación de Laplace usando el método iterativo de Gauss-Seidel.
        
        Args:
            tolerance (float): Tolerancia para la convergencia. Default 1e-5
            max_iter (int): Máximo número de iteraciones. Default 10000
            
        Returns:
            int: Número de iteraciones realizadas
            
        Raises:
            RuntimeError: Si no converge en el número máximo de iteraciones
        """
        self.tolerance = tolerance
        self.max_iter = max_iter
        
        for iter_count in range(self.max_iter):
            max_diff = 0.0
            
            # Actualizar puntos interiores usando el método de Gauss-Seidel
            for i in range(1, self.N-1):
                for j in range(1, self.N-1):
                    old_val = self.V[i, j]
                    new_val = 0.25 * (self.V[i+1, j] + self.V[i-1, j] + 
                                     self.V[i, j+1] + self.V[i, j-1])
                    self.V[i, j] = new_val
                    diff = abs(new_val - old_val)
                    max_diff = max(max_diff, diff)
            
            # Verificar convergencia
            if max_diff < self.tolerance:
                return iter_count + 1
        
        raise RuntimeError(f"No convergió después de {self.max_iter} iteraciones")
    
    def calcular_campo_e(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calcula el campo eléctrico E = -∇V usando diferencias centradas.
        
        Returns:
            Tuple[np.ndarray, np.ndarray]: Componentes Ex y Ey del campo eléctrico
        """
        # Calcular gradientes usando diferencias centradas
        Ey, Ex = np.gradient(self.V, self.h)
        
        # Campo eléctrico E = -∇V
        Ex = -Ex
        Ey = -Ey
        
        return Ex, Ey
    
    def get_potential(self) -> np.ndarray:
        """
        Retorna la matriz del potencial eléctrico.
        
        Returns:
            np.ndarray: Matriz N x N con los valores del potencial
        """
        return self.V.copy()
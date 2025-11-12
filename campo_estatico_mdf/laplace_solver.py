import numpy as np
from typing import Tuple, Dict

class LaplaceSolver2D:
    """
    Solves the 2D Laplace equation using the finite difference method.
    
    This class implements the Jacobi iterative method to solve the Laplace equation
    in a 2D square region with fixed boundary conditions.
    
    Parameters
    ----------
    n : int
        Grid size (n x n points). Must be greater than 2.
    boundary_conditions : dict
        Dictionary with boundary conditions. Keys can be:
        'left', 'right', 'top', 'bottom' and values are the applied voltages.
    
    Raises
    ------
    ValueError
        If n is less than or equal to 2, or if no boundary conditions are provided.
    
    Examples
    --------
    >>> solver = LaplaceSolver2D(50, {'left': 0, 'right': 10, 'top': 5, 'bottom': 5})
    >>> iterations = solver.solve_jacobi(tol=1e-5)
    >>> Ex, Ey = solver.calculate_electric_field()
    """
    
    def __init__(self, n: int, boundary_conditions: Dict[str, float]):
        """
        Initializes the solver with grid size and boundary conditions.
        
        Parameters
        ----------
        n : int
            Grid size (n x n points)
        boundary_conditions : dict
            Boundary conditions for the edges
            
        Raises
        ------
        ValueError
            If n <= 2 or if no boundary conditions are provided
        """
        if n <= 2:
            raise ValueError("Grid size n must be greater than 2")
        if not boundary_conditions:
            raise ValueError("Boundary conditions must be provided")
        
        self.n = n
        self.V = np.zeros((n, n))
        self.boundary_conditions = boundary_conditions
        self._apply_boundary_conditions()
    
    def _apply_boundary_conditions(self):
        """
        Applies boundary conditions to the grid edges.
        
        Boundary conditions are applied to the four edges according to the
        boundary_conditions dictionary provided in the constructor.
        
        Notes
        -----
        Edges are identified as:
        - 'left': first column (index 0)
        - 'right': last column (index -1)
        - 'top': first row (index 0)
        - 'bottom': last row (index -1)
        """
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
        Solves the Laplace equation using the Jacobi iterative method.
        
        Parameters
        ----------
        tol : float, optional
            Tolerance for convergence (maximum difference between iterations).
            Default is 1e-4.
        max_iter : int, optional
            Maximum number of iterations allowed. Default is 10000.
        
        Returns
        -------
        int
            Number of iterations performed until convergence.
            If it doesn't converge, returns max_iter.
        
        Raises
        ------
        ValueError
            If tol <= 0 or max_iter <= 0.
        
        Notes
        -----
        The Jacobi method updates all grid points simultaneously using values
        from the previous iteration.
        """
        if tol <= 0:
            raise ValueError("Tolerance must be greater than 0")
        if max_iter <= 0:
            raise ValueError("Maximum number of iterations must be greater than 0")
        
        V_old = self.V.copy()
        for iteration in range(max_iter):
            # Update interior points
            for i in range(1, self.n-1):
                for j in range(1, self.n-1):
                    self.V[i, j] = 0.25 * (V_old[i+1, j] + V_old[i-1, j] + 
                                          V_old[i, j+1] + V_old[i, j-1])
            
            # Check convergence
            max_diff = np.max(np.abs(self.V - V_old))
            if max_diff < tol:
                return iteration + 1
            
            V_old = self.V.copy()
        
        return max_iter
    
    def calculate_electric_field(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calculates the electric field as E = -grad V.
        
        Returns
        -------
        Tuple[np.ndarray, np.ndarray]
            Tuple with electric field components (Ex, Ey).
            Ex is the x-direction component, Ey is the y-direction component.
        
        Notes
        -----
        Uses numpy.gradient to calculate the numerical gradient.
        The electric field is the negative gradient of the potential.
        """
        Ey, Ex = np.gradient(self.V)
        return -Ex, -Ey
    
    def get_potential(self) -> np.ndarray:
        """
        Returns the calculated potential matrix.
        
        Returns
        -------
        np.ndarray
            2D matrix with electric potential values V(x, y).
        """
        return self.V.copy()

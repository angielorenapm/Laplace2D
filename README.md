Laplace2D – Electrostatic Field Simulation Using the Finite Difference Method ⚡🔢

Laplace2D is a Python package for solving the two-dimensional Laplace equation using the Finite Difference Method (FDM) and the Gauss–Seidel iterative algorithm.
It provides a numerical solver, an interactive Streamlit interface, scientific visualizations, automated testing tools, and Sphinx-based documentation.
The project is suitable for education, research, and computational physics applications.

📦 PyPI: https://pypi.org/project/campo-estatico-laplace2D-G/0.1.0/

💻 GitHub: https://github.com/angielorenapm/Laplace2D

1. Project Structure 🗂️
campo_estatico/
│
├── campo_estatico_mdf/
│   ├── __init__.py
│   ├── campo_estatico_mdf.py        # Numerical solver
│   └── tests/
│       ├── __init__.py
│       └── test_campo_estatico_mdf.py
│
├── streamlit_app/
│   └── app.py                        # Streamlit GUI
│
├── docs/                             # Sphinx documentation
│   ├── conf.py
│   ├── index.rst
│   └── modules.rst
│
├── requirements.txt
├── setup.py
├── pyproject.toml
└── README.md

2. Overview 📘

This package offers a complete computational environment for exploring Laplace’s equation in 2D:

Solver using central finite differences and Gauss–Seidel iterations

Configurable Dirichlet boundary conditions on all edges

Calculation of the electric potential over a square domain

Computation of the electric field from the potential

Visualizations of:

Potential field (heatmaps)

Electric field (quiver plots)

Interactive Streamlit application

Automated tests using pytest

Documentation generated with Sphinx

The project is ideal for learning numerical methods, understanding electrostatics, and building reproducible simulations.

3. Installation 🔧
Install from PyPI
pip install campo-estatico-laplace2D-G

Install from source
git clone https://github.com/angielorenapm/Laplace2D.git
cd Laplace2D
pip install .

Developer installation
pip install -e .[dev]

4. Running the Streamlit Application 🖥️

The interactive interface allows users to:

Configure the grid size

Adjust tolerance and maximum iterations

Set boundary voltages

Visualize the potential distribution

Explore the electric field

Inspect numerical metrics

To launch the app:

streamlit run streamlit_app/app.py

5. Usage Example (Python API) 🧪
from campo_estatico_mdf import LaplaceSolver2D

# Create solver
solver = LaplaceSolver2D(N=60)

# Boundary conditions
solver.set_boundary_conditions(
    left=0.0, right=10.0,
    top=0.0, bottom=0.0
)

# Solve the equation
iterations = solver.resolver(tolerance=1e-5, max_iter=10000)

# Retrieve results
V = solver.get_potential()
Ex, Ey = solver.calcular_campo_e()

6. Mathematical Background 📐🧠

This section summarizes the physics and numerical foundations behind the solver, using notation that is compatible with Markdown and PyPI.

6.1. Laplace’s Equation in Electrostatics ⚡

In a region free of electric charge, the electric potential V(x,y) satisfies Laplace’s equation:

nabla^2 V = 0


This comes from:

Gauss’s law: div(E) = rho / epsilon_0

Electric field definition: E = -grad(V)

If the charge density rho = 0, then:

div(E) = div(-grad(V)) = -nabla^2 V = 0


Solving Laplace’s equation gives:

The electric potential V(x,y)

The electric field E = -grad(V)

for a given set of boundary conditions.

This equation models many physical systems, including:

Capacitors

Electrodes and conductors

Electrostatic shielding

Steady-state heat conduction (mathematically analogous)

6.2. Finite Difference Discretization 🔢

The continuous square domain is discretized into an N x N grid.
Let the grid spacing be:

h = 1 / (N - 1)


The Laplacian operator in 2D is:

nabla^2 V = d^2 V / dx^2 + d^2 V / dy^2


Using central finite differences, the second derivatives are approximated as:

d^2 V / dx^2 ≈ (V(i+1,j) - 2*V(i,j) + V(i-1,j)) / h^2
d^2 V / dy^2 ≈ (V(i,j+1) - 2*V(i,j) + V(i,j-1)) / h^2


Substituting into Laplace’s equation and rearranging yields the discrete update:

V(i,j) = 0.25 * ( V(i+1,j) + V(i-1,j) + V(i,j+1) + V(i,j-1) )


This means:

👉 At equilibrium, the potential at each interior point is the average of its four nearest neighbors.

6.3. Boundary Conditions (Dirichlet) 🧱

The solution inside the domain is determined by the potential on the boundaries (Dirichlet conditions). For a square domain:

Left boundary: V(0, y) = V_left

Right boundary: V(1, y) = V_right

Bottom boundary: V(x, 0) = V_bottom

Top boundary: V(x, 1) = V_top

These boundary values represent physical constraints such as:

Conducting plates held at fixed potentials

Electrodes in contact with a conductor

Imposed voltages in a device or numerical experiment

6.4. Gauss–Seidel Iterative Method 🔁

To solve the discrete Laplace equation on the grid, the package uses the Gauss–Seidel iterative method.

At each iteration, for every interior point (i,j):

V_new(i,j) =
    0.25 * (
        V_old(i+1,j) +
        V_new(i-1,j) +
        V_old(i,j+1) +
        V_new(i,j-1)
    )


The algorithm:

Starts from an initial guess (typically zeros in the interior).

Sweeps over all interior points updating them using the equation above.

Tracks the maximum absolute difference between old and new values:

diff = |V_new(i,j) - V_old(i,j)|


Stops when the maximum difference is below a user-defined tolerance tolerance,
or when a maximum number of iterations max_iter is reached.

Reasons for using Gauss–Seidel:

Faster convergence than Jacobi for many elliptic PDE problems

Simple implementation

Low memory requirements

Well-suited for Laplace-type equations

6.5. Electric Field Computation 🧲

After computing the potential matrix V, the electric field E is calculated as:

E = -grad(V)


In discrete form, using central differences:

Ex ≈ - ( V(i+1,j) - V(i-1,j) ) / (2*h)
Ey ≈ - ( V(i,j+1) - V(i,j-1) ) / (2*h)


These components:

Indicate the direction and magnitude of the electric field

Are used to construct quiver plots showing field lines

Help connect potential landscapes with physical electric forces

6.6. Physical Interpretation 🧭

The numerical solution from Laplace2D represents a steady-state electrostatic configuration:

No free charges inside the domain

All variation in the potential is imposed by the boundaries

Potential surfaces are smooth and harmonic

Electric field lines always go from regions of higher potential to lower potential

Equipotential curves are always perpendicular to electric field lines

This connects the numerical method directly with the physical intuition taught in electromagnetism courses.

6.7. Applications 🎓

Typical applications of this solver include:

Modeling parallel-plate capacitors and other geometries

Studying electric shielding and field shaping

Numerical experiments in electrostatics

Educational labs for numerical methods and PDEs

Heat conduction and diffusion analogies (same mathematical structure)

7. Features 🧩

2D Laplace solver using finite differences and Gauss–Seidel

Configurable Dirichlet boundary conditions

Adjustable mesh size, tolerance, and maximum iterations

Electric field computation from the potential

Potential heatmaps and electric field vector plots

Interactive Streamlit graphical interface

Pytest-based test suite

Sphinx-based documentation

Clean, modular, object-oriented codebase

8. Documentation 📚

To build the documentation locally:

cd docs
make html


The generated HTML files will be located in:

docs/_build/html/

9. Running Tests 🧪

To run all tests:

pytest


To run with coverage:

pytest --cov=campo_estatico_mdf --cov-report=html

10. API Reference 📘
Class: LaplaceSolver2D

Constructor

LaplaceSolver2D(N: int = 50)


Creates an N x N computational grid and initializes the potential matrix.

Methods

set_boundary_conditions(left, right, top, bottom)
Sets constant Dirichlet boundary conditions on the four borders of the square domain.

resolver(tolerance=1e-5, max_iter=10000)
Runs the Gauss–Seidel iteration until convergence or until max_iter is reached.
Returns the number of iterations performed.

get_potential()
Returns a copy of the potential matrix V.

calcular_campo_e()
Computes and returns the electric field components (Ex, Ey) using finite differences.

11. Contributing 🤝

Contributions, improvements, and extensions are welcome.
If you plan to contribute:

Fork the repository.

Create a new branch for your feature or fix.

Add or update tests when appropriate.

Submit a pull request with a clear description of the changes.

12. Authors 👥

Juan Pablo Patiño – Numerical methods and implementation
Email: jppatinob@udistrital.edu.co

Angie Lorena Pineda Morales – Physics validation and development
Email: alpinedam@udistrital.edu.co

13. License 📄

This project is licensed under the MIT License.
You are free to use, modify, and distribute the software in accordance with the license terms.

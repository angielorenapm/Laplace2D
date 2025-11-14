# Laplace2D – Electrostatic Field Simulation Using the Finite Difference Method ⚡🔢

**Laplace2D** is a Python package for solving the two-dimensional Laplace equation using the **Finite Difference Method (FDM)** and the **Gauss–Seidel iterative algorithm**.  
It includes a numerical solver, a Streamlit GUI, scientific visualizations, a test suite, and Sphinx documentation.  
The project is intended for **education**, **research**, and **computational physics** applications.

📦 **PyPI:** https://pypi.org/project/campo-estatico-laplace2D-G/  
💻 **GitHub Repository:** https://github.com/angielorenapm/Laplace2D

---

## 1. Project Structure 🗂️

```text
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
```

---

## 2. Overview 📘

Laplace2D provides a complete environment for exploring the Laplace equation in 2D:

- Finite Difference + Gauss–Seidel solver  
- Configurable Dirichlet boundary conditions  
- Electric field computation  
- Potential heatmaps and quiver plots  
- Interactive Streamlit app  
- Automated tests using pytest  
- Sphinx documentation  

This package is ideal for numerical methods courses, electrostatics studies, and scientific computing projects.

---

## 3. Installation 🔧

### Install from PyPI

```bash
pip install campo-estatico-laplace2D-G
```

### Install from source

```bash
git clone https://github.com/angielorenapm/Laplace2D.git
cd Laplace2D
pip install .
```

### Developer mode

```bash
pip install -e .[dev]
```

---

## 4. Running the Streamlit Application 🖥️

The interactive GUI allows you to:

- Set the grid size  
- Adjust convergence tolerance  
- Define boundary voltages  
- Visualize potential and electric field  

Run:

```bash
streamlit run streamlit_app/app.py
```

---

## 5. Python Usage Example 🧪

```python
from campo_estatico_mdf import LaplaceSolver2D

solver = LaplaceSolver2D(N=60)

solver.set_boundary_conditions(
    left=0.0, right=10.0,
    top=0.0, bottom=0.0
)

iterations = solver.resolver(tolerance=1e-5, max_iter=10000)

V = solver.get_potential()
Ex, Ey = solver.calcular_campo_e()
```

---

# 6. Mathematical Background 📐🧠

The solver is based on core concepts from electrostatics and numerical methods.  
GitHub supports Markdown rendering, but not full LaTeX in all contexts, so equations are written in plain text.

---

## 6.1. Laplace’s Equation in Electrostatics ⚡

In a charge-free region, the electric potential satisfies:

```text
nabla^2 V = 0
```

With the electric field defined as:

```text
E = - grad(V)
```

This equation describes physical systems such as:

- Capacitors  
- Electrodes  
- Conducting boundaries  
- Electrostatic shielding  
- Steady-state heat conduction (mathematically equivalent)

---

## 6.2. Finite Difference Discretization 🔢

The 2D domain is discretized into an `N x N` grid.  
Grid spacing:

```text
h = 1 / (N - 1)
```

Finite difference approximations:

```text
d2V/dx2 ≈ (V(i+1,j) - 2*V(i,j) + V(i-1,j)) / h^2
d2V/dy2 ≈ (V(i,j+1) - 2*V(i,j) + V(i,j-1)) / h^2
```

Discrete Laplace equation:

```text
V(i,j) = 0.25 * ( V(i+1,j) + V(i-1,j) + V(i,j+1) + V(i,j-1) )
```

Meaning:

👉 **Each interior point equals the average of its four neighbors**.

---

## 6.3. Dirichlet Boundary Conditions 🧱

Boundary voltages define the problem:

```text
Left   : V(0,y) = V_left
Right  : V(1,y) = V_right
Top    : V(x,1) = V_top
Bottom : V(x,0) = V_bottom
```

---

## 6.4. Gauss–Seidel Iterative Method 🔁

Iterative update rule:

```text
V_new(i,j) = 0.25 * (
    V_old(i+1,j) +
    V_new(i-1,j) +
    V_old(i,j+1) +
    V_new(i,j-1)
)
```

Convergence criterion:

```text
|V_new - V_old| < tolerance
```

Advantages:

- Faster than Jacobi  
- Efficient for elliptic PDEs like Laplace  
- Simple to implement  
- Low memory usage  

---

## 6.5. Electric Field Computation 🧲

Electric field is obtained from:

```text
E = - grad(V)
```

Using central differences:

```text
Ex ≈ - (V(i+1,j) - V(i-1,j)) / (2*h)
Ey ≈ - (V(i,j+1) - V(i,j-1)) / (2*h)
```

---

## 6.6. Physical Interpretation 🧭

The computed solution represents a **steady-state electrostatic equilibrium**:

- No charges inside the domain  
- All variation comes from boundary conditions  
- Potential surfaces are smooth and harmonic  
- Electric field lines go from high to low potential  
- Equipotential lines intersect field lines orthogonally  

---

## 6.7. Applications 🎓

- Capacitor modelling  
- Electrostatic shielding  
- Electric field design  
- Numerical PDE education  
- Heat conduction simulations  
- Computational physics laboratories  

---

## 7. Features 🧩

- Finite Difference + Gauss–Seidel solver  
- Electric field computation  
- Streamlit GUI  
- Heatmap and vector field visualizations  
- Pytest suite  
- Sphinx documentation  
- Clean, modular, object-oriented design  

---

## 8. Running Tests 🧪

```bash
pytest
```

With coverage:

```bash
python -m unittest campo_estatico_mdf.tests.test_campo_estatico_mdf -v
```
Alternatively
```bash
python -m pytest campo_estatico_mdf/tests/test_campo_estatico_mdf.py -v
```

---

## 10. API Reference 📘

### Class: `LaplaceSolver2D`

Constructor:

```text
LaplaceSolver2D(N=50)
```

Methods:

```text
set_boundary_conditions(left, right, top, bottom)
resolver(tolerance, max_iter)
get_potential()
calcular_campo_e()
```

---

## 11. Contributing 🤝

Contributions are welcome.  
Please:

1. Fork the repository  
2. Create a feature branch  
3. Add tests  
4. Submit a pull request  

---

## 12. Authors 👥

- **Juan Pablo Patiño** – Numerical implementation  
- **Angie Lorena Pineda Morales** – Physics validation and development  

---

## 13. License 📄

Released under the **MIT License**.

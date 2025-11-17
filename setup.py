# setup.py
from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8") if (HERE / "README.md").exists() else ""

setup(
    name="campo_estatico_mdf",
    use_scm_version=True,  # usa setuptools_scm (coincide con pyproject.toml)
    setup_requires=["setuptools_scm"],
    description="A Python package for solving 2D Laplace equation using finite difference method",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Juan Pablo Patiño & Angie Lorena Pineda Morales",
    author_email="jppatinob@udistrital.edu.co, alpinedam@udistrital.edu.co",
    url="https://github.com/angielorenapm/Laplace2D",
    packages=find_packages(where="."),
    include_package_data=True,
    package_data={"campo_estatico_mdf": ["py.typed"]},
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "matplotlib>=3.5.0",
        "streamlit>=1.22.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "black>=22.0",
            "flake8>=4.0",
        ]
    },
    entry_points={
        "console_scripts": [
            # Coincide con project.scripts en pyproject.toml
            "campo-estatico-app = streamlit_app.app:main",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    keywords=[
        "laplace-equation",
        "finite-differences",
        "electrostatics",
        "numerical-methods",
        "scientific-computing",
    ],
    python_requires=">=3.8",
    license="MIT",
    project_urls={
        "Homepage": "https://github.com/angielorenapm/Laplace2D",
        "Documentation": "https://angielorenapm.github.io/Laplace2D",
        "Repository": "https://github.com/angielorenapm/Laplace2D",
        "Issue Tracker": "https://github.com/angielorenapm/Laplace2D/issues",
    },
    zip_safe=False,
)

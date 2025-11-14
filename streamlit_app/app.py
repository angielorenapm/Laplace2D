import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Agregar el directorio del módulo al path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from campo_estatico_mdf import LaplaceSolver2D

def main():
    st.set_page_config(page_title="Simulador de Campo Electroestático", layout="wide")
    
    st.title("⚡ Simulador de Campo Electroestático 2D")
    st.markdown("""
    Esta aplicación resuelve la **Ecuación de Laplace** usando el **Método de Diferencias Finitas**
    con el algoritmo **Gauss-Seidel** para calcular la distribución del potencial eléctrico 
    en una región cuadrada.
    """)
    
    # Sidebar para inputs
    st.sidebar.header("Parámetros de Simulación")
    
    # Inputs del usuario
    N = st.sidebar.slider("Tamaño de la malla (N x N)", min_value=10, max_value=100, value=50)
    tolerance = st.sidebar.number_input("Tolerancia de convergencia", min_value=1e-8, max_value=1e-2, value=1e-5, format="%.0e")
    max_iter = st.sidebar.number_input("Máximo de iteraciones", min_value=100, max_value=50000, value=10000)
    
    st.sidebar.header("Condiciones de Contorno")
    left_V = st.sidebar.number_input("Voltaje borde izquierdo (V)", value=0.0)
    right_V = st.sidebar.number_input("Voltaje borde derecho (V)", value=10.0)
    top_V = st.sidebar.number_input("Voltaje borde superior (V)", value=0.0)
    bottom_V = st.sidebar.number_input("Voltaje borde inferior (V)", value=0.0)
    
    # Botón para ejecutar simulación
    if st.sidebar.button("Ejecutar Simulación"):
        try:
            with st.spinner("Calculando solución..."):
                # Crear solver y configurar condiciones
                solver = LaplaceSolver2D(N=N)
                solver.set_boundary_conditions(
                    left=left_V, 
                    right=right_V, 
                    top=top_V, 
                    bottom=bottom_V
                )
                
                # Ejecutar método Gauss-Seidel
                iterations = solver.resolver(tolerance=tolerance, max_iter=max_iter)
                
                # Calcular campo eléctrico
                Ex, Ey = solver.calcular_campo_e()
                V = solver.get_potential()
                
                # Mostrar resultados
                st.success(f"Simulación completada en {iterations} iteraciones")
                
                # Crear visualizaciones
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Distribución del Potencial Eléctrico")
                    fig1, ax1 = plt.subplots(figsize=(8, 6))
                    im = ax1.imshow(V, cmap='viridis', origin='lower', 
                                   extent=[0, 1, 0, 1])
                    ax1.set_xlabel('X')
                    ax1.set_ylabel('Y')
                    ax1.set_title('Potencial Eléctrico V(x,y)')
                    plt.colorbar(im, ax=ax1, label='Voltaje (V)')
                    st.pyplot(fig1)
                
                with col2:
                    st.subheader("Campo Eléctrico")
                    fig2, ax2 = plt.subplots(figsize=(8, 6))
                    
                    # Reducir densidad de vectores para mejor visualización
                    step = max(1, N // 20)
                    x = np.linspace(0, 1, N)
                    y = np.linspace(0, 1, N)
                    X, Y = np.meshgrid(x, y)
                    
                    # Calcular magnitud del campo para colorear vectores
                    E_magnitude = np.sqrt(Ex**2 + Ey**2)
                    
                    quiver = ax2.quiver(X[::step, ::step], Y[::step, ::step], 
                                      Ex[::step, ::step], Ey[::step, ::step],
                                      E_magnitude[::step, ::step], 
                                      cmap='hot', scale=20 if np.max(E_magnitude) > 0 else 1)
                    
                    ax2.set_xlabel('X')
                    ax2.set_ylabel('Y')
                    ax2.set_title('Campo Eléctrico E(x,y)')
                    plt.colorbar(quiver, ax=ax2, label='|E|')
                    st.pyplot(fig2)
                
                # Información adicional
                st.subheader("Métricas de la Simulación")
                col3, col4, col5 = st.columns(3)
                
                with col3:
                    st.metric("Iteraciones", iterations)
                
                with col4:
                    V_range = f"{np.min(V):.3f} V - {np.max(V):.3f} V"
                    st.metric("Rango de Potencial", V_range)
                
                with col5:
                    max_E = f"{np.max(E_magnitude):.3f}"
                    st.metric("Máxima |E|", max_E)
                    
        except RuntimeError as e:
            st.error(f"Error en la simulación: {e}")
        except Exception as e:
            st.error(f"Error inesperado: {e}")
    
    else:
        # Mostrar instrucciones antes de ejecutar
        st.info("👈 Configura los parámetros en la barra lateral y haz clic en 'Ejecutar Simulación'")

if __name__ == "__main__":
    main()
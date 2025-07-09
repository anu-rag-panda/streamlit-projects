import streamlit as st
import numpy as np
import plotly.graph_objects as go
import sympy as sp
from io import BytesIO


#page setup
st.set_page_config(
    page_title="Graph Plotter",
    layout="centered"
)
st.title("📊 2D / 3D Graph Plotter")

#----user input----
st.markdown("Enter a mathematical function using 'x' for 2D or 'x' and 'y' for 3D.")
func_input = st.text_input("🔢 Enter Function:", value="sin(x)")
plot_type = st.radio("📐 Plot Type:", ["2D", "3D"])

#custom axis range
st.markdown("Set custom axis range (optional):")
x_min = st.number_input("X min", value=-5.0)
x_max = st.number_input("X max", value=5.0)

if plot_type == "3D":
    y_min = st.number_input("Y min", value=-5.0)
    y_max = st.number_input("Y max", value=5.0)
else:
    y_min = None
    y_max = None

#derivative or integral option
if plot_type == "2D":
    st.subheader("Derivative or Integral")
    show_derivative = st.checkbox("Show Derivative")
    show_integral = st.checkbox("Show Indefinite Integral")
else:
    show_derivative = False
    show_integral = False
    
#function parsing
x, y = sp.symbols('x y')
try:
    func_expr = sp.sympify(func_input)
except (sp.SympifyError, TypeError):
    st.error("Invalid function input. Please enter a valid mathematical expression.")
    st.stop()
    
#plotting
if plot_type == "2D":
    x_vals = np.linspace(x_min, x_max, 800)
    f_lamdified = sp.lambdify(x, func_expr, modules=["numpy"])
    
    try:
        y_vals = f_lamdified(x_vals)
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name="f(X)"))
        
        #derivative
        if show_derivative:
            derivative_expr = sp.diff(func_expr, x)
            derivative_lambdified = sp.lambdify(x, derivative_expr, modules=["numpy"])
            y_derivative_vals = derivative_lambdified(x_vals)
            fig.add_trace(go.Scatter(x=x_vals, y=y_derivative_vals, mode='lines', name="f'(X)"))
            
        #integral
        if show_integral:
            integral_expr = sp.integrate(func_expr, x)
            integral_lambdified = sp.lambdify(x, integral_expr, modules=["numpy"])
            y_integral_vals = integral_lambdified(x_vals)
            fig.add_trace(go.Scatter(x=x_vals, y=y_integral_vals, mode='lines', name="∫f(X) dX"))
            
        fig.update_layout(
            title = f"2D plot of {func_input}",
            xaxis_title="X-axis",
            yaxis_title="Y-axis",
            template="plotly_white"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        #save image
        img_bytes = fig.to_image(format="png")
        st.download_button(
            label="Download Plot as PNG",
            data=BytesIO(img_bytes),
            file_name="plot.png",
            mime="image/png"
        )
    except Exception as e:
        st.error(f"Error in plotting: {e}")

else:
    x_vals = np.linspace(x_min, x_max, 200)
    y_vals = np.linspace(y_min, y_max, 200)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    try:
        f_lambdified_3d = sp.lambdify((x, y), func_expr, modules=["numpy"])
        Z = f_lambdified_3d(X, Y)

        fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
        fig.update_layout(
            title=f"3D Surface Plot of {func_input}",
            scene=dict(xaxis_title="x", yaxis_title="y", zaxis_title="f(x, y)"),
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Save as image
        img_bytes = fig.to_image(format="png")
        st.download_button(
            label="💾 Download Plot as PNG",
            data=BytesIO(img_bytes),
            file_name="3d_graph.png",
            mime="image/png"
        )
    except Exception as e:
        st.error(f"Error in plotting: {e}")
        
# Add a footer
st.markdown("---")
st.markdown("Made with ❤️ by [Anurag Panda](https://linkedin.com/in/anurag-panda-)")





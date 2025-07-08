import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Advanced Lab Data Plotter", layout="wide")
st.title("📊 Advanced Lab Data Plotter")

tab1, tab2 = st.tabs(["📁 Upload CSV", "📝 Manual Table Input"])

# Function to plot multiple curves
def plot_curves(df, x_col, y_cols, xlim, ylim):
    fig, ax = plt.subplots()

    for y_col in y_cols:
        ax.plot(df[x_col], df[y_col], marker='o', linestyle='-', label=y_col)

    ax.set_xlabel(x_col)
    ax.set_ylabel("Values")
    ax.set_title("Lab Data Plot (Multi-Curve)")
    ax.legend()
    ax.grid(True)

    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)

    st.pyplot(fig)

    # Download as PNG
    from io import BytesIO
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    st.download_button("Download Plot as PNG", buffer.getvalue(), "plot.png", "image/png")

# ============================
# 📁 CSV Upload Tab
# ============================

with tab1:
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.subheader("🔍 Preview")
        st.dataframe(df)

        x_col = st.selectbox("Select X-axis", df.columns)
        y_cols = st.multiselect("Select Y-axis (one or more)", df.columns, default=[df.columns[1]])

        col1, col2 = st.columns(2)
        with col1:
            xmin = st.number_input("X-axis Min", value=float(df[x_col].min()))
            xmax = st.number_input("X-axis Max", value=float(df[x_col].max()))
        with col2:
            ymin = st.number_input("Y-axis Min", value=float(df[y_cols[0]].min()))
            ymax = st.number_input("Y-axis Max", value=float(df[y_cols[0]].max()))

        if st.button("📈 Plot CSV Data"):
            plot_curves(df, x_col, y_cols, (xmin, xmax), (ymin, ymax))

# ============================
# 📝 Manual Table Tab
# ============================

with tab2:
    num_cols = 3
    st.subheader("🖋️ Define Column Headers First")

    headers = [st.text_input(f"Header for Column {i+1}", value=f"Column {i+1}") for i in range(num_cols)]
    default_values = [[0]*5 for _ in range(num_cols)]
    manual_df = pd.DataFrame(dict(zip(headers, default_values)))
    manual_df = st.data_editor(manual_df, num_rows="dynamic")
    manual_df = manual_df.astype(float)

    
    st.write("Enter data manually or edit the table below:")

    # default_data = pd.DataFrame(manual_df)

    # manual_df = st.data_editor(default_data, num_rows="dynamic", use_container_width=True)

    x_col_m = st.selectbox("Select X-axis", manual_df.columns, key="x_col_manual")
    y_cols_m = st.multiselect("Select Y-axis (one or more)", manual_df.columns.drop(x_col_m), default=[manual_df.columns[1]], key="y_col_manual")

    col3, col4 = st.columns(2)
    with col3:
        xmin_m = st.number_input("X-axis Min", value=float(manual_df[x_col_m].min()), key="xmin_manual")
        xmax_m = st.number_input("X-axis Max", value=float(manual_df[x_col_m].max()), key="xmax_manual")
    with col4:
        ymin_m = st.number_input("Y-axis Min", value=float(manual_df[y_cols_m[0]].min()), key="ymin_manual")
        ymax_m = st.number_input("Y-axis Max", value=float(manual_df[y_cols_m[0]].max()), key="ymax_manual")

    if st.button("📈 Plot Manual Data"):
        plot_curves(manual_df, x_col_m, y_cols_m, (xmin_m, xmax_m), (ymin_m, ymax_m))

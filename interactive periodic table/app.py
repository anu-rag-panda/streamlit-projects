import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Interactive Periodic Table", layout="wide")
st.title("🧪 Interactive Periodic Table")

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json"
    df = pd.read_json(url)
    elements = pd.json_normalize(df["elements"])
    if 'category' in elements.columns:
        elements['groupBlock'] = elements['category']  # Map category to groupBlock if needed
    return elements

elements = load_data()

# Verify available columns before filtering
if 'groupBlock' not in elements.columns:
    st.error("Column 'groupBlock' not found in data. Available columns: " + ", ".join(elements.columns))
    st.stop()

# # Sidebar Filters
# st.sidebar.header("🔍 Filters")
# group_filter = st.sidebar.multiselect("Select Group(s):", options=sorted(elements["groupBlock"].dropna().unique()), default=sorted(elements["groupBlock"].unique()))
# phase_filter = st.sidebar.multiselect("Select Phase(s):", options=sorted(elements["phase"].dropna().unique()), default=sorted(elements["phase"].unique()))

# filtered_elements = elements[(elements["groupBlock"].isin(group_filter)) & (elements["phase"].isin(phase_filter))]

# Color map by groupBlock
color_map = {
    "alkali metal": "#f94144", "alkaline earth metal": "#f3722c", "transition metal": "#f9844a",
    "post-transition metal": "#f9c74f", "metalloid": "#90be6d", "nonmetal": "#43aa8b",
    "halogen": "#577590", "noble gas": "#277da1", "lanthanoid": "#9d4edd", "actinoid": "#5f0f40"
}
elements['color'] = elements['groupBlock'].map(color_map).fillna("#adb5bd")

# Layout for Periodic Table
rows, cols = 10, 18
grid = [[None]*cols for _ in range(rows)]

for _, row in elements.iterrows():
    x, y = int(row['xpos']) - 1, int(row['ypos']) - 1
    grid[y][x] = row

# Display the Periodic Table
for row in grid:
    cols = st.columns(18)
    for i, elem in enumerate(row):
        if elem is None:
            cols[i].empty()
        else:
            with cols[i]:
                # Check if element data exists and convert to string safely
                symbol = str(elem.get('symbol', ''))
                number = str(elem.get('number', ''))
                color = elem.get('color', '#adb5bd')
                name = str(elem.get('name', ''))
                
                # Create a tooltip with basic element info
                tooltip_text = f"""
                Name: {name}
                Atomic Number: {number}
                Category: {elem.get('groupBlock', 'N/A')}
                Phase: {elem.get('phase', 'N/A')}
                """
                
                st.markdown(f"""
                    <div style="position:relative;" title="{name} - {elem.get('groupBlock', 'N/A')}">
                    <div style="background-color:{color}; border-radius:10px; padding:8px; text-align:center; color:white">
                        <strong>{symbol}</strong><br/>
                        <small>{number}</small>
                    </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Button to select element
                if st.button(f"{symbol}", key=symbol):
                    st.session_state['element_details'] = elem

# Element Details
if 'element_details' in st.session_state:
    elem = st.session_state['element_details']
    st.markdown("---")
    st.subheader(f"🔬 Details of {elem.get('name', 'Unknown')} ({elem.get('symbol', 'Unknown')})")
    st.markdown(f"""
    - *Atomic Number*: {elem.get('number', 'N/A')}
    - *Symbol*: {elem.get('symbol', 'N/A')}
    - *Name*: {elem.get('name', 'N/A')}
    - *Atomic Mass*: {elem.get('atomic_mass', 'N/A')}
    - *Category*: {elem.get('groupBlock', 'N/A')}
    - *Phase*: {elem.get('phase', 'N/A')}
    - *Density*: {elem.get('density', 'N/A')} g/cm³
    - *Melting Point*: {elem.get('meltingPoint', 'N/A')} K
    - *Boiling Point*: {elem.get('boilingPoint', 'N/A')} K
    - *Electron Configuration*: {elem.get('electronConfiguration', 'N/A')}
    - *Year Discovered*: {elem.get('yearDiscovered', 'N/A')}
    """)
    
    
st.markdown("---")
st.markdown("Made with ❤️ by [Anurag Panda](https://linkedin.com/in/anurag-panda-)")
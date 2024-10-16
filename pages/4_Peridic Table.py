import streamlit as st
import pandas as pd


st.set_page_config(page_title="Periodic Table", page_icon=":bar_chart:", layout="wide", initial_sidebar_state="auto")
# Load the periodic table data
def load_data():
    try:
        df = pd.read_csv('elements.csv')
        return df
    except Exception as e:
        st.error(f"Error loading the file: {e}")
        return pd.DataFrame()  # Return empty DataFrame in case of an error

df = load_data()

# Sidebar Filters
st.sidebar.header('Filter Elements')

# Filter by Group (s, p, d, f)
group_filter = st.sidebar.multiselect(
    'Select Group', 
    options=df['Group'].unique(),
)

# Filter by Acidity (acid, base, neutral)
acidity_filter = st.sidebar.multiselect(
    'Select Acidity', 
    options=df['Acidity'].unique(),
)

# Filter by State (solid, liquid, gas)
state_filter = st.sidebar.multiselect(
    'Select State (Room Temperature)', 
    options=df['State'].unique(),
)


# Apply filters only if values are selected, otherwise show all data
filtered_df = df.copy()

if group_filter:
    filtered_df = filtered_df[filtered_df['Group'].isin(group_filter)]

if acidity_filter:
    filtered_df = filtered_df[filtered_df['Acidity'].isin(acidity_filter)]

if state_filter:
    filtered_df = filtered_df[filtered_df['State'].isin(state_filter)]

# Display the interactive periodic table
st.subheader('Interactive Periodic Table', divider="red")

# Custom CSS to increase table size and ensure it fits nicely in the Streamlit app
st.markdown("""
    <style>
    .dataframe-container {
        width: 100%;
        overflow-x: auto;
        height: 100px;
    }
    .dataframe-container table {
        width: 100%; /* Adjust width as needed */
        font-size: 14px; /* Adjust font size as needed */
    }
    </style>
""", unsafe_allow_html=True)

# Display the filtered table
# Use Streamlit's built-in dataframe display for simplicity
columns_to_display = ['Element', 'Symbol', 'Atomic Number','Atomic Weight', 'Valency','Acidity', 'Group', 'State']
filtered_df = filtered_df[columns_to_display]

st.dataframe(filtered_df, use_container_width=True, height=420)  # Adjust width as needed

# Display individual element details when clicked
if not filtered_df.empty:
    selected_element = st.selectbox('Select an Element', options=[''] + filtered_df['Element'].tolist(), index=0)
    st.write(f"You selected: {selected_element}")
    if selected_element:
        element_info = df[df['Element'] == selected_element].iloc[0]
        # Convert element_info to DataFrame for tabular display
        element_df = pd.DataFrame([{
            'Element': element_info['Element'],
            'Symbol': element_info['Symbol'],
            'Atomic Number': element_info['Atomic Number'],
            'Atomic Weight': element_info['Atomic Weight'],
            'Valency': element_info['Valency'],
            'Color' : element_info['Color'],
            'Octet': element_info['Octet'],
            'Group': element_info['Group'],
            'Acidity': element_info['Acidity'],
            'State at Room Temperature': element_info['State'],
            'Density': element_info['Density'],
            'Melting Point': element_info['Melting_Point'],
            'Boiling Point': element_info['Boiling_Point'],
            'Electronic Configuration': element_info['Electron_Configuration'],
            'Electric Conductivity': element_info['Electrical_Type']    
        }]
        )
        # Display as a table
        st.subheader("Element Details", divider="red")
        st.dataframe(element_df , use_container_width=True) 
st.info("Use the sidebar to filter elements!", icon="ℹ️")

st.sidebar.subheader("About Interactive Periodic Table: ", divider="orange")
st.sidebar.info("The Interactive Periodic Table is an educational and research-oriented tool designed to help users explore chemical elements with ease. This app offers a streamlined and visually appealing way to filter and investigate the properties of elements based on various chemical and physical attributes. The goal is to provide chemistry and students, educators with an accessible, interactive, and informative platform to study the periodic table.",)

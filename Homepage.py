import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Chemical Reaction Simulator",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS to style the page
st.markdown("""
    <style>
        .landing-title {
            font-size: 50px;
            color: #4A90E2;
            # text-align: center;
            font-weight: bold;
        }
        .landing-subtitle {
            font-size: 24px;
            color: #555;
            # text-align: center;
            margin-top: -10px;
        }
        
        .feature-section {
            margin-top: 10px;
        }
        .feature-section h3 {
            # text-align: center;
            color: #333;
        }
        .feature-section p {
            # text-align: center;   
            color: #777;
        }
        .footer {
            # text-align: center;
            margin-top: 50px;
            color: #aaa;
        }
        .footer a {
            color: #4A90E2;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='landing-title'>Welcome to the <span style='color: #f78393;'>ChemTech</span></h1>", unsafe_allow_html=True)
st.markdown("<p class='landing-subtitle'>Your Gateway to Advanced Chemical Learning and Simulation!</p>", unsafe_allow_html=True)

st.markdown("""
<div class='feature-section' style="margin-bottom: 50px;">
    <h2 style = "color: #4A90E2;">Why use our AI-powered tool?</h2>
    <p >🔍 Explore over 100+ elements and their properties.</p>
    <p> 📖 Easy understanding of Name Reactions</p>
    <p>⚡ Simulate reactions with customized conditions and catalysts.</p>
    <p>🎨 Get detailed information on products, including structure and properties.</p>
    <p>📊 Visualize molecular weights and densities in a tabular format.</p>
    
</div>
""", unsafe_allow_html=True)

left, middle, right = st.columns(3, gap="small")
with left:
    # st.markdown ("Perform any reaction chemical reaction in seconds !")
    if st.button("⚗️ Basic Reactions", type="secondary", use_container_width=True):
        st.switch_page("pages/3_Reaction Simulator.py")
    

with middle:    
    if st.button("👩‍🔬 Name Reactions", type="secondary", use_container_width=True):
        st.switch_page("pages/2_Name_Reactions.py")
    

with right:
    if st.button("📊 Periodic Table", type="secondary", use_container_width=True):
        st.switch_page("pages/4_Peridic Table.py")
    

with st.sidebar:
    st.subheader("Made with ❤️ by ChemTech", divider="red")
    st.image("chem.gif", use_column_width=True,width=None)

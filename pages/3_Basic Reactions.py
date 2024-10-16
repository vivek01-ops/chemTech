from cgitb import text
import streamlit as st
import os
import time
import google.generativeai as genai
import pandas as pd

os.environ["GOOGLE_API_KEY"] = "AIzaSyAdS57TfssxTs_Z0_YTXB3kikFv7KqWtA0"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def load_elements():
    return pd.read_csv('elements.csv')

# Load elements data
elements_df = load_elements()
#Page confiquration 
st.set_page_config(page_title="Reaction Simulator", page_icon="⚗️", layout="wide", initial_sidebar_state="auto")

# Title and Introduction
st.subheader("Chemical Reaction Simulator", divider="red")
# st.write("Simulate chemical reactions by selecting reactants, catalysts, and conditions.")

# Reactant Selection
reactants = st.multiselect(
   'Select Reactants',
    elements_df['Element'].tolist(),
    placeholder="Select at least one reactant",
    help="Choose the chemicals that will react.",   
)

substrate = st.multiselect(
    'Select Substrate',
    elements_df['Element'].tolist(),
    placeholder="Select at least one substrate",
    help="Choose the chemicals that will react as substrate.",
)

# Catalyst Selection
catalyst = st.selectbox(
    'Select Catalyst (Optional)',
    [
       'None','Platinum (Pt)', 'Iron (Fe)', 'Zinc (Zn)'
    ],
    help="Choose the chemicals that will react.",   
)

temperature = st.number_input('Temperature (K)', min_value=0, max_value=1000, value=300, step=1)
doubt = st.text_input('Any question about the reaction?')

# Trigger the Reaction Simulation
if st.button('Perform Reaction'):
    st.toast('The result will be generated shortly, please wait a moment!')
    time.sleep(5)
    if reactants:
        # Display input parameters
        st.write(f"**Reactants:** {', '.join(reactants)}")
        st.write(f"**Catalyst:** {catalyst}")
        st.write(f"**Temperature:** {temperature} K")
        st.write(f"**Substrate:** {', '.join(substrate)}")
        
        with st.status('Performing the reaction...', expanded=True):
            for seconds in range(40):
                st.write(f"⏳ {seconds} seconds have passed")
                time.sleep(1)
            st.write(":material/check:Wait")
            
            reaction_representation = (
            f"""
            **Reaction**:
            **Reactants:** {reactants[0]} + {substrate[0]} --(**Temp:** {temperature} K)--> 
            **Products:** 
            """.strip()
        )

        # Initialize the generative model
            model = genai.GenerativeModel("gemini-1.5-pro-002")
            response = model.generate_content(
                f"Perform a chemical reaction under the following conditions and provide a list of all possible products in tabular form with their chemical names and symbols:\n"
                f"Reactants: {', '.join(reactants)}\n"
                f"Substrate: {', '.join(substrate)}\n"
                f"Catalyst: {catalyst}\n"
                f"Temperature: {temperature} K\n"
                f"Let me know if you have any questions about the reaction: {doubt}\n"
                f"Display the reaction with proper format:\n\n"
                f"{reaction_representation}\n\n"
                f"Provide the molecular weight and molecular density of the products in a table.\n"
                f"Describe the products’ properties (color, odor, taste, state, gas emission, etc.).\n"
                f"Include key details about the catalyst (if any) in bullet points."
            )

            # Assuming 'response' contains the products information in some format
            # Parse the response to extract actual products (This part may vary based on the response structure)
            # Example response parsing (customize according to your model response format):
            # Assuming the response format is like: "Products: Product1 (C1), Product2 (C2), ..."

            if response:
                # Example of how you might extract the products from the response (customize as needed)
                # Let's say the response contains a list of products in some format.
                products = ["Product 1 (C1)", "Product 2 (C2)"]  # Replace this with actual extraction logic
                actual_products = ', '.join(products)

                # Update the ASCII representation with the actual products
                reaction_representation = (
                    f"""
                    Reaction:
                    Reactants: {reactants[0]} + {substrate[0]} --(Temp: {temperature} K)--> 
                    Products: {actual_products}
                    """.strip()
                )


            # Display the result of the reaction
            result = response.text
            sections = result.split("\n\n")  # Assuming the response is divided by two newlines between sections
            st.write(result)
        
        st.success("Done", **{"icon": "✔"})
        st.write("Result is generated by Generative AI, it can make mistakes in some cases, please cross check the result from your side")
    else:
        st.error("Please select at least one reactant.")
        
st.sidebar.subheader("About Reaction Simulator: ", divider="orange")
st.sidebar.info("📌 The Chemical Reaction Simulator is a powerful, AI-driven tool designed to simulate chemical reactions dynamically by allowing users to select various chemical elements, catalysts, and conditions. It leverages Generative AI to predict possible reaction outcomes, generating insightful information about the resulting products, including their properties, molecular weight, and density.",)

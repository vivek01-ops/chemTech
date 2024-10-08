from cgitb import text
import streamlit as st
import os
import time
import google.generativeai as genai
import pandas as pd

# Set up API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAdS57TfssxTs_Z0_YTXB3kikFv7KqWtA0"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

st.set_page_config(page_title="Name Reactions", page_icon="🧪", layout="wide", initial_sidebar_state="auto")

# Data for Name Reactions
name_reactions = {
    "Sr.No": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    ],
    "Reaction Name": [
        "Pinnacle-Pinacalon rearrangement",
        "Hafman's reaction",
        "Baeyer-Villiger oxidation",
        "Benzilic acid rearrangement",
        "Beckmann's rearrangement",
        "Claisen-Schmidt condensation",
        "Schmidt rearrangement",
        "Clemmensen reduction",
        "Wolff rearrangement",
        "Oppenauer oxidation",
        "Dakin reaction",
        "Birch reduction"
    ],
    "Description": [
        "Rearrangement of pinacol to pinacolone through acid catalysis.",
        "Elimination of an alcohol from a β-hydroxy ketone to form an α,β-unsaturated carbonyl compound.",
        "Oxidation of ketones to esters using peracids (e.g., peracetic acid).",
        "Rearrangement of benzil to benzilic acid via nucleophilic attack on the carbonyl.",
        "Rearrangement of oximes to amides in the presence of acid.",
        "Condensation of two esters or an ester and a carbonyl compound in the presence of a base.",
        "Rearrangement of primary amides to amines and carboxylic acids upon treatment with nitrous acid.",
        "Reduction of ketones or aldehydes to alkanes using zinc amalgam and hydrochloric acid.",
        "Rearrangement of α-ketoacids to form isocyanides upon treatment with a base.",
        "Oxidation of alcohols to ketones using aluminum alkoxides as catalysts.",
        "Reaction of aromatic aldehydes with hydrogen peroxide to form phenols.",
        "Reduction of aromatic compounds to cyclohexadienes using sodium in liquid ammonia."
    ],
    "Molecular Formula": [
        "C6H12O2 (Pinacol); C6H10O (Pinacolone)",
        "C6H10O (β-hydroxy ketone); C6H10O (α,β-unsaturated carbonyl)",
        "C4H8O2 (Acetic acid); C5H10O2 (Ethyl acetate)",
        "C14H12O3 (Benzilic acid)",
        "C5H9NO (Oxime); C5H11NO (Amide)",
        "C9H10O2 (Alkylated product)",
        "C4H9NO (Amide); C5H11NO2 (Amines and acids)",
        "C6H12O (Ketone); C6H14 (Alkane)",
        "C3H4O2 (α-keto acid); C3H5NO (Isocyanide)",
        "C6H14O (Alcohol); C6H12O (Ketone)",
        "C6H6O (Phenol)",
        "C6H6 (Benzene); C6H10 (Cyclohexadiene)"
    ]
}

# Data for Benzene Reactions
benzene_reactions = {
    "Sr.No": [
        1, 2, 3, 4, 5
    ],
    "Reaction Name": [
        "Halogenation",
        "Nitration",
        "Sulfonation",
        "Friedel-Crafts Alkylation",
        "Friedel-Crafts Acylation"
    ],
    "Reaction Overview": [
        "Electrophilic aromatic substitution of benzene with halogens (Cl₂, Br₂).",
        "Electrophilic aromatic substitution of benzene with nitric acid to form nitrobenzene.",
        "Electrophilic aromatic substitution of benzene with sulfur trioxide (SO₃) to form benzene sulfonic acid.",
        "Electrophilic aromatic substitution where an alkyl group is introduced into benzene.",
        "Electrophilic aromatic substitution where an acyl group is introduced into benzene."
    ],
    "Catalyst": [
        "FeCl₃ (Ferric chloride) or AlCl₃ (Aluminum chloride)",
        "H₂SO₄ (Sulfuric acid)",
        "H₂SO₄ (Sulfuric acid)",
        "AlCl₃ (Aluminum chloride)",
        "AlCl₃ (Aluminum chloride)"
    ]
}


# Function to load elements from CSV
def load_elements():
    return pd.read_csv('elements.csv')

elements_df = load_elements()


# Create DataFrames

st.title("Name Reactions")

st.subheader("Have a quick revision on Name and Benzene Reactions", divider="red")
df1 = pd.DataFrame(name_reactions)
df2 = pd.DataFrame(benzene_reactions)
with st.expander("Show Name Reactions"):
        st.dataframe(df1, use_container_width=True, hide_index=True)
with st.expander("Show Benzene Reactions"):
        st.dataframe(df2, use_container_width=True, hide_index=True)

# Create two columns for input and output
# col1, col2 = st.columns([1, 2.5], gap="large")

# User input for reaction details
st.subheader("Perform Name Reactions", divider="red")
    
    # Input fields for user to enter new reaction details
reaction_name = st.selectbox(
        'Select Name Reaction',
        df1['Reaction Name'].tolist(),
        placeholder="Select at least one reaction",
        help="Choose the Name Reaction you want to perform.",
    )
benzene = st.selectbox(
        'Select Benzene Reaction',
        df2['Reaction Name'].tolist(),
        placeholder="Select at least one reaction",
        help="Choose the Benzene Reaction you want to perform.",
)
compounds = st.text_input(
        'Enter Compound (separated by commas)',
        placeholder="Enter compounds",
        help="Enter the compound you want to perform the reaction on.",
)

substrate = st.multiselect(
        'Select Substrate',
        elements_df['Element'].tolist(),
        placeholder="Select at least one substrate",
        help="Choose the chemicals that will react as substrate.",
    )
temperature = st.number_input('Temperature (K)', min_value=0, max_value=1000, value=300, step=1)    

    # Trigger the Reaction Simulation
if st.button('Perform Reaction'):
        if reactants:
            # Display input parameters
            st.write(f"**You Selected:** {reaction_name}")
            st.write(f"**You Selected:** {benzene}")
            st.header("Reaction Information")   
        
            with st.status('Performing the reaction...', expanded=True):
                try:
                    # Send prompt to Google genai API
                    model = genai.GenerativeModel("gemini-1.5-pro-002")
                    # Combine the prompt into one string
                    prompt = (
                        f"Provide detailed information on the {reaction_name} reaction, including: "
                        f"1. Definition, "
                        f"2. Conditions (temperature, catalyst, etc.), "
                        f"3. Mechanism, and "
                        f"4. General structure of the product in ASCII format.\n"
                        f"Provide detailed information on the {benzene} reaction, including: "
                        f"1. Definition, "
                        f"2. Conditions (temperature, catalyst, etc.), "
                        f"3. Mechanism, and "
                        f"4. General structure of the product in ASCII format.\n"   
                        f"Also, simulate a reaction using the reactants {', '.join(reactants)} and the substrates {', '.join(substrate)} "
                        f"under the typical conditions of {reaction_name}, and describe the expected product with its chemical names."
                    )

                    response = model.generate_content(prompt)
                    
                    # Display the result of the reaction
                    result = response.text
                    sections = result.split("\n\n")   # Assuming the response is divided by two newlines between sections
                    st.write(result)
                    st.success("Done", **{"icon": "✔"})
                except Exception as e:
                    st.error(f"**Error:** There was an issue with the API request: {e}")
        else:
            st.error("Please select at least one reactant.")

st.sidebar.subheader("About Name Reaction Simulator: ", divider="orange")
st.sidebar.info("The Name Reactions and Benzene Reactions Simulator is an advanced AI-powered tool designed to help chemistry students to explore, learn and simulate chemical reactions. The app focuses on well-known Name Reactions and Benzene Reactions, offering detailed information about the mechanisms, conditions, and products of these reactions. Additionally, users can simulate reactions by selecting specific reactants and substrates, with detailed results generated using Generative AI.",)



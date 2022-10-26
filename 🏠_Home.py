import pandas as pd
import os
import streamlit as st

from mobility.constants import motifs, moyens, tuus
from mobility.datasets import load_data



st.title("Mobilité des personnes 2019")
st.header("Objectifs")
st.markdown("""
    Le but de ce dashboard est d'analyser les données de mobilité des personnes mises à disposition par le ministère du développement durable et solidaire en **2019**.
""")

st.header("Données")
st.markdown("""
    Données prises depuis [le site du mtes](https://www.statistiques.developpement-durable.gouv.fr/resultats-detailles-de-lenquete-mobilite-des-personnes-de-2019?rubrique=60&dossier=1345).
""")

df = load_data()
st.success(f"Données chargées! **{len(df)}** déplacements récupérés.", icon="✅")
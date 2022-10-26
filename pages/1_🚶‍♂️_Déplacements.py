import pandas as pd
import os
import streamlit as st

from mobility.constants import motifs, moyens, tuus
from mobility.datasets import load_data


def build_distribution_df(series, digits=3):
    df = series.sort_values(ascending=False).to_frame()
    df["ratio"] = df[series.name] / series.sum()
    df["cumratio"] = df["ratio"].cumsum()
    df = df.rename(columns={series.name: "count"})
    return df.style.format(
        {
            "count": "{:,.0f}".format,
            "ratio": "{:,.2%}".format,
            "cumratio": "{:,.2%}".format,
        }
    )


st.title("Analyse des déplacements")

fn = "~/Downloads/donnees_individuelles_anonymisees_emp2019_V2/k_deploc_public_V2.csv"
df = load_data()
# with st.sidebar:
with st.expander(label="Filtres", expanded=False):
    region = st.selectbox(
        label="Région",
        options=sorted(
            [""]
            + list(df.loc[~pd.isnull(df["REG_DES"])]["REG_DES"].astype(str).unique())
        ),
    )
    tuu = st.selectbox(
        label="Taille d'unité urbaine", options=[""] + list(tuus["name"]), index=0
    )
    motif = st.selectbox(label="Motif", options=[""] + list(motifs["name"]), index=0)
    col1, col2 = st.columns(2)
    with col1:
        distance_min = st.slider(
            "Distance min", min_value=0, max_value=100, value=0, step=1
        )
    with col2:
        distance_max = st.slider(
            "Distance max", min_value=1, max_value=100, value=100, step=1
        )

predicate = f"(MDISTTOT_fin >= {distance_min}) and (MDISTTOT_fin < {distance_max})"
if motif:
    df = df.loc[df["MMOTIFDES"] == motif.split(" - ")[0]]
if region:
    df = df.loc[df["REG_DES"] == region]
if tuu:
    df = df.loc[df["TUU2017_ORI"] == float(tuu.split(" - ")[0])]
df = df.query(predicate)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Déplacements", value=len(df))
with col2:
    st.metric(label="Individus", value=df["IDENT_IND"].nunique())
with col3:
    st.metric(label="Ménages", value=df["IDENT_MEN"].nunique())
with col4:
    st.metric(label="Durée moyenne (min)", value=df["DUREE"].mean().round(1))
st.subheader("Distribution des déplacements par famille de motifs")
st.dataframe(
    build_distribution_df(df.groupby("moyen_groupe_1")["IDENT_DEP"].count()),
    use_container_width=True,
)
st.subheader("Distribution des déplacements par motif")
st.dataframe(
    build_distribution_df(df.groupby("moyen_1")["IDENT_DEP"].count()),
    use_container_width=True,
)

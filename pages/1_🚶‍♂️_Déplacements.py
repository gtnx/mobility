import pandas as pd
import os
import streamlit as st

from mobility.constants import motifs, moyens, tuus
from mobility.datasets import load_data

st.set_page_config(layout="wide")


def build_distribution_df(series, digits=3):
    df = series.sort_values("count", ascending=False)
    df["ratio"] = df["count"] / df["count"].sum()
    df["cumratio"] = df["ratio"].cumsum()
    df["vitesse"] = df.eval("distance / durée * 60")
    df = df[
        ["count", "ratio", "cumratio"]
        + [col for col in df.columns if col not in ("count", "ratio", "cumratio")]
    ]
    return df.style.format(
        {
            "count": "{:,.0f}".format,
            "ratio": "{:,.1%}".format,
            "cumratio": "{:,.1%}".format,
            "durée": "{:,.1f}".format,
            "distance": "{:,.1f}".format,
            "vitesse": "{:,.1f}".format,
        }
    )


st.title("Analyse des déplacements")

fn = "~/Downloads/donnees_individuelles_anonymisees_emp2019_V2/k_deploc_public_V2.csv"
df = load_data()
with st.sidebar:
    # with st.expander(label="Filtres", expanded=False):
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
    moyen = st.selectbox(label="Moyen", options=[""] + list(moyens["name"]), index=0)
    distance_min = st.slider(
        "Distance min", min_value=0, max_value=100, value=0, step=1
    )
    distance_max = st.slider(
        "Distance max", min_value=1, max_value=100, value=100, step=1
    )

predicate = f"(MDISTTOT_fin >= {distance_min}) and (MDISTTOT_fin < {distance_max})"
if motif:
    df = df.loc[df["MMOTIFDES"] == motif.split(" - ")[0]]
if moyen:
    df = df.loc[df["MMOY1S"] == moyen.split(" - ")[0]]
if region:
    df = df.loc[df["REG_DES"] == region]
if tuu:
    df = df.loc[df["TUU2017_ORI"] == float(tuu.split(" - ")[0])]
df = df.query(predicate)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric(label="Déplacements", value=len(df))
with col2:
    st.metric(label="Individus", value=df["IDENT_IND"].nunique())
with col3:
    st.metric(label="Durée moyenne (min)", value=df["DUREE"].mean().round(1))
with col4:
    st.metric(label="Distance moyenne (km)", value=df["MDISTTOT_fin"].mean().round(1))
with col5:
    st.metric(
        label="Vitesse moyenne (km/h)",
        value=(df["MDISTTOT_fin"].mean() / df["DUREE"].mean() * 60).round(1),
    )
aggs = {"IDENT_DEP": "count", "DUREE": "mean", "MDISTTOT_fin": "mean"}
columns = {"IDENT_DEP": "count", "DUREE": "durée", "MDISTTOT_fin": "distance"}

groups = [
    ("moyen_groupe_1", "Distribution des déplacements par famille de moyens"),
    ("moyen_1", "Distribution des déplacements par moyen"),
    ("REG_DES", "Distribution des déplacements par région"),
    ("tuu2017_orig_label", "Distribution des déplacements par taille d'unité urbaine"),
    ("motif_deplacement", "Distribution des déplacements par motif")
]
for key, subheader in groups:
    st.subheader(subheader)
    st.dataframe(
        build_distribution_df(df.groupby(key).agg(aggs).rename(columns=columns)),
        use_container_width=True,
    )

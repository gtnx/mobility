import io
import pandas as pd
import requests
import streamlit as st
import zipfile

from mobility.constants import motifs, moyens, tuus

__all__ = ("load_data",)


@st.cache
def download_data():
    url = "https://www.statistiques.developpement-durable.gouv.fr/sites/default/files/2022-04/donnees_individuelles_anonymisees_emp2019_V2.zip"
    return requests.get(url)


@st.cache
def load_data():
    ret = download_data()
    buf = io.BytesIO(ret.content)
    file = zipfile.ZipFile(buf)
    buf = io.BytesIO(file.read("k_deploc_public_V2.csv"))
    df = pd.read_csv(buf, encoding="latin1", delimiter=";", low_memory=False)
    df["mobloc"] = df["mobloc"].astype(bool)
    for key in ("MMOTIFDES", "MMOY1S", "MMOY2S", "MMOY3S", "MMOY4S"):
        df[key] = df[key].astype(str)
    df["motif_deplacement"] = df.merge(
        motifs, left_on="MMOTIFDES", right_index=True, how="left"
    )["name"]
    df["moyen_1"] = df.merge(moyens, left_on="MMOY1S", right_index=True, how="left")[
        "name"
    ]
    df["moyen_groupe_1"] = df.merge(
        moyens, left_on="MMOY1S", right_index=True, how="left"
    )["group"]
    df["tuu2017_orig_label"] = df.merge(
        tuus, left_on="TUU2017_ORI", right_index=True, how="left"
    )["name"]
    df["distance_bin"] = df["MDISTTOT_fin"].apply(
        lambda x: "1. <=1km"
        if x <= 1
        else "2. <=2km"
        if x <= 2
        else "3. <=5km"
        if x <= 5
        else "4. <=10km"
        if x <= 10
        else "5. <=20km"
        if x <= 20
        else "6. <=50km"
        if x <= 50
        else "7. >50km"
    )
    return df

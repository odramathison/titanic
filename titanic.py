import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

from PIL import Image


############################################################

st.set_page_config(layout="wide")

image = Image.open('titanic.jfif')

st.image(image, use_column_width=True)

st.write("""
# Datos estadisticos del hundimiento del Titanic.
Como fue la tragedia del Titanic visto desde las estadísticas?
***
""")


df = sns.load_dataset('titanic')
# print(df.head())

if st.checkbox('Mostrar el dataframe'):st.write(df)

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button("Presione para descargar", csv, 'files.csv', 'text/csv', key='dowload-csv')


############################################################
   
st.markdown("## Sobrevivientes & Fallecidos por Genero")   ## Main Title

def main():
    page = st.sidebar.selectbox(
        "Seleccione una gráfica:", 
        [
             'Gráfico de Barras', 'Gráfico de Torta'
        ]
    )

    if page == "Gráfico de Barras":
        countPlot()
    
    elif page == "Gráfico de Torta":
        piePlot()


def countPlot():
    fig = plt.figure(figsize=(18, 8))
    sns.countplot(x= 'sex',hue= 'survived', data=df)
    st.pyplot(fig)

def piePlot():
    fig = plt.figure(figsize=(18, 8))
    df['survived'].value_counts().plot.pie(autopct = '%1.1f%%', explode= [0, 0.1], shadow = True)
    st.pyplot(fig)   


if __name__ == "__main__":
    main()
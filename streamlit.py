import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
from PIL import Image
import pickle

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

st.markdown("<h1 style='text-align: center; color: black;'>MONEYBALL DÉPOR</h1>", unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    imagen = Image.open('images/depresivo.jpg')
    st.image(imagen, use_column_width=True)
with col2:
    imagen = Image.open('images/moneyball.jpg')
    st.image(imagen, use_column_width=True)


page = st.sidebar.selectbox("Choose your page", ['Jugador', 'Precio'])

if page == 'Jugador':

    df = pd.read_csv("data/promesas/jovenespromesas.csv")

    st.markdown("<h1 style='text-align: center; color: black;'>Jóvenes promesas</h1>", unsafe_allow_html=True)
    st.write(df)

    @st.cache
    def convert_df(df):
     return df.to_csv().encode('utf-8')
    
    csv = convert_df(df)

    st.download_button(
   "Descargar csv",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )


    col1, col2 = st.columns(2)

    with col1:
        image = Image.open('images/Características Pelayo González.png')
        st.image(image)

    with col2:
        image = Image.open('images/Comparativa jugadores.png')
        st.image(image)



if page == 'Precio':

    
    modelclust = pickle.load(open('notebook/modeloprecio/cluster.pkl', 'rb'))
    clust1 = pickle.load(open('notebook/modeloprecio/model1.pkl', 'rb'))
    clust2 = pickle.load(open('notebook/modeloprecio/model2.pkl', 'rb'))
    clust3 = pickle.load(open('notebook/modeloprecio/model3.pkl', 'rb'))

    edad = st.number_input('Inserte edad: ')
    valoract = st.number_input('Inserte valoración actual: ')
    progres = st.number_input('Inserte progresión: ')
    atac = st.number_input('Inserte valoración ataque: ')
    regt = st.number_input('Inserte valoración regate: ')
    acelr = st.number_input('Inserte valoración aceleración: ')
    tiro = st.number_input('Inserte valoración potencia tiro: ')
    agres = st.number_input('Inserte valoración agresividad: ')
    defen = st.number_input('Inserte valoración defensa: ')
    port = st.number_input('Inserte valoración portería: ')

    X = pd.DataFrame({'edad':[edad],
                      'Valoración_actual':[valoract], 
                      'Progresión':[progres], 
                      'Ataque':[atac], 
                      'Regate':[regt],
                      'Aceleración':[acelr],
                      'Potencia_tiro':[tiro], 
                      'Agresividad':[agres],
                      'Defensa':[defen],
                      'Portería':[port]
                     })

    resultados = modelclust.predict(X)

    if ( resultados == 0 ):
        st.success("El jugador es delantero")
        valor3 = clust3.predict(X)
        print(type(valor3))
        st.success(f"El jugador tiene un valor de {np.round(valor3, 2)} €")
    elif ( resultados == 1 ):
        st.success('El jugador defensa')
        valor1 = clust1.predict(X)
        st.success(f"El jugador tiene un valor de {np.round(valor1, 2)} €")
    else:
        st.success('El jugador es portero')
        valor2 = clust2.predict(X)
        st.success(f"El jugador tiene un valor de {np.round(valor2, 2)} €")
        

    graf = st.button('Gráfico características')

    if graf:
        categories = ['Ataque','Regate','Aceleración',
           'Potencia tiro', 'Agresividad',
          'Defensa', 'Portería']

        r1 = [atac, regt, acelr, tiro, agres, defen, port]

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            name='Jugador 1',
            r= r1,
            theta=categories,
            fill='toself',
            marker=dict(size=5, color = "darkorange")
        ))

        fig.update_layout(
            title = "Gráfico radar características jugador",
            font_size = 15,
            font_family = 'Times New Roman',
            font_color = 'black',
            showlegend = False)

        fig.update_layout(polar = dict(radialaxis = dict(showticklabels = False)))

        fig.show();



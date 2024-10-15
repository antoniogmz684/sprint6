import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('Sprint 6\sprint6\vehicles_us.csv') # leer los datos
hist_cbox = st.checkbox('Construir histograma') #Crea un botón
disp_cbox = st.checkbox('Construir gráfico de dispersión')

if hist_cbox: #Al hacer click en el botón
    #Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    #Crear un histograma
    fig = px.histogram(car_data, x = "odometer")

    #Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width = True)

if disp_cbox:
    #Escribir un mensaje
    st.write("Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches")

    #Crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x = "odometer")

    #Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width = True)
import streamlit as st
import pandas as pd
import plotly.express as px

#Header incluido
st.header("Análisis de datos de vehículos")

#variables para los checkboxes
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_cbox = st.checkbox('Construir histograma') #Crea un botón
disp_cbox = st.checkbox('Construir gráfico de dispersión')


#creación de las gráficas al seleccionar en los checboxes
if hist_cbox: #Al hacer click en el botón
    #Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    #Crear un histograma
    fig = px.histogram(car_data, x = "odometer")

    #Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width = True )

if disp_cbox:
    #Escribir un mensaje
    st.write("Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches")

    #Crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x = "odometer", y = "price", title="Scatter Plot fo Odometer vs Price")

    #Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width = True)
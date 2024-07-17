import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
# crear un histograma
    fig = px.histogram(car_data, color = 'type', x="odometer")
    fig.show()
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


    fig = px.scatter(car_data, x = 'odometer', y = 'price')
    fig.show()

    bar = st.selectbox('Seleccione', car_data ['type'].unique())

    st.dataframe(car_data)

    car_data_bar = car_data[car_data['model_year'] >=1960]

    fig_bar = px.bar(car_data_bar, x= 'model_year', y= 'model_year', orientation="h")
    fig_bar.update_layout(
        tittle= "Grafico de modelo de ano de los vehiculos",
        xaxis_tittle= "Ano",
        yaxis_tittle= "Ano modelo",
        legend_titlle= "Cantidad",
        width= 1000,
        height=600)
    fig_bar-update_traces(marker={"color": "darkcyan"}), # type: ignore
    fig_bar.show()


    
    

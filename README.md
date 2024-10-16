# sprint6
Proyecto de sprint 6 triple ten Antonio Gomez

Esta es una applicación diseñada para la base de datos vehicles_us.csv.
En esta base de datos encontramos datos referentes a:
    -price
    -model_year
    -model
    -condition
    -cylinders
    -fuel
    -odometer
    -transmission
    -type
    -paint_color
    -is_4wd
    -date_posted
    -days_listed

Específciamente la app se enfoca en la distribución del odómetro en la gráfica de histograma y en la relación odómetro-precio en la gráfica de dispersión.

Para la funcionalidad de esta app se usan las librerías: 
    -streamlit: Para crear los chechboxes y los textos explicativos
    -pandas: Para leer la base de datos
    -plotly.express: Para crear las gráficas

Por último se utiliza "if" para indicarle a la app que:
    "Cuando se haga click en la checkbox  de histograma, el programa deberá hasta entonces crear el histograma." Misma cuestión para la el checkbox de dispersión.



Sitio en Render
https://sprint6-2-8k5d.onrender.com/
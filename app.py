# Importar las bibliotecas de la aplicación
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos de anuncios de vehículos
csv_path = Path(__file__).resolve().parent / "vehicles_us.csv"
df = pd.read_csv(csv_path)

# Mostrar el encabezado de la aplicación
st.header("Análisis interactivo del mercado de vehículos usados")

# Control para mostrar el kilometraje de los vehículos
mostrar_histograma = st.checkbox(
    "Ver cuántos kilómetros han recorrido los vehículos"
)

# Mostrar el histograma cuando el usuario active la casilla
if mostrar_histograma:
    fig_histograma = px.histogram(
        df,
        x="odometer",
        nbins=50,
        title="Kilometraje de los vehículos anunciados",
        labels={"odometer": "Kilometraje registrado"}
    )

    # Separar visualmente las barras con un borde naranja
    fig_histograma.update_traces(
        marker_line_color="#F50F0F",
        marker_line_width=0.7
    )

    st.plotly_chart(fig_histograma, use_container_width=True)

# Control para comparar kilometraje y precio
mostrar_dispersion = st.checkbox(
    "Ver cómo se relacionan los kilómetros recorridos y el precio"
)

if mostrar_dispersion:
    # Seleccionar los datos del rango visible
    datos_puntos = df.loc[
        df["odometer"].between(0, 400000)
        & df["price"].between(0, 60000),
        ["odometer", "price"]
    ].copy()

    # Calcular la concentración local de cada punto
    datos_puntos["tramo_km"] = pd.cut(
        datos_puntos["odometer"], bins=80
    )
    datos_puntos["tramo_precio"] = pd.cut(
        datos_puntos["price"], bins=60
    )

    datos_puntos["concentracion"] = datos_puntos.groupby(
        ["tramo_km", "tramo_precio"], observed=True
    )["price"].transform("size")

    # Limitar la escala cromática para distinguir mejor los colores
    limite_color = datos_puntos["concentracion"].quantile(0.95)

    datos_puntos["intensidad"] = datos_puntos[
        "concentracion"
    ].clip(upper=limite_color)

    # Retirar columnas auxiliares de intervalos
    datos_puntos = datos_puntos.drop(
        columns=["tramo_km", "tramo_precio"]
    )

    # Dibujar primero los puntos más concentrados
    datos_puntos = datos_puntos.sort_values(
        "concentracion", ascending=True
    )

    # Todos los anuncios se representan mediante puntos
    fig_dispersion = px.scatter(
        datos_puntos,
        x="odometer",
        y="price",
        color="intensidad",
        color_continuous_scale=[
            [0.00, "#0A1172"],  # Fondo azul marino oscuro
            [0.05, "#1A237E"],  # Azul oscuro
            [0.15, "#2563EB"],  # Azul medio
            [0.25, "#03A9F4"],  # Azul claro
            [0.35, "#27F5E4"],  # Cian
            [0.45, "#4CAF50"],  # Verde base
            [0.55, "#8BC34A"],  # Verde claro
            [0.65, "#CDDC39"],  # Verde-Amarillo
            [0.72, "#FFEB3B"],  # Amarillo puro
            [0.78, "#FFC107"],  # Ámbar
            [0.84, "#FFA000"],  # Naranja claro
            [0.89, "#FF7043"],  # Naranja salmón
            [0.94, "#F4511E"],  # Terracota / Naranja oscuro
            [0.97, "#E53935"],  # Rojo brillante
            [1.00, "#B71C1C"]   # Rojo carmesí (Núcleo absoluto)
        ],
        opacity=0.65,
        render_mode="webgl",
        title="Relación entre kilometraje y precio",
        labels={
            "odometer": "Kilometraje registrado",
            "price": "Precio anunciado",
            "intensidad": "Concentración relativa"
        },
        hover_data={
            "concentracion": True,
            "intensidad": False
        }
    )

    fig_dispersion.update_traces(
        marker={"size": 3}
    )

    fig_dispersion.update_xaxes(range=[0, 400000])
    fig_dispersion.update_yaxes(range=[0, 60000])

    # Mostrar explícitamente el mínimo de la escala de colores
    fig_dispersion.update_coloraxes(
        colorbar=dict(
            tickmode="array",
            tickvals=[1, 50, 100],
            ticktext=["1", "50", "100"]
        )
    )

    st.plotly_chart(fig_dispersion, use_container_width=True)

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

# → Separador de la sección de comparación de precios ← #
st.divider()

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

# → Separador de la sección de comparación de precios ← #
st.divider()

# → Control para comparar fabricantes y tipos de vehículos ← #
mostrar_fabricantes = st.checkbox(
    "Comparar los tipos de vehículos que anuncia cada fabricante"
)

# Mostrar los tipos de vehículos por fabricante #
if mostrar_fabricantes:
    # Preparar los datos sin modificar el dataset original
    df_fabricantes = df.copy()
    df_fabricantes["fabricante"] = (
        df_fabricantes["model"].str.split().str[0]
    )

    # Ordenar los fabricantes por cantidad de anuncios
    orden_fabricantes = (
        df_fabricantes["fabricante"]
        .value_counts()
        .index.tolist()
    )

    # Construir el gráfico de barras apiladas
    fig_fabricantes = px.histogram(
        df_fabricantes,
        x="fabricante",
        color="type",
        category_orders={"fabricante": orden_fabricantes},
        barmode="stack",
        title="Tipos de vehículos por fabricante",
        labels={
            "fabricante": "Fabricante",
            "type": "Tipo de vehículo"
        }
    )

    fig_fabricantes.update_layout(
        xaxis_tickangle=-45,
        yaxis_title="Cantidad de anuncios"
    )

    st.info(
        "💡 **¡Explora el gráfico!** \n\n → **En su leyenda:**\n\n"
        "• Haz clic en un tipo de vehículo para ocultarlo "
        "o mostrarlo.\n\n • Haz doble clic para aislar ese tipo;\n\n"
        "•  Haz doble clic NUEVAMENTE para restaurar las categorías."
    )

    st.plotly_chart(fig_fabricantes, use_container_width=True)

# → Preparar las opciones para comparar precios por fabricante ← #
df_comparacion = df.copy()
df_comparacion["fabricante"] = (
    df_comparacion["model"].str.split().str[0]
)

fabricantes_disponibles = (
    df_comparacion["fabricante"]
    .value_counts()
    .index.tolist()
)

# → Separador de la sección de comparación de precios ← #
st.divider()

# → Comparación interactiva de precios por fabricante ← #
st.subheader("¿Cómo varían los precios entre fabricantes?")

st.write(
    "Compara los precios anunciados de distintas marcas de vehículos. "
    "Selecciona dos o más fabricantes para explorar sus diferencias."
)

st.info(
    "💡 **¿Cómo interpretar la gráfica?**\n\n"
    "• La línea dentro de cada caja representa el precio mediano.\n\n"
    "• La caja contiene el 50 % central de los precios.\n\n"
    "• Los puntos fuera de los bigotes '•  • •├───[ █ ▏ ░ ]───┤• •  •' representan valores atípicos.\n\n"
    "• El eje vertical utiliza una escala logarítmica para facilitar "
    "la comparación de precios muy diferentes."
)

fabricantes_seleccionados = st.multiselect(
    "Selecciona los fabricantes que deseas comparar",
    options=fabricantes_disponibles,
    default=["ford", "toyota"],
    key="selector_fabricantes_precios"
)

# → Mostrar la comparación de precios por fabricante ← #
if fabricantes_seleccionados:
    df_precios_seleccionados = df_comparacion[
        df_comparacion["fabricante"].isin(fabricantes_seleccionados)
    ]

    fig_comparacion = px.box(
        df_precios_seleccionados,
        x="fabricante",
        y="price",
        category_orders={"fabricante": fabricantes_seleccionados},
        log_y=True,
        title="Comparación de precios entre fabricantes",
        labels={
            "fabricante": "Fabricante",
            "price": "Precio (USD)"
        }
    )

    fig_comparacion.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_comparacion, use_container_width=True)
else:
    st.info(
        "Selecciona al menos un fabricante para visualizar "
        "la distribución de precios."
    )

# → Búsqueda de vehículos según las preferencias del consumidor ← #
st.divider()

st.subheader("🚗 Encuentra tu próximo vehículo")

st.write(
    "Explora los anuncios de vehículos usados y encuentra opciones "
    "que se ajusten a tu presupuesto y al kilometraje que buscas."
)

st.info(
    "💡 **Personaliza tu búsqueda**\n\n"
    "Establece los límites de precio y kilometraje. "
    "La aplicación mostrará los anuncios que cumplan tus criterios, "
    "ordenados según tu prioridad.\n\n"
    "**Importante:** Los resultados son opciones de búsqueda, "
    "no recomendaciones de compra verificadas."
)

# → Controles de precio y kilometraje ← #

st.markdown("#### 💰 Presupuesto del vehículo")

precio_minimo = st.number_input(
    "Precio mínimo (USD)",
    min_value=0,
    max_value=375000,
    value=1000,
    step=500,
    key="busqueda_precio_minimo"
)

precio_maximo = st.number_input(
    "Precio máximo (USD)",
    min_value=0,
    max_value=375000,
    value=16000,
    step=500,
    key="busqueda_precio_maximo"
)

st.markdown("#### 🚘 Kilometraje del vehículo")

kilometraje_minimo = st.number_input(
    "Kilometraje mínimo",
    min_value=0,
    max_value=990000,
    value=1000,
    step=1000,
    key="busqueda_km_minimo"
)

kilometraje_maximo = st.number_input(
    "Kilometraje máximo",
    min_value=0,
    max_value=990000,
    value=80000,
    step=10000,
    key="busqueda_km_maximo"
)

# → Prioridad de búsqueda ← #
prioridad_busqueda = st.radio(
    "¿Qué prefieres priorizar?",
    options=[
        "Menor precio",
        "Menor kilometraje",
        "Equilibrio entre precio y kilometraje"
    ],
    key="busqueda_prioridad"
)

# → Filtrar vehículos según las preferencias del consumidor ← #

if precio_minimo > precio_maximo:
    st.warning("El precio mínimo no puede superar el precio máximo.")

elif kilometraje_minimo > kilometraje_maximo:
    st.warning(
        "El kilometraje mínimo no puede superar el kilometraje máximo."
    )

else:
    vehiculos_encontrados = df.loc[
        df["price"].between(precio_minimo, precio_maximo)
        & df["odometer"].between(kilometraje_minimo, kilometraje_maximo)
    ].copy()

    # Aplicar el criterio de ordenamiento seleccionado
    if prioridad_busqueda == "Menor precio":
        vehiculos_encontrados = vehiculos_encontrados.sort_values(
            by=["price", "odometer"],
            ascending=[True, True]
        )

    elif prioridad_busqueda == "Menor kilometraje":
        vehiculos_encontrados = vehiculos_encontrados.sort_values(
            by=["odometer", "price"],
            ascending=[True, True]
        )

    else:
        # Equilibrar precio y kilometraje dentro de los resultados
        if not vehiculos_encontrados.empty:
            rango_precio = vehiculos_encontrados["price"].max(
            ) - vehiculos_encontrados["price"].min()
            rango_km = vehiculos_encontrados["odometer"].max(
            ) - vehiculos_encontrados["odometer"].min()

            puntuacion_precio = (
                (vehiculos_encontrados["price"] -
                 vehiculos_encontrados["price"].min())
                / rango_precio
                if rango_precio > 0 else 0
            )

            puntuacion_km = (
                (vehiculos_encontrados["odometer"] -
                 vehiculos_encontrados["odometer"].min())
                / rango_km
                if rango_km > 0 else 0
            )

            vehiculos_encontrados["puntuacion"] = (
                puntuacion_precio + puntuacion_km
            ) / 2

            vehiculos_encontrados = vehiculos_encontrados.sort_values(
                by=["puntuacion", "price", "odometer"]
            )

    st.write(
        f"**Anuncios encontrados: {len(vehiculos_encontrados):,}**"
    )

    if vehiculos_encontrados.empty:
        st.warning(
            "No encontramos anuncios con estos criterios. "
            "Prueba ampliando los intervalos de búsqueda."
        )
    else:
        st.dataframe(
            vehiculos_encontrados[
                ["model", "model_year", "price", "odometer", "condition", "type"]
            ].head(20),
            use_container_width=True
        )

import streamlit as st
import pandas as pd 

#configuracion de la aplicacion 
st.set_page_config(
    page_title="Monitoreo de ventas",
    page_icon="📊",
    layout="wide"
)

st.title("📊sistema de monitoreo de ventas")
st.write("administracion y analisis de informacion comercial")

#Datos de ejemplo 
datos = {
    "producto": [
        "laptop","mouse","teclado",
        "monitor","laptop","mouse",
        "monitor","teclado"
    ],
    "cantidad":[2,10,5,3,1,8,4,6],
    "precio":[12000,150,350,2800,1200,150,2800,350]
}

df = pd.DataFrame(datos)

# Calcular ingresos 
df["total"] = df["cantidad"] * df["precio"]

# Administracion de datos 
st.header("1.Administrcion de datos")

df = st.data_editor(
    df,
    num_rows="dynamic",
    use_container_width=True
)

# Actualizar calculos 
df["cantidad"] = pd.to_numeric(
    df["cantidad"],errors="coerce"
).fillna(0)

df["precio"] = pd.to_numeric(
    df["precio"],errors="coerce"
).fillna(0)

df["total"] = df["cantidad"] * df["precio"]

#Indicadores 
st.header("2.Indicadores de venta")

col1,col2,col3 = st.columns(3)

col1.metric("productos registrados", len(df))
col2.metric("unidades vendidas", int(df["cantidad"].sum()))
col3.metric("ingresos totales", f"${df['total'].sum():,.2f}")

# Reporte grafico
st.header("3. Reporte grafico")

ventas = df.groupby("producto")["total"].sum()

st.subheader("ingresos por producto")
st.bar_chart(ventas)

unidades = df.groupby("producto")["cantidad"].sum()

st.subheader("cantidad de productos vendidos")
st.dataframe(df, use_container_width = True)

#Tabla de resultados 
st.header("4.Reporte de resultados")
st.dataframe(df, use_container_width=True)

# Descargar reporte
csv = df.to_csv(index=False).encode("utf-8-sig")

st.download_button(
    label="Descargar reporte csv",
    data=csv,
    file_name="reporte_ventas.csv",
    mime="text/csv"
)


import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Colbún Digital - Maestro Solution", layout="wide")

# Estilo personalizado con CSS
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #007bff; color: white; }
    .card { background-color: white; padding: 20px; border-radius: 15px; shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# 1. BASE DE DATOS (Simulando la conexión con el Municipio)
data = {
    "Lugar": ["Lago Machicura", "Termas de Panimávida", "Artesanía en Rari", "Parque Tricahue", "Reserva Los Bellotos"],
    "Categoría": ["Naturaleza/Balneario", "Salud/Termal", "Cultura/Artesanía", "Ecoturismo", "Cordillera"],
    "Costo Adulto": [3500, 45000, 0, 5000, 0],
    "Beneficios": ["Playa pública, Kayak, Picnic", "Hidromasaje, Historia, Relax", "Taller en vivo, Souvenirs únicos", "Avistamiento loros, Senderos", "Bosque nativo, Fotografía"],
    "Estado": ["Abierto", "Abierto", "Abierto", "Solo con Reserva", "Abierto con Precaución"]
}

df = pd.DataFrame(data)

# 2. ENCABEZADO
st.title("🏔️ Colbún Digital")
st.caption("Impulsado por **Maestro Solution** | Conectando el turismo con la comunidad")

# 3. FILTROS LATERALES
st.sidebar.header("Panel de Búsqueda")
categoria_select = st.sidebar.multiselect("Filtrar por categoría", df["Categoría"].unique(), default=df["Categoría"].unique())
presupuesto = st.sidebar.slider("Tu presupuesto máximo (CLP)", 0, 50000, 50000)

# Filtrado de datos
df_filtrado = df[(df["Categoría"].isin(categoria_select)) & (df["Costo Adulto"] <= presupuesto)]

# 4. CUERPO DE LA APP
st.subheader("Lugares disponibles según tu perfil")

# Mostrar tarjetas
cols = st.columns(2)
for index, row in df_filtrado.iterrows():
    with cols[index % 2]:
        with st.expander(f"📍 {row['Lugar']}", expanded=True):
            st.write(f"**Categoría:** {row['Categoría']}")
            st.write(f"**Costo:** ${row['Costo Adulto']:,} CLP" if row['Costo Adulto'] > 0 else "**Costo:** Gratuito")
            st.write(f"**Beneficios:** {row['Beneficios']}")
            
            # Etiqueta de estado dinámica
            if row['Estado'] == "Abierto":
                st.success(f"Estado: {row['Estado']}")
            else:
                st.warning(f"Estado: {row['Estado']}")
            
            if st.button(f"Ver Mapa de {row['Lugar']}", key=row['Lugar']):
                st.info("Redirigiendo a coordenadas GPS...")

# 5. SECCIÓN DE BENEFICIOS MUNICIPALES
st.divider()
st.subheader("🎁 Beneficios Maestro Solution & Municipio")
st.write("Muestra tu app en locales adheridos para obtener descuentos.")
col_b1, col_b2 = st.columns(2)
col_b1.metric("Descuento Rari", "10%", "En artesanía")
col_b2.metric("Descuento Termas", "15%", "Convenio Vecino")

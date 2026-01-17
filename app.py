import streamlit as st

# Configuración de la App
st.set_page_config(page_title="Colbún Digital", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background-color: #f8fafc; }
    
    /* Contenedores */
    .section-container {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 30px;
        border: 1px solid #e2e8f0;
    }
    .titulo-oscuro { color: #1e3a8a; font-weight: bold; font-size: 1.6rem; margin-bottom: 10px; }
    .texto-oscuro { color: #334155; font-size: 1rem; }

    /* Estilo de Tarjetas de Lugares */
    .card {
        background-color: white;
        border-radius: 15px;
        padding: 15px;
        border: 1px solid #cbd5e1;
        margin-top: 15px;
    }
    .card-title { font-size: 1.2rem; font-weight: bold; color: #0f172a; }
    .price-badge {
        background-color: #059669;
        color: white;
        padding: 2px 10px;
        border-radius: 10px;
        float: right;
        font-size: 0.8rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. ENCABEZADO
st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>COLBÚN DIGITAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-weight: bold;'>MAESTRO SOLUTION TECH</p>", unsafe_allow_html=True)

# 2. RESEÑA DE LA COMUNA
st.markdown("""
<div class="section-container">
    <div class="titulo-oscuro">Explora lo Auténtico</div>
    <div class="texto-oscuro">
        Colbún te espera con la calidez de su gente y la belleza de sus paisajes. 
        Descubre la artesanía única de Rari, saborea la gastronomía local y relájate en nuestras termas históricas.
    </div>
</div>
""", unsafe_allow_html=True)

# 3. BUSCADOR Y LISTADO (Simplificado para el ejemplo)
lugares = [
    {"nombre": "Artesanía en Crin Rari", "cat": "Artesanía", "precio": "Gratis", "url": "https://www.google.com/maps/search/Artesanía+Rari+Colbun"},
    {"nombre": "Mercado de Colbún", "cat": "Local", "precio": "Libre", "url": "https://www.google.com/maps/search/Mercado+Colbun"},
    {"nombre": "Termas Panimávida", "cat": "Turismo", "precio": "$45.000", "url": "https://www.google.com/maps/search/Termas+de+Panimavida"}
]

search = st.text_input("🔍 ¿Qué buscas hoy?", placeholder="Ej: Artesanía, Comida...")

for l in lugares:
    if search.lower() in l["nombre"].lower() or search.lower() in l["cat"].lower():
        st.markdown(f"""
            <div class="card">
                <span class="price-badge">{l['precio']}</span>
                <div style="color: #64748b; font-size: 0.7rem; font-weight: bold;">{l['cat'].upper()}</div>
                <div class="card-title">{l['nombre']}</div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button(f"📍 Cómo llegar", l["url"], use_container_width=True)

# 4. FORMULARIO DE CONTACTO (SECCIÓN NUEVA)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div class="section-container" style="border-left: 5px solid #10b981;">
    <div class="titulo-oscuro" style="color: #065f46;">📬 Contacto y Colaboración</div>
    <p class="texto-oscuro">¿Eres dueño de un local o artesano y quieres aparecer aquí? ¿Tienes alguna duda? ¡Escríbenos!</p>
</div>
""", unsafe_allow_html=True)

with st.form("contacto_form"):
    nombre = st.text_input("Nombre Completo")
    email = st.text_input("Correo Electrónico")
    tipo = st.selectbox("Asunto", ["Quiero registrar mi local", "Consulta turística", "Soporte Técnico", "Otro"])
    mensaje = st.text_area("Tu Mensaje")
    
    submit = st.form_submit_button("Enviar Solicitud")
    
    if submit:
        if nombre and email and mensaje:
            st.success(f"¡Gracias {nombre}! Tu solicitud ha sido enviada con éxito a Maestro Solution.")
            # Aquí se podría integrar un envío de mail real
        else:
            st.error("Por favor, completa los campos obligatorios.")

# 5. PIE DE PÁGINA
st.divider()
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.8rem;'>© 2026 Maestro Solution - Innovación para el Maule</p>", unsafe_allow_html=True)

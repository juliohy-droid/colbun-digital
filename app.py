import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Guía Colbún Digital", layout="centered")

# 2. CSS DE ALTO IMPACTO (Foco en fotos y legibilidad)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background-color: #fcfcfc; }
    
    /* Encabezado */
    .header-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
        padding: 40px 20px;
        border-radius: 0 0 30px 30px;
        margin: -60px -20px 30px -20px;
        text-align: center;
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    }

    /* Fila de Iconos */
    .icon-row {
        display: flex;
        justify-content: space-around;
        background: white;
        padding: 15px;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .icon-item { text-align: center; font-size: 0.75rem; color: #1e3a8a; font-weight: bold; }
    .icon-emoji { font-size: 1.5rem; display: block; margin-bottom: 5px; }

    /* Tarjetas con Imágenes Grandes */
    .card {
        background-color: white;
        border-radius: 25px;
        overflow: hidden;
        margin-bottom: 30px;
        box-shadow: 0 12px 24px rgba(0,0,0,0.1);
        border: 1px solid #edf2f7;
    }
    .card-img { width: 100%; height: 260px; object-fit: cover; }
    .card-content { padding: 25px; }
    .card-title { font-size: 1.7rem; font-weight: 800; color: #1a202c; margin-bottom: 8px; }
    .badge {
        background-color: #ebf8ff; color: #2b6cb0;
        padding: 5px 14px; border-radius: 12px;
        font-size: 0.8rem; font-weight: 700; text-transform: uppercase;
    }

    /* VENTANA DE REGISTRO (Diseño Destacado) */
    .register-box {
        background-color: #065f46;
        color: white;
        padding: 30px;
        border-radius: 25px;
        margin-top: 40px;
        text-align: center;
        box-shadow: 0 10px 20px rgba(6, 95, 70, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ENCABEZADO
st.markdown("""
<div class="header-container">
    <h1 style='color: white; margin: 0; font-size: 2.3rem;'>🏔️ Guía Colbún Digital</h1>
    <p style='color: #dbeafe; font-weight: 500; font-size: 1rem;'>Plataforma Turística de la Comuna de Colbún</p>
</div>
""", unsafe_allow_html=True)

# 4. ICONOS EN FILA
st.markdown("""
<div class="icon-row">
    <div class="icon-item"><span class="icon-emoji">🏊</span>Balneario</div>
    <div class="icon-item"><span class="icon-emoji">🏨</span>Hoteles</div>
    <div class="icon-item"><span class="icon-emoji">🍴</span>Restorán</div>
    <div class="icon-item"><span class="icon-emoji">🧶</span>Artesanía</div>
    <div class="icon-item"><span class="icon-emoji">⛺</span>Camping</div>
</div>
""", unsafe_allow_html=True)

# 5. BASE DE DATOS ACTUALIZADA (Balneario, Hoteles, Locales)
lugares = [
    {
        "nombre": "Balneario Machicura",
        "cat": "Balneario Inclusivo",
        "desc": "Playa pública de aguas cristalinas. Cuenta con accesibilidad universal, zonas de picnic y deportes náuticos.",
        "foto": "https://portalcolbun.cl/wp-content/uploads/2021/12/machicura-playa.jpg",
        "maps": "https://www.google.com/maps/search/?api=1&query=Balneario+Machicura+Colbun"
    },
    {
        "nombre": "Termas de Panimávida",
        "cat": "Hotel & Salud",
        "desc": "Referente nacional en turismo termal. Salud, historia y relajo en un solo lugar.",
        "foto": "https://p-u.popcdn.net/attachments/images/000/013/376/large/panimavida.jpg",
        "maps": "https://www.google.com/maps/search/?api=1&query=Termas+de+Panimavida"
    },
    {
        "nombre": "Artesanía en Crin Rari",
        "cat": "Artesanía y Cultura",
        "desc": "Única artesanía en el mundo tejida con pelo de caballo. Tesoro Humano Vivo de la zona.",
        "foto": "https://www.artesaniasdechile.cl/wp-content/uploads/2016/11/crin-rari.jpg",
        "maps": "https://www.google.com/maps/search/?api=1&query=Artesania+Crin+Rari"
    },
    {
        "nombre": "Borde Lago Restaurante",
        "cat": "Restorán y Eventos",
        "desc": "Disfruta de la mejor gastronomía con una vista privilegiada al Lago Colbún.",
        "foto": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800",
        "maps": "https://www.google.com/maps/search/?api=1&query=Borde+Lago+Restaurante+Colbun"
    }
]

# 6. BUSCADOR
search = st.text_input("", placeholder="🔍 ¿Buscas playa, comida, artesanía o descanso?")

# 7. LISTADO DE LUGARES CON FOTOS
for l in lugares:
    if search.lower() in l["nombre"].lower() or search.lower() in l["cat"].lower():
        st.markdown(f"""
            <div class="card">
                <img src="{l['foto']}" class="card-img">
                <div class="card-content">
                    <span class="badge">{l['cat']}</span>
                    <div class="card-title">{l['nombre']}</div>
                    <p style='color: #4a5568; font-size: 1rem; line-height: 1.6;'>{l['desc']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button(f"📍 Cómo llegar a {l['nombre']}", l["maps"], use_container_width=True)
        st.write("")

# 8. VENTANA DE REGISTRO DESTACADA (Nuevos Clientes)
st.markdown("""
<div class="register-box">
    <h2 style='color: white; margin: 0;'>🚀 ¿Quieres aparecer en esta App?</h2>
    <p style='color: #d1fae5; font-size: 1.1rem; margin: 15px 0;'>
        Si eres dueño de un hotel, restorán, camping o artesano, 
        únete a la red digital de <b>Maestro Solution</b>.
    </p>
</div>
""", unsafe_allow_html=True)

with st.form("registro_maestro"):
    st.write("### Completa tus datos")
    nombre_local = st.text_input("Nombre de tu Negocio")
    rubro = st.selectbox("Categoría", ["Restorán", "Hotel", "Artesanía", "Camping", "Tour Operador"])
    whatsapp = st.text_input("WhatsApp (ej: +569...)")
    detalles = st.text_area("Cuéntanos brevemente qué ofreces")
    
    if st.form_submit_button("Solicitar Inscripción Gratis"):
        st.success(f"¡Excelente! El equipo de Maestro Solution contactará a {nombre_local} a la brevedad.")
        st.balloons()

# 9. PIE DE PÁGINA
st.markdown("<p style='text-align: center; color: #94a3b8; padding: 30px;'>© 2026 Maestro Solution - Innovación en Colbún</p>", unsafe_allow_html=True)

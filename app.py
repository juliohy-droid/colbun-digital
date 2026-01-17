import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Guía Colbún Digital", layout="centered")

# 2. CSS AVANZADO (Color, Tarjetas e Iconos en Fila)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background-color: #f0f4f8; }
    
    /* Encabezado con Color */
    .header-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 40px 20px;
        border-radius: 0 0 30px 30px;
        margin: -60px -20px 30px -20px;
        text-align: center;
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    }

    /* Fila de Iconos Horizontal en Móvil */
    .icon-row {
        display: flex;
        justify-content: space-around;
        background: white;
        padding: 15px;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .icon-item { text-align: center; font-size: 0.75rem; color: #1e3a8a; font-weight: bold; }
    .icon-emoji { font-size: 1.4rem; display: block; }

    /* Tarjetas con Fotos Reales */
    .card {
        background-color: white;
        border-radius: 25px;
        overflow: hidden;
        margin-bottom: 25px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.08);
        border: 1px solid #e2e8f0;
    }
    .card-img { width: 100%; height: 220px; object-fit: cover; }
    .card-content { padding: 20px; }
    .card-title { font-size: 1.5rem; font-weight: bold; color: #1e293b; }
    .badge {
        background-color: #dbeafe; color: #1e40af;
        padding: 4px 12px; border-radius: 10px;
        font-size: 0.7rem; font-weight: 700; text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ENCABEZADO
st.markdown("""
<div class="header-container">
    <h1 style='color: white; margin: 0; font-size: 2.2rem;'>🏔️ Guía Colbún Digital</h1>
    <p style='color: #bfdbfe; font-weight: 500;'>Plataforma Turística de la Comuna de Colbún</p>
</div>
""", unsafe_allow_html=True)

# 4. ICONOS EN FILA (Fuerza horizontal en móvil)
st.markdown("""
<div class="icon-row">
    <div class="icon-item"><span class="icon-emoji">🍴</span>Restorán</div>
    <div class="icon-item"><span class="icon-emoji">🏨</span>Hoteles</div>
    <div class="icon-item"><span class="icon-emoji">🧶</span>Artesanía</div>
    <div class="icon-item"><span class="icon-emoji">⛺</span>Camping</div>
    <div class="icon-item"><span class="icon-emoji">🧗</span>Tours</div>
</div>
""", unsafe_allow_html=True)

# 5. BASE DE DATOS AMPLIADA (Locales Reales)
lugares = [
    {
        "nombre": "Termas de Panimávida",
        "cat": "Hotel & Salud",
        "desc": "Aguas medicinales históricas y relajo total.",
        "foto": "https://p-u.popcdn.net/attachments/images/000/013/376/large/panimavida.jpg",
        "maps": "https://www.google.com/maps/search/Termas+de+Panimavida"
    },
    {
        "nombre": "Artesanía en Crin Rari",
        "cat": "Artesanía",
        "desc": "Conoce a las tejedoras de tesoros humanos vivos.",
        "foto": "https://www.artesaniasdechile.cl/wp-content/uploads/2016/11/crin-rari.jpg",
        "maps": "https://www.google.com/maps/search/Artesania+Rari"
    },
    {
        "nombre": "Lodge Borde Lago",
        "cat": "Restorán & Aventura",
        "desc": "Excelente gastronomía con la mejor vista al Embalse Colbún.",
        "foto": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800",
        "maps": "https://www.google.com/maps/search/Borde+Lago+Colbun"
    },
    {
        "nombre": "Camping Los Bellotos",
        "cat": "Camping",
        "desc": "Naturaleza pura en el Cajón del Melado.",
        "foto": "https://images.unsplash.com/photo-1478131143081-80f7f84ca84d?w=800",
        "maps": "https://www.google.com/maps/search/Reserva+Los+Bellotos"
    }
]

# 6. BUSCADOR
search = st.text_input("", placeholder="🔍 ¿Qué buscas hoy en Colbún?")

# 7. DESPLIEGUE DE TARJETAS
for l in lugares:
    if search.lower() in l["nombre"].lower() or search.lower() in l["cat"].lower():
        st.markdown(f"""
            <div class="card">
                <img src="{l['foto']}" class="card-img">
                <div class="card-content">
                    <span class="badge">{l['cat']}</span>
                    <div class="card-title">{l['nombre']}</div>
                    <p style='color: #475569; font-size: 0.9rem;'>{l['desc']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button(f"📍 Ir a {l['nombre']}", l["maps"], use_container_width=True)
        st.write("")

# 8. FORMULARIO PARA NUEVOS CLIENTES (Maestro Solution)
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #1e3a8a;'>📩 ¿Quieres que tu local aparezca aquí?</h2>", unsafe_allow_html=True)
st.info("Forma parte de la red digital de Maestro Solution y llega a miles de turistas.")

with st.form("contacto_cliente"):
    nombre_local = st.text_input("Nombre del Local/Negocio")
    rubro = st.selectbox("Rubro", ["Restorán", "Hotel", "Camping", "Artesanía", "Otros"])
    whatsapp = st.text_input("WhatsApp de contacto")
    if st.form_submit_button("Solicitar Registro"):
        st.success(f"¡Gracias! Maestro Solution se contactará con {nombre_local} pronto.")
        st.balloons()

st.markdown("<p style='text-align: center; color: #94a3b8; padding: 20px;'>© 2026 Maestro Solution</p>", unsafe_allow_html=True)

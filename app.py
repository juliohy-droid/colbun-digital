import streamlit as st

# Configuración de la App con estilo móvil moderno
st.set_page_config(page_title="Colbún Digital", layout="centered")

# CSS Avanzado para Interfaz Atractiva
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background-color: #f0f4f8; }
    
    /* Encabezado con degradado */
    .header-box {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 40px 20px;
        border-radius: 0 0 30px 30px;
        margin: -60px -20px 30px -20px;
        text-align: center;
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    }

    /* Tarjetas Estilo Instagram / TripAdvisor */
    .card {
        background-color: white;
        border-radius: 25px;
        overflow: hidden;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border: 1px solid #e2e8f0;
    }
    .card-img-container {
        position: relative;
        width: 100%;
        height: 250px;
    }
    .card-img-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .badge-cat {
        position: absolute;
        top: 15px;
        left: 15px;
        background: rgba(255,255,255,0.9);
        color: #1e3a8a;
        padding: 5px 12px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: bold;
        text-transform: uppercase;
    }
    .card-info { padding: 20px; }
    .card-title { font-size: 1.6rem; font-weight: 800; color: #1e293b; margin-bottom: 5px; }
    .card-price { color: #059669; font-weight: 700; font-size: 1.1rem; }
    .card-text { color: #475569; font-size: 0.95rem; line-height: 1.5; margin: 10px 0; }
    
    /* Formulario Estilizado */
    .form-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #e2e8f0;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. ENCABEZADO IMPACTANTE
st.markdown("""
<div class="header-box">
    <h1 style='color: white; margin: 0; font-size: 2.5rem;'>COLBÚN DIGITAL</h1>
    <p style='color: #bfdbfe; font-weight: 600; letter-spacing: 2px;'>MAESTRO SOLUTION TECH</p>
</div>
""", unsafe_allow_html=True)

# 2. RESEÑA DE BIENVENIDA (Legible y Elegante)
st.markdown("""
<div style="background: white; padding: 25px; border-radius: 20px; margin-bottom: 30px; border-left: 8px solid #3b82f6;">
    <h2 style="color: #1e3a8a; margin-top: 0;">El Corazón del Maule</h2>
    <p style="color: #334155; font-size: 1.1rem; line-height: 1.6;">
        Bienvenidos a la guía definitiva de <b>Colbún</b>. Un territorio de contrastes donde la calma de las termas 
        se encuentra con la aventura de los lagos y la herencia viva de nuestra artesanía local.
    </p>
</div>
""", unsafe_allow_html=True)

# 3. BASE DE DATOS COMPLETA (Lugares Reales con Fotos)
lugares = [
    {
        "nombre": "Termas de Panimávida",
        "cat": "Hotel & Spa",
        "desc": "Relájate en aguas mineromedicinales en un hotel con más de 100 años de historia.",
        "precio": "Desde $45.000",
        "img": "https://images.unsplash.com/photo-1544161515-4ae6ce6ca606?w=800",
        "maps": "https://maps.google.com/?cid=12368284243410402569&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ"
    },
    {
        "nombre": "Artesanía en Crin Rari",
        "cat": "Artesanía Local",
        "desc": "Visita los talleres de las únicas artesanas en el mundo que tejen pelo de caballo.",
        "precio": "Entrada Gratuita",
        "img": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=800",
        "maps": "https://maps.google.com/?cid=317387301014535064&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ"
    },
    {
        "nombre": "Balneario Machicura",
        "cat": "Balneario & Playa",
        "desc": "Playa inclusiva con aguas tranquilas, kayak y excelentes zonas de recreación.",
        "precio": "$3.500",
        "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800",
        "maps": "https://maps.google.com/?cid=695509618017172482&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ"
    },
    {
        "nombre": "Camping Los Bellotos",
        "cat": "Camping & Naturaleza",
        "desc": "Acampa bajo las estrellas rodeado de bosque nativo en el Cajón del Melado.",
        "precio": "$10.000 p/p",
        "img": "https://images.unsplash.com/photo-1478131143081-80f7f84ca84d?w=800",
        "maps": "https://maps.google.com/?cid=15489324013524022592&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ"
    },
    {
        "nombre": "Restaurante Raíces Maulinis",
        "cat": "Restaurantes",
        "desc": "Prueba el mejor pastel de choclo y empanadas tradicionales de la zona.",
        "precio": "$12.000 promedio",
        "img": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800",
        "maps": "https://www.google.com/maps/search/?api=1&query=Reserva+Nacional+Los+Bellotos"
    }
]

# 4. BUSCADOR DINÁMICO
search = st.text_input("", placeholder="🔍 Busca camping, hoteles, comida o artesanía...")

# 5. RENDERIZADO DE TARJETAS
for l in lugares:
    if search.lower() in l["nombre"].lower() or search.lower() in l["cat"].lower():
        st.markdown(f"""
            <div class="card">
                <div class="card-img-container">
                    <img src="{l['img']}">
                    <div class="badge-cat">{l['cat']}</div>
                </div>
                <div class="card-info">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div class="card-title">{l['nombre']}</div>
                        <div class="card-price">{l['precio']}</div>
                    </div>
                    <p class="card-text">{l['desc']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        # Botón funcional de Google Maps
        st.link_button(f"📍 Cómo llegar a {l['nombre']}", l["maps"], use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

# 6. FORMULARIO DE CONTACTO PROFESIONAL
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #1e3a8a; text-align: center;'>📬 ¿Quieres aparecer en la App?</h2>", unsafe_allow_html=True)
st.write("Si eres dueño de un hotel, camping o local, escríbenos para integrarte a la red de Maestro Solution.")

with st.form("form_contacto"):
    col_a, col_b = st.columns(2)
    with col_a:
        nombre = st.text_input("Nombre del Negocio")
        categoria = st.selectbox("Categoría", ["Hotel", "Restaurante", "Artesanía", "Camping", "Otro"])
    with col_b:
        contacto = st.text_input("WhatsApp o Correo")
        ubicacion = st.text_input("Ubicación (Calle/Sector)")
    
    mensaje = st.text_area("Cuéntanos brevemente sobre tu servicio")
    
    enviar = st.form_submit_button("Enviar Solicitud de Registro")
    if enviar:
        st.success("¡Solicitud recibida! El equipo de Maestro Solution te contactará pronto.")
        st.balloons()

# 7. PIE DE PÁGINA
st.markdown("""
<div style="text-align: center; padding: 40px; color: #94a3b8;">
    <p>Desarrollado con ❤️ para Colbún por <b>Maestro Solution Tech</b></p>
    <small>2026 © Todos los derechos reservados</small>
</div>
""", unsafe_allow_html=True)

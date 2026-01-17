import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Guía Colbún Digital",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. DISEÑO VISUAL (CSS) - ENFOQUE EN LEGIBILIDAD Y ATRACTIVO
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background-color: #f8fafc; }
    
    /* Encabezado Principal */
    .header-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 40px 20px;
        border-radius: 0 0 25px 25px;
        margin: -60px -20px 40px -20px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Reseña Comunal */
    .resena-box {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        border-left: 6px solid #1e3a8a;
        margin-bottom: 30px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }

    /* Tarjetas de Atractivos */
    .card {
        background-color: white;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 35px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .card-img {
        width: 100%;
        height: 250px;
        object-fit: cover;
    }
    .card-body { padding: 20px; }
    .category-badge {
        background-color: #dbeafe;
        color: #1e40af;
        padding: 4px 12px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
    }
    .card-title { font-size: 1.6rem; font-weight: bold; color: #1e293b; margin-top: 10px; }
    .card-price { color: #059669; font-weight: 700; font-size: 1.1rem; float: right; }
    .card-text { color: #475569; font-size: 1rem; line-height: 1.5; margin: 15px 0; }
    
    /* Formulario */
    .form-box {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #cbd5e1;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ENCABEZADO ACTUALIZADO
st.markdown("""
<div class="header-container">
    <h1 style='color: white; margin: 0; font-size: 2.2rem;'>🏔️ Guía Colbún Digital</h1>
    <p style='color: #bfdbfe; font-weight: 500;'>Plataforma Turística de la Comuna de Colbún</p>
</div>
""", unsafe_allow_html=True)

# 4. RESEÑA DE LA COMUNA
st.markdown("""
<div class="resena-box">
    <h3 style="color: #1e3a8a; margin-top: 0;">Corazón de la Región del Maule</h3>
    <p style="color: #334155; line-height: 1.6;">
        <b>Colbún</b> es un territorio donde el agua y la tierra cuentan historias. Desde la majestuosidad de sus embalses 
        hasta el susurro de la precordillera, nuestra comuna invita al descanso termal, la aventura al aire libre y 
        el encuentro con tradiciones artesanales únicas en el mundo como el Crin de Rari.
    </p>
</div>
""", unsafe_allow_html=True)

# 5. BASE DE DATOS AMPLIADA (Lugares, Locales, Restaurantes, Campings)
lugares = [
    {
        "nombre": "Termas de Panimávida",
        "cat": "Hotel & Termal",
        "desc": "Hotel histórico con aguas mineromedicinales curativas. Experiencia de lujo y salud.",
        "precio": "$45.000+",
        "foto": "https://images.unsplash.com/photo-1544161515-4ae6ce6ca606?w=800",
        "maps": "https://www.google.com/maps/search/Termas+de+Panimavida"
    },
    {
        "nombre": "Artesanía en Crin (Rari)",
        "cat": "Artesanía & Cultura",
        "desc": "Conoce los talleres de las artesanas que tejen pelo de caballo a mano. Patrimonio Vivo.",
        "precio": "Entrada Libre",
        "foto": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=800",
        "maps": "https://www.google.com/maps/search/Rari+Colbun"
    },
    {
        "nombre": "Balneario Machicura",
        "cat": "Balneario & Playa",
        "desc": "Playa pública inclusiva con kayak, picnic y seguridad para toda la familia.",
        "precio": "$3.500",
        "foto": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800",
        "maps": "https://www.google.com/maps/search/Playa+Machicura"
    },
    {
        "nombre": "Restaurante Raíces Maulinis",
        "cat": "Restaurantes",
        "desc": "Gastronomía típica: Pastel de choclo, humitas y vinos del Valle del Maule.",
        "precio": "$12.000 prom.",
        "foto": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800",
        "maps": "https://www.google.com/maps/search/Restaurantes+en+Colbun"
    },
    {
        "nombre": "Camping Los Bellotos",
        "cat": "Camping & Aventura",
        "desc": "Acampada en la Reserva Nacional Los Bellotos del Melado. Naturaleza pura.",
        "precio": "$10.000 p/p",
        "foto": "https://images.unsplash.com/photo-1478131143081-80f7f84ca84d?w=800",
        "maps": "https://www.google.com/maps/search/Reserva+Los+Bellotos+Colbun"
    },
    {
        "nombre": "Termas de Quinamávida",
        "cat": "Hotel & Termal",
        "desc": "Piscinas termales y baños de barro tradicionales. Un lugar para el descanso familiar.",
        "precio": "$35.000+",
        "foto": "https://images.unsplash.com/photo-1584132967334-10e028bd69f7?w=800",
        "maps": "https://maps.app.goo.gl/9h2XG7yV6qG2"
    }
]

# 6. BUSCADOR DINÁMICO
search = st.text_input("", placeholder="🔍 ¿Qué buscas hoy? (Hotel, Camping, Comida...)")

# 7. RENDERIZADO DE ATRACTIVOS
for l in lugares:
    if search.lower() in l["nombre"].lower() or search.lower() in l["cat"].lower():
        st.markdown(f"""
            <div class="card">
                <img src="{l['foto']}" class="card-img">
                <div class="card-body">
                    <span class="price-badge">{l['precio']}</span>
                    <span class="category-badge">{l['cat']}</span>
                    <div class="card-title">{l['nombre']}</div>
                    <p class="card-text">{l['desc']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button(f"📍 Ir a {l['nombre']}", l["maps"], use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

# 8. FORMULARIO DE CONTACTO
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #1e3a8a;'>📩 Registro de Locales</h2>", unsafe_allow_html=True)
st.write("Si eres dueño de un restaurante, hotel o artesano, completa este formulario para aparecer en la App.")

with st.form("registro_negocio"):
    col1, col2 = st.columns(2)
    with col1:
        nombre_negocio = st.text_input("Nombre del Local/Negocio")
        rubro = st.selectbox("Rubro", ["Hotel", "Camping", "Restaurante", "Artesanía", "Transporte"])
    with col2:
        encargado = st.text_input("Nombre de contacto")
        whatsapp = st.text_input("WhatsApp de contacto")
    
    detalles = st.text_area("Cuéntanos sobre tu local (servicios, precios, ubicación)")
    
    enviar = st.form_submit_button("Enviar para Validación")
    if enviar:
        st.success("¡Excelente! El equipo de Maestro Solution revisará los datos para publicarlos.")
        st.balloons()

# 9. PIE DE PÁGINA
st.markdown("""
<div style="text-align: center; color: #94a3b8; padding: 40px;">
    <p>Desarrollado con ❤️ por <b>Maestro Solution</b></p>
    <small>© 2026 Colbún, Provincia de Linares</small>
</div>
""", unsafe_allow_html=True)

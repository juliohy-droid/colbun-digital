import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Guía Colbún Digital",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. DISEÑO VISUAL (CSS)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background-color: #f8fafc; }
    
    .header-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 40px 20px;
        border-radius: 0 0 25px 25px;
        margin: -60px -20px 40px -20px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Iconos de Categoría */
    .icon-bar {
        display: flex;
        justify-content: space-around;
        margin-bottom: 30px;
        background: white;
        padding: 15px;
        border-radius: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    .icon-item { text-align: center; font-size: 0.8rem; color: #1e3a8a; font-weight: bold; }

    .card {
        background-color: white;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 35px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .card-img { width: 100%; height: 250px; object-fit: cover; }
    .card-body { padding: 20px; }
    
    .category-badge {
        background-color: #dbeafe;
        color: #1e40af;
        padding: 4px 12px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 700;
        display: inline-flex;
        align-items: center;
        gap: 5px;
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

# 4. BARRA DE ICONOS DE CATEGORÍA
st.markdown("<br>", unsafe_allow_html=True)
col_cat1, col_cat2, col_cat3, col_cat4, col_cat5 = st.columns(5)
with col_cat1: st.markdown("<div class='icon-item'>🍴<br>Restorán</div>", unsafe_allow_html=True)
with col_cat2: st.markdown("<div class='icon-item'>🚵<br>Aventura</div>", unsafe_allow_html=True)
with col_cat3: st.markdown("<div class='icon-item'>🏨<br>Hotel</div>", unsafe_allow_html=True)
with col_cat4: st.markdown("<div class='icon-item'>🧶<br>Artesanía</div>", unsafe_allow_html=True)
with col_cat5: st.markdown("<div class='icon-item'>⛺<br>Camping</div>", unsafe_allow_html=True)

# 5. BASE DE DATOS AMPLIADA
# He añadido el campo "icono" para cada lugar
lugares = [
    {
        "nombre": "Termas de Panimávida",
        "cat": "Hotel & Termal",
        "icono": "🏨",
        "desc": "Hotel histórico con aguas mineromedicinales. Experiencia de salud y relajo.",
        "precio": "$45.000+",
        "foto": "https://images.unsplash.com/photo-1544161515-4ae6ce6ca606?w=800",
        "maps": "https://maps.google.com/?q=Termas+de+Panimavida"
    },
    {
        "nombre": "Artesanía en Crin (Rari)",
        "cat": "Artesanía & Cultura",
        "icono": "🧶",
        "desc": "Micro-artesanía única en el mundo tejida con pelo de caballo. Tesoro Humano Vivo.",
        "precio": "Entrada Libre",
        "foto": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=800",
        "maps": "https://maps.google.com/?q=Artesania+Rari"
    },
    {
        "nombre": "Restaurante Sabores del Maule",
        "cat": "Restorán",
        "icono": "🍴",
        "desc": "Comida tradicional chilena, expertos en pastel de choclo y empanadas.",
        "precio": "$12.000 prom.",
        "foto": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800",
        "maps": "https://maps.google.com/?q=Restaurante+Colbun"
    },
    {
        "nombre": "Parque Natural Tricahue",
        "cat": "Aventura & Trekking",
        "icono": "🚵",
        "desc": "Senderos de bosque nativo y avistamiento del Loro Tricahue.",
        "precio": "$5.000",
        "foto": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800",
        "maps": "https://maps.google.com/?q=Parque+Tricahue"
    },
    {
        "nombre": "Camping Los Bellotos",
        "cat": "Camping",
        "icono": "⛺",
        "desc": "Camping cordillerano en la Reserva Nacional. Naturaleza en estado puro.",
        "precio": "$10.000 p/p",
        "foto": "https://images.unsplash.com/photo-1478131143081-80f7f84ca84d?w=800",
        "maps": "https://maps.google.com/?q=Reserva+Los+Bellotos"
    }
]

# 6. BUSCADOR
search = st.text_input("", placeholder="🔍 ¿Qué buscas hoy? (Restorán, Aventura, Hotel...)")

# 7. RENDERIZADO
for l in lugares:
    if search.lower() in l["nombre"].lower() or search.lower() in l["cat"].lower():
        st.markdown(f"""
            <div class="card">
                <img src="{l['foto']}" class="card-img">
                <div class="card-body">
                    <span style="color: #059669; font-weight: bold; float: right;">{l['precio']}</span>
                    <span class="category-badge">{l['icono']} {l['cat']}</span>
                    <div style="font-size: 1.5rem; font-weight: bold; color: #1e293b; margin-top: 10px;">{l['nombre']}</div>
                    <p style="color: #475569; font-size: 0.95rem; margin: 10px 0;">{l['desc']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button(f"📍 Ir a {l['nombre']}", l["maps"], use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

# 8. FORMULARIO DE REGISTRO
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #1e3a8a;'>📩 ¿Quieres aparecer aquí?</h3>", unsafe_allow_html=True)
with st.form("registro"):
    c1, c2 = st.columns(2)
    c1.text_input("Nombre Negocio")
    c2.selectbox("Categoría", ["Restorán", "Aventura", "Hotel", "Artesanía", "Camping"])
    st.text_area("Descripción de tu servicio")
    if st.form_submit_button("Enviar Solicitud"):
        st.success("¡Enviado! Maestro Solution procesará tu solicitud.")

st.markdown("<p style='text-align: center; color: #94a3b8; padding: 20px;'>© 2026 Maestro Solution</p>", unsafe_allow_html=True)

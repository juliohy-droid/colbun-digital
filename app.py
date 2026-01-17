import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Guía Colbún Digital",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. DISEÑO VISUAL (CSS) - FILA DE ICONOS HORIZONTAL Y CONTRASTE
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background-color: #f1f5f9; }
    
    /* Encabezado */
    .header-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 30px 20px;
        border-radius: 0 0 25px 25px;
        margin: -60px -20px 30px -20px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    
    /* FILA DE ICONOS HORIZONTAL (Fuerza la fila en el celular) */
    .icon-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: white;
        padding: 15px;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        overflow-x: auto; /* Permite scroll si hay muchos iconos */
    }
    .icon-item {
        flex: 1;
        text-align: center;
        font-size: 0.75rem;
        color: #1e3a8a;
        font-weight: bold;
        min-width: 60px;
    }
    .icon-emoji { font-size: 1.5rem; display: block; margin-bottom: 5px; }

    /* Tarjetas */
    .card {
        background-color: white;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 25px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .card-img { width: 100%; height: 200px; object-fit: cover; }
    .card-body { padding: 20px; }
    .category-badge {
        background-color: #dbeafe;
        color: #1e40af;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ENCABEZADO
st.markdown("""
<div class="header-container">
    <h1 style='color: white; margin: 0; font-size: 2rem;'>🏔️ Guía Colbún Digital</h1>
    <p style='color: #bfdbfe; font-size: 0.9rem;'>Plataforma Turística de la Comuna de Colbún</p>
</div>
""", unsafe_allow_html=True)

# 4. FILA DE ICONOS HORIZONTAL (Fija para móviles)
st.markdown("""
<div class="icon-row">
    <div class="icon-item"><span class="icon-emoji">🍴</span>Restorán</div>
    <div class="icon-item"><span class="icon-emoji">🚵</span>Aventura</div>
    <div class="icon-item"><span class="icon-emoji">🏨</span>Hotel</div>
    <div class="icon-item"><span class="icon-emoji">🧶</span>Artesanía</div>
    <div class="icon-item"><span class="icon-emoji">⛺</span>Camping</div>
</div>
""", unsafe_allow_html=True)

# 5. RESEÑA
st.markdown("""
<div style="background: white; padding: 20px; border-radius: 15px; border-left: 5px solid #1e3a8a; margin-bottom: 25px;">
    <h4 style="color: #1e3a8a; margin-top: 0;">Descubre lo mejor de Colbún</h4>
    <p style="color: #334155; font-size: 0.9rem; margin-bottom: 0;">
        Desde las históricas termas hasta la artesanía única de Rari. 
        Explora locales, restoranes y aventuras en el corazón del Maule.
    </p>
</div>
""", unsafe_allow_html=True)

# 6. BASE DE DATOS
lugares = [
    {
        "nombre": "Termas de Panimávida",
        "cat": "Hotel & Termal",
        "icono": "🏨",
        "desc": "Aguas medicinales y relajo total en un entorno histórico.",
        "precio": "$45.000+",
        "foto": "https://images.unsplash.com/photo-1544161515-4ae6ce6ca606?w=800",
        "maps": "https://maps.google.com/maps/contrib/104975540973083156828"
    },
    {
        "nombre": "Artesanía en Crin (Rari)",
        "cat": "Artesanía",
        "icono": "🧶",
        "desc": "Tejido manual único en el mundo con pelo de caballo.",
        "precio": "Entrada Libre",
        "foto": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=800",
        "maps": "https://maps.google.com/?cid=317387301014535064&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ3"
    },
    {
        "nombre": "Restaurante Raíces",
        "cat": "Restorán",
        "icono": "🍴",
        "desc": "Comida tradicional chilena con ingredientes locales.",
        "precio": "$12.000 prom.",
        "foto": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800",
        "maps": "https://www.google.com/maps/place//data=!3m4!1e2!3m2!1sAF1QipMUKMG_qDXi9DHQGlZMwckVT8U5vXsPpzTXugqF!2e10!4m2!3m1!1s0x966f908b3760fa23:0xbe10343903a3f861"
    }
]

# 7. BUSCADOR
search = st.text_input("", placeholder="🔍 Busca restorán, camping, artesanía...")

# 8. RENDERIZADO
for l in lugares:
    if search.lower() in l["nombre"].lower() or search.lower() in l["cat"].lower():
        st.markdown(f"""
            <div class="card">
                <img src="{l['foto']}" class="card-img">
                <div class="card-body">
                    <span style="color: #059669; font-weight: bold; float: right;">{l['precio']}</span>
                    <span class="category-badge">{l['icono']} {l['cat']}</span>
                    <div style="font-size: 1.4rem; font-weight: bold; color: #1e293b; margin-top: 10px;">{l['nombre']}</div>
                    <p style="color: #475569; font-size: 0.9rem; margin-top: 8px;">{l['desc']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button(f"📍 Ir a {l['nombre']}", l["maps"], use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

# 9. FORMULARIO DE CONTACTO
st.markdown("---")
with st.form("registro"):
    st.subheader("📩 ¿Quieres aparecer aquí?")
    st.text_input("Nombre del Local")
    st.selectbox("Categoría", ["Restorán", "Aventura", "Hotel", "Artesanía", "Camping"])
    if st.form_submit_button("Enviar Solicitud"):
        st.success("¡Solicitud enviada a Maestro Solution!")

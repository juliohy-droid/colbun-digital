import streamlit as st

# Configuración de página para que parezca una App
st.set_page_config(page_title="Colbún Digital", layout="centered", initial_sidebar_state="collapsed")

# CSS Avanzado para diseño atractivo y moderno
st.markdown("""
    <style>
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Fondo degradado estilo moderno */
    .stApp {
        background: linear-gradient(180deg, #1a73e8 0%, #f8f9fa 30%);
    }
    
    /* Contenedor de Tarjeta Estilo Premium */
    .card {
        background-color: white;
        border-radius: 25px;
        margin-bottom: 25px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        overflow: hidden;
        transition: transform 0.3s;
    }
    .card:hover { transform: scale(1.02); }
    
    .card-img {
        width: 100%;
        height: 200px;
        object-fit: cover;
    }
    
    .card-body { padding: 20px; }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1e3a8a;
        margin-bottom: 5px;
    }
    
    .price-badge {
        background-color: #34d399;
        color: white;
        padding: 5px 15px;
        border-radius: 50px;
        font-weight: bold;
        float: right;
    }
    
    .benefit-icon {
        background-color: #dbeafe;
        color: #1e40af;
        padding: 5px 12px;
        border-radius: 10px;
        font-size: 0.8rem;
        margin-right: 5px;
        display: inline-block;
        margin-top: 10px;
    }
    
    /* Título principal blanco */
    .main-title {
        color: white;
        text-align: center;
        font-family: 'Arial';
        padding-top: 20px;
        margin-bottom: 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado de la App
st.markdown("<h1 class='main-title'>COLBÚN DIGITAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: rgba(255,255,255,0.8);'>Desarrollado por Maestro Solution</p>", unsafe_allow_html=True)

# Datos con imágenes reales de alta disponibilidad
lugares = [
    {
        "nombre": "Lago Machicura",
        "desc": "Playa inclusiva perfecta para familias. Kayak y zonas de picnic.",
        "precio": "$3.500",
        "imagen": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "tags": ["Familiar", "Seguro"]
    },
    {
        "nombre": "Termas de Panimávida",
        "desc": "Aguas termales curativas en un entorno histórico y relajante.",
        "precio": "$45.000",
        "imagen": "https://images.unsplash.com/photo-1584132967334-10e028bd69f7?auto=format&fit=crop&w=800&q=80",
        "tags": ["Salud", "Relax"]
    },
    {
        "nombre": "Rari: Cuna del Crin",
        "desc": "Artesanía única en el mundo hecha a mano con pelo de caballo.",
        "precio": "Gratis",
        "imagen": "https://images.unsplash.com/photo-1459411552884-841db9b3cc2a?auto=format&fit=crop&w=800&q=80",
        "tags": ["Cultura", "Patrimonio"]
    }
]

# Buscador con diseño limpio
search = st.text_input("", placeholder="🔍 ¿Qué buscas hoy en Colbún?")

# Renderizado de la lista
for lug in lugares:
    if search.lower() in lug["nombre"].lower() or search.lower() in lug["desc"].lower():
        st.markdown(f"""
            <div class="card">
                <img src="{lug['imagen']}" class="card-img">
                <div class="card-body">
                    <span class="price-badge">{lug['precio']}</span>
                    <div class="card-title">{lug['nombre']}</div>
                    <p style='color: #4b5563;'>{lug['desc']}</p>
                    <div>
                        {' '.join([f'<span class="benefit-icon">{t}</span>' for t in lug['tags']])}
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Explorar {lug['nombre']}", key=lug['nombre']):
            st.balloons()
            st.info(f"Abriendo guía completa de {lug['nombre']}...")

# Barra de navegación estética al final
st.markdown("<br><p style='text-align: center; color: #9ca3af;'>🏠 Inicio | 📍 Mapa | 🎟️ Cupones</p>", unsafe_allow_html=True)

import streamlit as st

# Configuración de página estilo móvil
st.set_page_config(page_title="Colbún Digital", layout="centered")

# CSS Profesional con mejor contraste y más lugares
st.markdown("""
    <style>
    /* Ocultar elementos innecesarios */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Fondo con degradado azul oscuro para que resalte la marca */
    .stApp {
        background: linear-gradient(180deg, #0f172a 0%, #f8fafc 25%);
    }
    
    /* Título principal con sombra para legibilidad */
    .main-title {
        color: white;
        text-align: center;
        font-weight: 800;
        font-size: 2.2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 0;
        padding-top: 10px;
    }
    
    .sub-title {
        color: #94a3b8;
        text-align: center;
        font-size: 0.9rem;
        margin-bottom: 20px;
    }

    /* Tarjetas Premium */
    .card {
        background-color: white;
        border-radius: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        overflow: hidden;
        border: 1px solid #e2e8f0;
    }
    
    .card-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
    }
    
    .card-body { padding: 18px; }
    
    /* Texto dentro de tarjetas (Oscuro para legibilidad) */
    .card-name {
        font-size: 1.3rem;
        font-weight: bold;
        color: #1e293b;
        margin-bottom: 4px;
    }
    
    .card-desc {
        color: #475569;
        font-size: 0.9rem;
        line-height: 1.4;
        margin-bottom: 12px;
    }
    
    .price-badge {
        background-color: #10b981;
        color: white;
        padding: 4px 12px;
        border-radius: 99px;
        font-weight: bold;
        font-size: 0.85rem;
        float: right;
    }
    
    .tag {
        background-color: #f1f5f9;
        color: #334155;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 5px;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.markdown("<h1 class='main-title'>COLBÚN DIGITAL</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Desarrollado por Maestro Solution</p>", unsafe_allow_html=True)

# Buscador
search = st.text_input("", placeholder="🔍 Buscar termas, parques, lagos...")

# Base de datos ampliada de Colbún
lugares = [
    {
        "nombre": "Lago Machicura",
        "desc": "Playa inclusiva con excelentes instalaciones. Ideal para kayak y natación segura.",
        "precio": "$3.500",
        "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=500&q=80",
        "tags": ["Familiar", "Playa"]
    },
    {
        "nombre": "Termas de Panimávida",
        "desc": "Tradición y relax en el corazón de Colbún. Famosas por sus aguas mineromedicinales.",
        "precio": "$45.000",
        "img": "https://images.unsplash.com/photo-1544161515-4ae6ce6ca606?w=500&q=80",
        "tags": ["Salud", "Spa"]
    },
    {
        "nombre": "Reserva Los Bellotos",
        "desc": "Naturaleza pura en el Cajón del Melado. Protege el escaso Belloto del Sur.",
        "precio": "Gratis",
        "img": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500&q=80",
        "tags": ["Trekking", "Nativo"]
    },
    {
        "nombre": "Artesanía de Rari",
        "desc": "Conoce a las maestras del crin de caballo. Patrimonio cultural único en el mundo.",
        "precio": "Gratis",
        "img": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=500&q=80",
        "tags": ["Cultura", "Artesanía"]
    },
    {
        "nombre": "Parque Natural Tricahue",
        "desc": "Bosque nativo y avistamiento de Loros Tricahue. Ideal para ecoturismo.",
        "precio": "$5.000",
        "img": "https://images.unsplash.com/photo-1473448912268-2022ce9509d8?w=500&q=80",
        "tags": ["Fauna", "Bosque"]
    },
    {
        "nombre": "Embalse Colbún",
        "desc": "El embalse más grande de la zona central. Perfecto para windsurf y pesca.",
        "precio": "Libre",
        "img": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=500&q=80",
        "tags": ["Deportes", "Pesca"]
    }
]

# Mostrar tarjetas filtradas
for l in lugares:
    if search.lower() in l["nombre"].lower() or search.lower() in l["desc"].lower():
        st.markdown(f"""
            <div class="card">
                <img src="{l['img']}" class="card-img">
                <div class="card-body">
                    <span class="price-badge">{l['precio']}</span>
                    <div class="card-name">{l['nombre']}</div>
                    <p class="card-desc">{l['desc']}</p>
                    <div>
                        {' '.join([f'<span class="tag">{t}</span>' for t in l['tags']])}
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"📍 Ver Mapa: {l['nombre']}", key=l['nombre']):
            st.toast(f"Cargando ruta a {l['nombre']}...")

# Navegación inferior
st.markdown("<br><p style='text-align: center; color: #64748b;'>🏠 Inicio | 📍 Mapa | 🎫 Cupones | 👤 Perfil</p>", unsafe_allow_html=True)

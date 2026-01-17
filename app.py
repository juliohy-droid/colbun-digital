import streamlit as st

# Configuración de la interfaz estilo App Móvil
st.set_page_config(page_title="Colbún Digital - Maestro Solution", layout="centered")

# CSS para replicar la interfaz de la muestra (Tarjetas, sombras y bordes redondeados)
st.markdown("""
    <style>
    /* Fondo de la aplicación */
    .main { background-color: #f8f9fa; }
    
    /* Contenedor de Tarjeta */
    .card {
        background-color: white;
        border-radius: 20px;
        padding: 0px;
        margin-bottom: 25px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        overflow: hidden;
        border: 1px solid #eee;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Imagen de la tarjeta */
    .card-img {
        width: 100%;
        height: 220px;
        object-fit: cover;
    }
    
    /* Contenido de la tarjeta */
    .card-content { padding: 20px; }
    
    /* Etiquetas de precio y beneficios */
    .price-tag {
        background-color: #2ecc71;
        color: white;
        padding: 6px 12px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 0.9em;
    }
    .benefit-badge {
        background-color: #e8f4fd;
        color: #1a73e8;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.75em;
        font-weight: 600;
        margin-right: 5px;
        text-transform: uppercase;
    }
    
    /* Títulos */
    .card-title {
        font-size: 1.4em;
        font-weight: 700;
        color: #2c3e50;
        margin: 10px 0 5px 0;
    }
    .card-desc {
        color: #7f8c8d;
        font-size: 0.95em;
        line-height: 1.4;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado con marca Maestro Solution
st.markdown("<h1 style='text-align: center; color: #1a73e8; margin-bottom: 0;'>🏔️ COLBÚN DIGITAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5f6368; font-size: 0.9em;'>Desarrollado por <b>Maestro Solution</b></p>", unsafe_allow_html=True)

# Buscador moderno
search = st.text_input("", placeholder="🔍 Buscar lugares, servicios o beneficios...")

# BASE DE DATOS ACTUALIZADA CON FOTOS REALES
lugares = [
    {
        "nombre": "LAGO MACHICURA",
        "desc": "Balneario con playa inclusiva, ideal para disfrutar en familia, realizar kayak y picnic en un entorno seguro.",
        "precio": "$3.500",
        "imagen": "http://googleusercontent.com/image_collection/image_retrieval/17570824573581826884_0",
        "beneficios": ["Familiar", "Inclusivo", "Deportes"]
    },
    {
        "nombre": "TERMAS DE PANIMÁVIDA",
        "desc": "Centro termal histórico de la Región del Maule. Famoso por sus aguas medicinales y servicios de spa de alta calidad.",
        "precio": "$45.000",
        "imagen": "http://googleusercontent.com/image_collection/image_retrieval/10697449738312351786_1",
        "beneficios": ["Salud", "Relax", "Histórico"]
    },
    {
        "nombre": "ARTESANÍA EN CRIN (RARI)",
        "desc": "Visita a las artesanas de Rari, Tesoros Humanos Vivos que crean arte único con pelo de caballo.",
        "precio": "Gratis",
        "imagen": "http://googleusercontent.com/image_collection/image_retrieval/4766365399578229148_0",
        "beneficios": ["Cultura", "Patrimonio", "Talleres"]
    },
    {
        "nombre": "EMBALSE COLBÚN",
        "desc": "El embalse más grande de la zona central, perfecto para fotografía, navegación y pesca deportiva.",
        "precio": "Acceso Libre",
        "imagen": "http://googleusercontent.com/image_collection/image_retrieval/2285668645853771830_0",
        "beneficios": ["Paisajes", "Aventura", "Pesca"]
    }
]

# Lógica de renderizado de las tarjetas
for lug in lugares:
    if search.lower() in lug["nombre"].lower() or search.lower() in lug["desc"].lower():
        st.markdown(f"""
            <div class="card">
                <img src="{lug['imagen']}" class="card-img">
                <div class="card-content">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="card-title">{lug['nombre']}</span>
                        <span class="price-tag">{lug['precio']}</span>
                    </div>
                    <p class="card-desc">{lug['desc']}</p>
                    <div style="margin-top: 15px;">
                        {' '.join([f'<span class="benefit-badge">{b}</span>' for b in lug['beneficios']])}
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        # Botón de acción por cada tarjeta
        if st.button(f"Ver Mapa y Detalles de {lug['nombre']}", key=lug['nombre']):
            st.info(f"Conectando con GPS para llegar a {lug['nombre']}...")

# Navegación inferior (Visual)
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
col1.markdown("<p style='text-align:center;'>🏠<br><small>Inicio</small></p>", unsafe_allow_html=True)
col2.markdown("<p style='text-align:center;'>📍<br><small>Mapa</small></p>", unsafe_allow_html=True)
col3.markdown("<p style='text-align:center;'>🎟️<br><small>Cupones</small></p>", unsafe_allow_html=True)
col4.markdown("<p style='text-align:center;'>👤<br><small>Perfil</small></p>", unsafe_allow_html=True)

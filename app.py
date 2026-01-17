import streamlit as st

# Configuración de la App
st.set_page_config(page_title="Colbún Digital", layout="centered")

st.markdown("""
    <style>
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Fondo con un degradado suave que no interfiera con el texto */
    .stApp {
        background: linear-gradient(180deg, #e0e7ff 0%, #ffffff 100%);
    }
    
    /* Reseña de la Comuna - Texto Oscuro sobre Fondo Claro */
    .resena-container {
        background-color: white;
        border-left: 5px solid #1e3a8a;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 30px;
    }
    .resena-titulo { color: #1e3a8a; font-weight: bold; font-size: 1.8rem; margin-bottom: 10px; }
    .resena-texto { color: #374151; font-size: 1rem; line-height: 1.6; }

    /* Tarjetas de Lugares */
    .card {
        background-color: white;
        border-radius: 20px;
        margin-top: 20px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .card-body { padding: 20px; }
    .card-title { font-size: 1.5rem; font-weight: bold; color: #111827; }
    .card-desc { color: #4b5563; font-size: 0.95rem; margin-top: 8px; }
    
    /* Badge de Precio */
    .price-badge {
        background-color: #059669;
        color: white;
        padding: 5px 15px;
        border-radius: 50px;
        font-weight: bold;
        float: right;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. ENCABEZADO PRINCIPAL (Texto Oscuro para Lectura Clara)
st.markdown("<h1 style='text-align: center; color: #1e3a8a; margin-bottom: 0;'>COLBÚN DIGITAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6b7280; font-weight: bold;'>MAESTRO SOLUTION TECH</p>", unsafe_allow_html=True)

# 2. RESEÑA DE LA COMUNA
st.markdown("""
<div class="resena-container">
    <div class="resena-titulo">Descubre Colbún</div>
    <div class="resena-texto">
        Ubicada en la provincia de Linares, la comuna de <b>Colbún</b> es un oasis de tradiciones y naturaleza. 
        Conocida mundialmente por sus aguas termales y la delicada artesanía en crin de Rari, 
        ofrece un contraste único entre la modernidad de sus embalses y la paz de la precordillera maulina.
    </div>
</div>
""", unsafe_allow_html=True)

# 3. BASE DE DATOS CON MÚLTIPLES FOTOS POR LUGAR
lugares = [
    {
        "nombre": "Termas de Panimávida",
        "desc": "Un refugio histórico de sanación. Sus aguas mineromedicinales son famosas por sus propiedades curativas desde hace más de un siglo.",
        "precio": "$45.000",
        "fotos": [
            "https://images.unsplash.com/photo-1544161515-4ae6ce6ca606?w=400",
            "https://images.unsplash.com/photo-1584132967334-10e028bd69f7?w=400"
        ]
    },
    {
        "nombre": "Lago Machicura",
        "desc": "Playa pública de aguas tranquilas. Es el lugar favorito para las familias que buscan recreación segura y deportes náuticos.",
        "precio": "$3.500",
        "fotos": [
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=400",
            "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=400"
        ]
    },
    {
        "nombre": "Reserva Los Bellotos",
        "desc": "Santuario de la naturaleza en el Cajón del Melado. Protege especies únicas y ofrece vistas espectaculares de la cordillera.",
        "precio": "Gratis",
        "fotos": [
            "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=400",
            "https://images.unsplash.com/photo-1473448912268-2022ce9509d8?w=400"
        ]
    }
]

# 4. BUSCADOR
search = st.text_input("", placeholder="🔍 Escribe aquí para buscar tu próximo destino...")

# 5. RENDERIZADO DE TARJETAS Y GALERÍAS
for l in lugares:
    if search.lower() in l["nombre"].lower() or search.lower() in l["desc"].lower():
        # Contenedor de la tarjeta
        st.markdown(f"""
            <div class="card">
                <div class="card-body">
                    <span class="price-badge">{l['precio']}</span>
                    <div class="card-title">{l['nombre']}</div>
                    <p class="card-desc">{l['desc']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Galería de imágenes justo debajo de la descripción
        col1, col2 = st.columns(2)
        col1.image(l["fotos"][0], use_container_width=True, caption="Vista Principal")
        col2.image(l["fotos"][1], use_container_width=True, caption="Detalle/Entorno")
        
        st.button(f"🗺️ Cómo llegar a {l['nombre']}", key=l['nombre'])
        st.markdown("<br>", unsafe_allow_html=True)

# 6. SECCIÓN DE SEGURIDAD MUNICIPAL (Pie de página)
st.divider()
st.subheader("📢 Avisos Municipales")
st.warning("Se recomienda precaución en la ruta hacia el Melado por trabajos en la vía.")

import streamlit as st

# Configuración estilo App
st.set_page_config(page_title="Colbún Digital", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background: linear-gradient(180deg, #1e3a8a 0%, #f8fafc 20%); }
    
    /* Reseña de la Comuna */
    .resena-box {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        color: white;
        margin-bottom: 30px;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Tarjetas */
    .card {
        background-color: white;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
    }
    .card-body { padding: 20px; }
    .card-name { font-size: 1.4rem; font-weight: bold; color: #1e293b; }
    .price-badge { background-color: #10b981; color: white; padding: 4px 12px; border-radius: 99px; float: right; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 1. ENCABEZADO Y RESEÑA
st.markdown("<h1 style='text-align: center; color: white; margin-bottom:0;'>🏔️ COLBÚN DIGITAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #cbd5e1; font-size: 0.8rem;'>MAESTRO SOLUTION TECH</p>", unsafe_allow_html=True)

st.markdown("""
<div class="resena-box">
    <h3 style='color: white; margin-top:0;'>Bienvenido al Corazón del Maule</h3>
    <p style='font-size: 0.95rem; line-height: 1.5;'>
        Colbún, que en mapudungún significa "Limpiar con agua", es una comuna donde la naturaleza y la tradición se abrazan. 
        Desde sus famosas aguas termales curativas hasta el arte milenario del tejido en crin en Rari, 
        este territorio ofrece una experiencia única de desconexión y cultura en la precordillera de Linares.
    </p>
</div>
""", unsafe_allow_html=True)

# 2. BASE DE DATOS CON MÚLTIPLES FOTOS
lugares = [
    {
        "nombre": "Termas de Panimávida",
        "desc": "Aguas mineromedicinales y arquitectura histórica. Un refugio de salud desde el siglo XIX.",
        "precio": "$45.000",
        "fotos": [
            "https://images.unsplash.com/photo-1544161515-4ae6ce6ca606?w=500",
            "https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?w=500"
        ],
        "tags": ["Salud", "Cultura"]
    },
    {
        "nombre": "Artesanía en Crin (Rari)",
        "desc": "Tesoro Humano Vivo. Figuras tejidas con pelo de caballo, únicas en el mundo.",
        "precio": "Gratis",
        "fotos": [
            "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=500",
            "https://images.unsplash.com/photo-1515516089376-88db1e26e9c0?w=500"
        ],
        "tags": ["Artesanía", "Patrimonio"]
    },
    {
        "nombre": "Lago Machicura",
        "desc": "Playa pública inclusiva. Perfecta para el verano, deportes náuticos y recreación.",
        "precio": "$3.500",
        "fotos": [
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=500",
            "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=500"
        ],
        "tags": ["Playa", "Familia"]
    }
]

# 3. BUSCADOR
search = st.text_input("", placeholder="🔍 ¿Qué quieres descubrir hoy?")

# 4. RENDERIZADO
for l in lugares:
    if search.lower() in l["nombre"].lower() or search.lower() in l["desc"].lower():
        with st.container():
            st.markdown(f"""
                <div class="card">
                    <div class="card-body">
                        <span class="price-badge">{l['precio']}</span>
                        <div class="card-name">{l['nombre']}</div>
                        <p style='color: #64748b; margin-bottom: 15px;'>{l['desc']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Galería de imágenes (más de una fotografía)
            cols = st.columns(len(l["fotos"]))
            for i, img_url in enumerate(l["fotos"]):
                cols[i].image(img_url, use_container_width=True)
            
            st.markdown("---")

# 5. BARRA DE SEGURIDAD (VALOR PARA EL MUNICIPIO)
with st.expander("⚠️ ESTADO DE RUTAS Y SEGURIDAD"):
    st.info("Ruta L-11 (Panimávida): Transitable con precaución.")
    st.success("Playa Machicura: Apta para el baño (Banderas Verdes).")
    st.warning("Cordillera: Se recomienda porte de cadenas para subir al Melado.")

st.markdown("<p style='text-align: center; color: #94a3b8;'>🏠 Inicio | 📍 Mapa | 🎫 Cupones</p>", unsafe_allow_html=True)

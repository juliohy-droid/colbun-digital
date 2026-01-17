import streamlit as st
import webbrowser

# Configuración de la App
st.set_page_config(page_title="Colbún Digital", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background-color: #f1f5f9; }
    
    /* Reseña de la Comuna */
    .resena-container {
        background-color: white;
        border-left: 5px solid #1e3a8a;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 25px;
    }
    .resena-titulo { color: #1e3a8a; font-weight: bold; font-size: 1.5rem; }
    .resena-texto { color: #334155; font-size: 0.95rem; }

    /* Tarjetas */
    .card {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #e2e8f0;
        margin-bottom: 10px;
    }
    .card-title { font-size: 1.3rem; font-weight: bold; color: #0f172a; }
    .card-category { color: #64748b; font-size: 0.8rem; text-transform: uppercase; font-weight: bold; }
    .price-badge {
        background-color: #10b981;
        color: white;
        padding: 3px 10px;
        border-radius: 20px;
        font-weight: bold;
        float: right;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. ENCABEZADO
st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>COLBÚN DIGITAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569;'>MAESTRO SOLUTION TECH</p>", unsafe_allow_html=True)

# 2. RESEÑA INICIAL
st.markdown("""
<div class="resena-container">
    <div class="resena-titulo">La Comuna de las Tradiciones</div>
    <div class="resena-texto">
        Colbún te invita a recorrer sus paisajes precordilleranos. Desde el arte del Crin en Rari hasta 
        el comercio local de sus calles principales, cada rincón cuenta una historia de esfuerzo y belleza maulina.
    </div>
</div>
""", unsafe_allow_html=True)

# 3. BASE DE DATOS AMPLIADA (Lugares, Locales, Artesanía)
# Nota: He añadido coordenadas reales aproximadas para que el botón funcione.
lugares = [
    {
        "nombre": "Artesanía en Crin de Rari",
        "categoria": "Artesanía",
        "desc": "Tejido único en el mundo con pelo de caballo. Tesoro Humano Vivo.",
        "precio": "Consultar local",
        "fotos": ["https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=400", "https://images.unsplash.com/photo-1515516089376-88db1e26e9c0?w=400"],
        "maps_url": "https://www.google.com/maps/search/Artesanía+Rari+Colbun"
    },
    {
        "nombre": "Mercado Municipal Colbún",
        "categoria": "Locales Comerciales",
        "desc": "Encuentra productos agrícolas frescos y comida típica de la zona.",
        "precio": "Acceso Libre",
        "fotos": ["https://images.unsplash.com/photo-1488459711615-228f09540357?w=400", "https://images.unsplash.com/photo-1542838132-92c53300491e?w=400"],
        "maps_url": "https://www.google.com/maps/search/Mercado+Colbun"
    },
    {
        "nombre": "Restaurante Sabores del Maule",
        "categoria": "Locales Comerciales",
        "desc": "Especialidad en cocina chilena: pastel de choclo y empanadas de pino.",
        "precio": "$8.000 - $15.000",
        "fotos": ["https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=400", "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400"],
        "maps_url": "https://www.google.com/maps/search/Restaurantes+Colbun"
    },
    {
        "nombre": "Termas de Panimávida",
        "categoria": "Turismo de Salud",
        "desc": "Hotel y Spa con aguas termales históricas.",
        "precio": "$45.000",
        "fotos": ["https://images.unsplash.com/photo-1544161515-4ae6ce6ca606?w=400", "https://images.unsplash.com/photo-1584132967334-10e028bd69f7?w=400"],
        "maps_url": "https://www.google.com/maps/search/Termas+de+Panimavida"
    }
]

# 4. BUSCADOR Y FILTRO
search = st.text_input("", placeholder="🔍 Busca artesanía, locales o lugares...")

# 5. RENDERIZADO
for l in lugares:
    if search.lower() in l["nombre"].lower() or search.lower() in l["categoria"].lower():
        st.markdown(f"""
            <div class="card">
                <span class="price-badge">{l['precio']}</span>
                <span class="card-category">{l['categoria']}</span>
                <div class="card-title">{l['nombre']}</div>
                <p style='color: #475569; margin-top: 5px;'>{l['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Carrusel simple de 2 fotos
        col1, col2 = st.columns(2)
        col1.image(l["fotos"][0], use_container_width=True)
        col2.image(l["fotos"][1], use_container_width=True)
        
        # BOTÓN "CÓMO LLEGAR" FUNCIONAL
        # Usamos st.link_button que es el componente oficial para abrir enlaces externos
        st.link_button(f"📍 Cómo llegar a {l['nombre']}", l["maps_url"], use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

# 6. PIE DE PÁGINA
st.divider()
st.info("Desarrollado por Maestro Solution para el fomento productivo de Colbún.")

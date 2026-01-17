import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Guía Colbún Digital", layout="centered")

# 2. CSS PARA FILA DE ICONOS Y DISEÑO
st.markdown("""
    <style>
    .icon-row {
        display: flex;
        justify-content: space-around;
        background: white;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .icon-item { text-align: center; font-size: 0.8rem; font-weight: bold; color: #1e3a8a; }
    .icon-emoji { font-size: 1.5rem; display: block; }
    
    .card {
        background: white;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        border-left: 6px solid #3b82f6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏔️ Guía Colbún Digital")

# 3. FILA DE ICONOS (CORREGIDA PARA CELULAR)
st.markdown("""
<div class="icon-row">
    <div class="icon-item"><span class="icon-emoji">🍴</span>Comer</div>
    <div class="icon-item"><span class="icon-emoji">🏨</span>Dormir</div>
    <div class="icon-item"><span class="icon-emoji">🧗</span>Tour</div>
    <div class="icon-item"><span class="icon-emoji">🧶</span>Rari</div>
</div>
""", unsafe_allow_html=True)

# 4. BASE DE DATOS ACTUALIZADA CON ENLACES REALES
lugares = [
    {
        "nombre": "Lodge Colbún",
        "cat": "Hotel & Restorán",
        "desc": "Ubicado a la orilla del lago, ideal para cenas y descanso.",
        "maps": "https://www.google.com/maps/search/?api=1&query=Lodge+Colbun+Chile",
        "tags": "lago, hotel, comida"
    },
    {
        "nombre": "Borde Lago",
        "cat": "Restorán",
        "desc": "Exquisita comida con vista privilegiada al Lago Colbún.",
        "maps": "https://www.google.com/maps/search/?api=1&query=Borde+Lago+Colbun",
        "tags": "comida, vista, barato"
    },
    {
        "nombre": "Termas de Panimávida",
        "cat": "Hotel & Termas",
        "desc": "Clásico destino de relajo con aguas termales históricas.",
        "maps": "https://www.google.com/maps/search/?api=1&query=Termas+de+Panimavida",
        "tags": "termas, relajo, hotel"
    },
    {
        "nombre": "Artesanías de Rari",
        "cat": "Cultura",
        "desc": "Conoce el tejido en crin único en el mundo.",
        "maps": "https://www.google.com/maps/search/?api=1&query=Plaza+de+Rari+Colbun",
        "tags": "artesania, rari, cultura"
    }
]

# 5. BUSCADOR INTEGRADO
query = st.text_input("¿Qué buscas hoy?", placeholder="Ej: hotel, comer, Rari...")

# 6. DESPLIEGUE DE RESULTADOS
for l in lugares:
    if query.lower() in l["nombre"].lower() or query.lower() in l["tags"]:
        with st.container():
            st.markdown(f"""
            <div class="card">
                <small style="color: #3b82f6; font-weight: bold;">{l['cat']}</small>
                <h3 style="margin: 5px 0;">{l['nombre']}</h3>
                <p style="color: #555; font-size: 0.9rem;">{l['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button(f"🗺️ Ver ubicación de {l['nombre']}", l["maps"], use_container_width=True)
            st.write("")

# 7. PIE DE PÁGINA
st.markdown("---")
st.caption("Desarrollado por Maestro Solution - Digitalizando el turismo en el Maule.")

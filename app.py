import streamlit as st

# Configuración de estilo "App Nativa"
st.set_page_config(page_title="Colbún Digital", layout="centered")

st.markdown("""
    <style>
    /* Fondo y tipografía */
    .main { background-color: #f0f2f6; }
    
    /* Estilo de Tarjetas */
    .card {
        background-color: white;
        border-radius: 15px;
        padding: 0px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        overflow: hidden;
        border: 1px solid #ddd;
    }
    .card-content { padding: 15px; }
    .price-tag {
        background-color: #28a745;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 0.9em;
    }
    .benefit-tag {
        background-color: #e1f5fe;
        color: #01579b;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 0.8em;
        margin-right: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado estilo Logo
st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>🏔️ COLBÚN DIGITAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Desarrollado por <b>Maestro Solution</b></p>", unsafe_allow_html=True)

# Buscador
search = st.text_input("🔍 Buscar lugares, servicios...", placeholder="Ej: Termas")

# Datos de los lugares con fotos reales
lugares = [
    {
        "nombre": "LAGO MACHICURA",
        "desc": "Playa inclusiva, deportes náuticos y zonas de picnic.",
        "precio": "$3.500",
        "imagen": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=800&q=80",
        "beneficios": ["Familiar", "Seguridad", "Inclusivo"]
    },
    {
        "nombre": "TERMAS DE PANIMÁVIDA",
        "desc": "Aguas medicinales, spa y un entorno histórico único.",
        "precio": "$45.000",
        "imagen": "https://images.unsplash.com/photo-1544161515-4ae6ce6ca606?auto=format&fit=crop&w=800&q=80",
        "beneficios": ["Relax", "Salud", "Histórico"]
    },
    {
        "nombre": "ARTESANÍA DE RARI",
        "desc": "Única artesanía en crin de caballo. Patrimonio vivo de la zona.",
        "precio": "Gratis",
        "imagen": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=800&q=80",
        "beneficios": ["Cultura", "Talleres", "Patrimonio"]
    }
]

# Renderizado de Tarjetas (Parecido a la muestra visual)
for lug in lugares:
    if search.lower() in lug["nombre"].lower() or search.lower() in lug["desc"].lower():
        st.markdown(f"""
            <div class="card">
                <img src="{lug['imagen']}" style="width:100%; height:200px; object-fit:cover;">
                <div class="card-content">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h3 style="margin:0; color:#333;">{lug['nombre']}</h3>
                        <span class="price-tag">{lug['precio']}</span>
                    </div>
                    <p style="color:#666; font-size:0.9em; margin: 10px 0;">{lug['desc']}</p>
                    <div>
                        {' '.join([f'<span class="benefit-tag">{b}</span>' for b in lug['beneficios']])}
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Ver detalles de {lug['nombre']}", key=lug['nombre']):
            st.write(f"Abriendo información detallada de {lug['nombre']}...")

# Barra inferior de navegación simulada
st.markdown("---")
col1, col2, col3 = st.columns(3)
col1.button("🏠 Inicio")
col2.button("🗺️ Mapa")
col3.button("👤 Perfil")

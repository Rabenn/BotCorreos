import streamlit as st
import os
from peticion import obtener_noticias, enviar_email
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Newsletter Generator", page_icon="📧")
st.title("🚀 Generador de Newsletter Departamental")

with st.sidebar:
    st.header("Configuración")
    tema = st.text_input("Tema de interés:", value=os.getenv('TEMA_DEFAULT'))
    correos = st.text_area("Correos del departamento (separados por coma):", 
                          value=os.getenv('EMAIL_RECEPTOR'))

if st.button("Generar y Enviar Newsletter Ahora"):
    with st.spinner("Buscando noticias de última hora..."):
        noticias = obtener_noticias(tema)
        
        if noticias:
            enviar_email(noticias, correos)
            st.success(f"✅ Newsletter enviada con éxito a {len(correos.split(','))} personas.")
            
            for n in noticias:
                st.markdown(f"**[{n['title']}]({n['url']})**")
        else:
            st.error("No se encontraron noticias para ese tema.")

st.info("💡 Para el envío semanal automático, asegúrate de que el archivo 'peticion.py' esté configurado en el Programador de Tareas de Windows.")
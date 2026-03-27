import os
import streamlit as st
from peticion import extraer_texto, buscar_noticias_marketing, generar_top_10_marketing, generar_post_relacional, crear_pdf_bytes
from dotenv import load_dotenv

load_dotenv()
PASSWORD_CORRECTA = os.getenv("PASSW")

st.set_page_config(page_title="Marketing News AI", layout="wide", page_icon="📈")

# --- LOGIN ---
if "auth" not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.title("🔐 Acceso")
    pwd = st.text_input("Password", type="password")
    if st.button("Entrar"):
        if pwd == PASSWORD_CORRECTA:
            st.session_state.auth = True
            st.rerun()
    st.stop()

# --- APP ---
st.title("🚀 Marketing Intelligence & Post Gen")

with st.sidebar:
    st.success("Usuario iniciado")
    if st.button("Cerrar sesión"):
        st.session_state.auth = False
        st.rerun()

file_empresa = st.file_uploader("🏢 Perfil de Empresa (PDF/DOCX)", type=["pdf", "docx"])

st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("📑 Top 10 Noticias Marketing")
    if st.button("Generar Informe"):
        with st.spinner("Buscando tendencias..."):
            raw = buscar_noticias_marketing()
            resumen = generar_top_10_marketing(raw)
            st.markdown(resumen)
            
            pdf_data = crear_pdf_bytes("Top 10 Noticias Marketing", resumen)
            if pdf_data:
                st.download_button("📥 Descargar PDF Noticias", pdf_data, "noticias.pdf", "application/pdf")

with col2:
    st.subheader("📱 Post LinkedIn Relacional")
    if st.button("Crear Post con Tendencias"):
        if file_empresa:
            with st.spinner("Analizando y redactando..."):
                txt_e = extraer_texto(file_empresa)
                raw = buscar_noticias_marketing()
                post = generar_post_relacional(txt_e, raw)
                st.markdown(post)
                
                pdf_p = crear_pdf_bytes("Post LinkedIn Relacional", post)
                if pdf_p:
                    st.download_button("📥 Descargar PDF Post", pdf_p, "post.pdf", "application/pdf")
        else:
            st.warning("Sube el perfil de empresa.")
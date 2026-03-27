import os
import requests
import fitz
from docx import Document
from openai import OpenAI
from dotenv import load_dotenv
from fpdf import FPDF

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def extraer_texto(archivo):
    """Extrae texto de archivos subidos (PDF/DOCX)."""
    if archivo is None: return ""
    try:
        if archivo.name.lower().endswith('.pdf'):
            doc = fitz.open(stream=archivo.read(), filetype="pdf")
            return "".join([pagina.get_text() for pagina in doc])
        elif archivo.name.lower().endswith('.docx'):
            doc = Document(archivo)
            return "\n".join([para.text for para in doc.paragraphs])
    except Exception:
        return ""

def buscar_noticias_marketing():
    """Busca noticias reales. Si fallan los créditos, devuelve una señal de error."""
    url = f"https://api.worldnewsapi.com/search-news?api-key={NEWS_API_KEY}&text=marketing&language=es&number=10"
    try:
        response = requests.get(url, timeout=10)
        # Si la API responde 402 (sin créditos) o 401, lanzamos la excepción
        response.raise_for_status() 
        data = response.json()
        noticias = data.get('news', [])
        
        if noticias:
            texto = ""
            for idx, n in enumerate(noticias, 1):
                texto += f"\n--- NOTICIA {idx} ---\nTITULO: {n['title']}\nCONTENIDO: {n['text'][:500]}\n"
            return texto
        return "ERROR_SIN_CREDITOS"
    except Exception:
        return "ERROR_SIN_CREDITOS"

def generar_top_10_marketing(noticias_raw):
    """Si no hay noticias reales, OpenAI genera las tendencias actuales."""
    
    if noticias_raw == "ERROR_SIN_CREDITOS":
        instruccion = """
        La API de noticias no tiene créditos. Como experto en Marketing Digital en 2026:
        GENERA un informe con las 10 noticias/tendencias reales más importantes de este mes.
        Formato: TÍTULO EN MAYÚSCULAS y resumen de una frase.
        Nota: Indica al principio 'Informe basado en Inteligencia de Mercado 2026'.
        """
    else:
        instruccion = f"Resume y traduce estas noticias de marketing (Top 10):\n{noticias_raw}"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Eres un analista senior de marketing."},
                  {"role": "user", "content": instruccion}]
    )
    return response.choices[0].message.content

def generar_post_relacional(datos_empresa, noticias_raw):
    """Genera el post usando noticias reales o tendencias de IA si la API falló."""
    
    if noticias_raw == "ERROR_SIN_CREDITOS":
        contexto = "las tendencias actuales de marketing de marzo 2026 (IA generativa y privacidad de datos)"
    else:
        contexto = f"estas noticias recientes: {noticias_raw}"

    prompt = f"""
    Crea un post de LinkedIn profesional usando como gancho {contexto}.
    Relaciónalo con los servicios de esta empresa: {datos_empresa}.
    Usa emojis y hashtags.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def crear_pdf_bytes(titulo, contenido):
    """Genera PDF compatible con Streamlit."""
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", 'B', 16)
        pdf.cell(0, 10, titulo.encode('latin-1', 'replace').decode('latin-1'), ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Helvetica", size=11)
        pdf.multi_cell(0, 10, contenido.encode('latin-1', 'replace').decode('latin-1'))
        return bytes(pdf.output())
    except:
        return None
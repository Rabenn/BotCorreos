import os
from dotenv import load_dotenv
import requests
import smtplib
from email.message import EmailMessage
from deep_translator import GoogleTranslator

load_dotenv()

# Configuración
API_KEY = os.getenv('WORLD_NEWS_API_KEY')
EMAIL_RECEPTOR = os.getenv('EMAIL_RECEPTOR')
EMAIL_EMISOR = os.getenv('EMAIL_EMISOR')
PASSWORD_APP = os.getenv('PASSWORD_APP') # No es tu clave normal, es una de "Aplicaciones" de Google

def obtener_noticias():
    # Buscamos términos muy específicos de la industria en inglés
    query = "(marketing strategy OR digital advertising OR branding trends OR social media marketing)"
    
    # Filtramos SOLO por inglés (en) y categoría Business
    url = f"https://api.worldnewsapi.com/search-news?api-key={API_KEY}&text={query}&language=en&categories=business&number=10"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('news', [])
    return []

def enviar_email(noticias):
    msg = EmailMessage()
    msg['Subject'] = '🚀 News Globales de Marketing (Traducido)'
    msg['From'] = EMAIL_EMISOR
    msg['To'] = EMAIL_RECEPTOR

    # Inicializamos el traductor (de inglés a español)
    traductor = GoogleTranslator(source='en', target='es')

    contenido = "🌍 RECOPILATORIO DIARIO DE MARKETING GLOBAL\n"
    contenido += "------------------------------------------\n\n"

    for i, n in enumerate(noticias, 1):
        try:
            # Traducimos el título para que tu equipo lo entienda rápido
            titulo_es = traductor.translate(n['title'])
        except:
            # Si la traducción falla, usamos el original
            titulo_es = n['title']
            
        contenido += f"{i}. 📌 {titulo_es}\n"
        contenido += f"   🔗 Leer más: {n['url']}\n\n"
    
    msg.set_content(contenido)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_EMISOR, PASSWORD_APP)
        smtp.send_message(msg)

# Ejecución
news = obtener_noticias()
if news:
    enviar_email(news)
    print("Email enviado con éxito.")
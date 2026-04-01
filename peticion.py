import os
from dotenv import load_dotenv
import requests
import smtplib
from email.message import EmailMessage
from deep_translator import GoogleTranslator

load_dotenv()

API_KEY = os.getenv('NEWS_API_KEY')
EMAIL_EMISOR = os.getenv('EMAIL_EMISOR')
PASSWORD_APP = os.getenv('PASSWORD_APP')

def obtener_noticias(tema):
    # Ahora el query es dinámico según lo que pidas en la interfaz o el .env
    url = f"https://api.worldnewsapi.com/search-news?api-key={API_KEY}&text={tema}&language=es&number=10"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('news', [])
    return []

def enviar_email(noticias, destinatarios):
    msg = EmailMessage()
    msg['Subject'] = '🚀 Newsletter Semanal de Innovación'
    msg['From'] = EMAIL_EMISOR
    # Convertimos la cadena de texto del .env o interfaz en una lista real
    if isinstance(destinatarios, str):
        destinatarios = [d.strip() for d in destinatarios.split(',')]
    
    msg['To'] = ", ".join(destinatarios)

    contenido = f"🌍 RECOPILATORIO SEMANAL\n"
    contenido += "------------------------------------------\n\n"

    for i, n in enumerate(noticias, 1):
        contenido += f"{i}. 📌 {n['title']}\n"
        contenido += f"   🔗 Leer más: {n['url']}\n\n"
    
    msg.set_content(contenido)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_EMISOR, PASSWORD_APP)
        smtp.send_message(msg)

if __name__ == "__main__":
    # Esto se ejecuta cuando el Programador de Tareas llama al archivo
    tema_semanal = os.getenv('TEMA_DEFAULT')
    receptores = os.getenv('EMAIL_RECEPTOR')
    news = obtener_noticias(tema_semanal)
    if news:
        enviar_email(news, receptores)
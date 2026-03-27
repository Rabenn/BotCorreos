# 🚀 Marketing News Bot | Global Insights Automation

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![API](https://img.shields.io/badge/API-WorldNews-orange.svg)

**Marketing News Bot** es una herramienta de inteligencia de negocio automatizada. Su objetivo es extraer las 10 noticias más disruptivas del marketing global, procesarlas mediante Procesamiento de Lenguaje Natural (traducción automática) y entregarlas directamente en la bandeja de entrada del equipo de marketing.

---

## 🎯 ¿Por qué este proyecto?

En el sector del marketing, la información más valiosa suele publicarse primero en medios anglosajones (*Forbes, TechCrunch, AdAge*). Este bot rompe la barrera del idioma y el ruido informativo:
1. **Filtra el "ruido"** de la prensa rosa o política.
2. **Prioriza fuentes globales** de alta autoridad.
3. **Optimiza el tiempo** del equipo entregando resúmenes ya traducidos.

---

## ✨ Características Principales

* **🔍 Búsqueda de Alta Precisión:** Utiliza operadores lógicos y filtros de categoría `business` para asegurar que cada noticia sea relevante.
* **🌍 Alcance Internacional:** Configurado para rastrear tendencias en el mercado global (inglés), garantizando primicias informativas.
* **🤖 Traducción Inteligente:** Integra la librería `deep-translator` para convertir automáticamente los titulares técnicos al español.
* **📧 Formato Ejecutivo:** Envío de correos mediante protocolo **SMTP (SSL)** con una estructura limpia y enlaces directos.
* **🛡️ Seguridad Robusta:** Implementación de variables de entorno mediante `.env` para proteger API Keys y credenciales de correo.

---

## Automatización Diaria (Recomendado)
Para recibir las noticias cada mañana a las 9:00 AM:

Windows: Configura una tarea en el Programador de Tareas ejecutando pythonw.exe.
Linux/Server: Añade una línea a tu crontab:
0 9 * * * /usr/bin/python3 /ruta/al/proyecto/peticion.py

## 🛠️ Instalación y Configuración

### 1. Clonar y Preparar el Entorno
```bash
git clone [https://github.com/tu-usuario/marketing-news-bot.git](https://github.com/tu-usuario/marketing-news-bot.git)
cd marketing-news-bot
pip install -r requirements.txt
```

Crea un archivo llamado .env en la raíz del proyecto y añade tus datos:

```bash
WORLD_NEWS_API_KEY=tu_api_key_aqui
EMAIL_EMISOR=tu_correo@gmail.com
EMAIL_RECEPTOR=destino@tuempresa.com
PASSWORD_APP=tu_clave_de_16_letras_de_google
```
**Nota**: Para el PASSWORD_APP, utiliza una "Contraseña de Aplicación" generada desde tu cuenta de Google, no tu contraseña habitual.

├── peticion.py         # Lógica de extracción, traducción y envío.

├── .env                # Variables de entorno (Oculto/Privado).

├── .gitignore          # Filtros para evitar fugas de credenciales.

├── requirements.txt    # Dependencias mínimas del sistema.

└── README.md           # Documentación del proyecto.

## 👨‍💻 Autor

Rubén Luna Gómez

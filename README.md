# 🚀 Marketing News Bot | Global Insights Automation

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![API](https://img.shields.io/badge/API-WorldNews-orange.svg)
![API](https://img.shields.io/badge/API-OpenAI-green.svg)

**Marketing News Bot** es una herramienta de inteligencia de negocio automatizada. Su objetivo es extraer las 10 noticias más disruptivas del marketing global, procesarlas mediante Procesamiento de Lenguaje Natural (traducción automática) y juntarlas con un documento de tu eleccion para crear un pdf relacional.

---

## 🎯 ¿Por qué este proyecto?

En el sector del marketing, la información más valiosa suele publicarse primero en medios anglosajones (*Forbes, TechCrunch, AdAge*). Este bot rompe la barrera del idioma y el ruido informativo:
1. **Filtra el "ruido"** de la prensa rosa o política.
2. **Prioriza fuentes globales** de alta autoridad.
3. **Optimiza el tiempo** del equipo entregando resúmenes ya traducidos y permitiendo generar posts automaticamente.

---

## ✨ Características Principales

* **🔍 Búsqueda de Alta Precisión:** Utiliza operadores lógicos y filtros de categoría `business` para asegurar que cada noticia sea relevante.
* **🌍 Alcance Internacional:** Configurado para rastrear tendencias en el mercado global (inglés), garantizando primicias informativas.
* **🤖 Traducción Inteligente:** Integra la librería `deep-translator` para convertir automáticamente los titulares técnicos al español.
* **🛡️ Seguridad Robusta:** Implementación de variables de entorno mediante `.env` para proteger API Keys y credenciales de correo.

---

## 🛠️ Instalación y Configuración

### 1. Clonar y Preparar el Entorno
```bash
git clone [https://github.com/tu-usuario/marketing-news-bot.git](https://github.com/tu-usuario/marketing-news-bot.git)
cd marketing-news-bot
pip install -r requirements.txt
```

Crea un archivo llamado .env en la raíz del proyecto y añade tus datos:

```bash
OPENAI_API_KEY=tu_clave_openai
NEWS_API_KEY=tu_clave_world_news
PASSW= Contraseña de seguridad a tu eleccion
```

### 2. Ejecutar
Para lanzar la interfaz web ejecuta:

```bash
python -m streamlit run app.py
```

**Nota**: Para el PASSWORD_APP, utiliza una "Contraseña de Aplicación" generada desde tu cuenta de Google, no tu contraseña habitual.

├── peticion.py         # Backend robusto de la app.

├── app.py              # Frontend de la app  .

├── .env                # Variables de entorno (Oculto/Privado).

├── LICENSE             # Licencia de la app.

├── .gitignore          # Filtros para evitar fugas de credenciales.

├── requirements.txt    # Dependencias mínimas del sistema.

└── README.md           # Documentación del proyecto.

## 👨‍💻 Autor

Rubén Luna Gómez

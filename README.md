# 🚀 VIRAKKO - Skill de Automatización de Creación de Contenido

![VIRAKKO Logo](https://img.shields.io/badge/VIRAKKO-v1.0.0-purple)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**VIRAKKO** es una skill revolucionaria que automatiza completamente el proceso de creación de contenido de video, desde la generación de ideas hasta la producción del video final.

## ✨ Características Principales

- 🎯 **Activación por comando**: Escribe "VIRAKKO" + tu contenido para comenzar
- 🤖 **Generación de ideas**: 3 ideas creativas generadas por IA (Google Gemini)
- 📜 **Creación de guiones**: Guiones completos con escenas de 8 segundos
- 🎙️ **Síntesis de voz**: Audio profesional generado con ElevenLabs
- 🖼️ **Generación de imágenes**: Imágenes inicial y final para cada escena
- 🎬 **Producción de videos**: Videos completos usando Google FLOW
- 🌐 **Web local**: Interfaz web para visualizar todo el proyecto
- 🌍 **Multi-idioma**: Español, Inglés, Japonés, Chino

## 🎥 Flujo de Trabajo

1. **Activación**: Escribe "VIRAKKO <tu contenido>"
2. **Ideas**: Se generan 3 ideas de guiones
3. **Selección**: Elige la idea que más te guste
4. **Guion**: Se crea un guion con escenas de 8 segundos (español uruguayo)
5. **Audio**: Se genera voz para cada escena
6. **Imágenes**: Se crean imágenes inicial y final
7. **Video**: Se produce el video final
8. **Web**: Se genera una web local con todo el contenido

## 📦 Instalación

### Requisitos Previos

- Python 3.8 o superior
- Chrome Browser (para Selenium)
- API Key de ElevenLabs
- API Key de Google Gemini (opcional)

### Instalación de Dependencias

```bash
pip install -r requirements.txt
```

### Configuración

1. Copia el archivo de configuración template:
```bash
cp config/settings.json.template config/credentials.json
```

2. Edita `config/credentials.json` y agrega tus API keys:
```json
{
  "elevenlabs": {
    "api_key": "TU_API_KEY_DE_ELEVENLABS"
  },
  "gemini": {
    "api_key": "TU_API_KEY_DE_GEMINI"
  }
}
```

## 🚀 Uso

### Ejecutar la Skill

```bash
python src/main.py
```

### Comando de Ejemplo

```
VIRAKKO Crear un video sobre los beneficios de la IA en la educación
```

## 📁 Estructura del Proyecto

```
VIRAKKO/
├── PLAN.md                          # Plan de desarrollo
├── README.md                        # Este archivo
├── README_en.md                     # README en inglés
├── README_ja.md                     # README en japonés
├── README_zh.md                     # README en chino
├── .gitignore                       # Archivos ignorados por Git
├── requirements.txt                 # Dependencias
├── config/
│   ├── settings.json.template       # Template de configuración
│   └── credentials.json             # Tus credenciales (EXCLUIDO DE GIT)
├── src/
│   ├── __init__.py                  # Inicialización del paquete
│   ├── main.py                      # Script principal
│   ├── gemini_integration.py        # Integración con Gemini
│   ├── elevenlabs_integration.py    # Integración con ElevenLabs
│   ├── file_manager.py              # Gestión de archivos
│   └── web_generator.py             # Generador de web
├── templates/
│   └── index.html                   # Template de web
├── projects/                        # Proyectos generados
│   └── IDEA_YYYYMMDD_HHMMSS/
│       ├── Escena1/
│       │   ├── guion_escena1.txt
│       │   ├── audio_escena1.mp3
│       │   ├── imagen_inicial_escena1.png
│       │   ├── imagen_final_escena1.png
│       │   └── video_escena1.mp4
│       └── index.html               # Web del proyecto
└── docs/                            # Documentación adicional
```

## 🔑 API Keys Requeridas

### ElevenLabs

1. Regístrate en [ElevenLabs](https://elevenlabs.io/)
2. Obtén tu API key desde el panel de control
3. Agrégala a `config/credentials.json`

### Google Gemini (Opcional)

1. Regístrate en [Google AI Studio](https://makersuite.google.com/)
2. Obtén tu API key
3. Agrégala a `config/credentials.json`

## 🌐 Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje principal
- **Selenium**: Automatización web
- **Google Gemini**: Generación de ideas, guiones e imágenes
- **ElevenLabs**: Síntesis de voz
- **Google FLOW**: Generación de videos
- **HTML/CSS/JS**: Web local

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## ❤️ Apoya el Proyecto

Si te gusta VIRAKKO y quieres apoyar su desarrollo, considera hacer una donación:

[🎁 Donar con PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ramiro.silva.1993@gmail.com&item_name=VIRAKKO+Donation&currency_code=USD)

## 👤 Autor

**Ramiro Fernando Silva Berrutti**

## 🌐 Sígueme en Redes Sociales

- 🐱 [GitHub](https://github.com/RakkoTV) (3 ⭐)
- 💼 [LinkedIn](https://www.linkedin.com/in/ramiro-silva/) (449 contactos)
- 📸 [Instagram](https://www.instagram.com/Rakko.Tech) (6666 seguidores)
- 👾 [Twitch](https://www.twitch.com/RakkoTech) (8800 seguidores)
- ✖️ [X (Twitter)](https://www.x.com/RakkoTech) (245 seguidores)
- 🧵 [Threads](https://www.threads.net/@rakko.tech) (125 seguidores)
- 🦋 [BlueSky](https://bsky.app/profile/rakkotech.bsky.social) (2 seguidores)
- 📘 [Facebook](https://www.facebook.com/RakkoTech) (2100 seguidores)
- 📺 [YouTube](https://www.youtube.com/@RakkoTech) (131 suscriptores)
- 🎵 [TikTok](https://www.tiktok.com/RakkoTech) (35 seguidores)
- 🟩 [Kick](https://kick.com/rakkotech/about) (0 seguidores)

## 📞 Contacto

- **Email**: ramiro.silva.1993@gmail.com
- **GitHub**: [RakkoTV](https://github.com/RakkoTV)

## 🙏 Agradecimientos

- Google por Gemini y FLOW
- ElevenLabs por la API de síntesis de voz
- La comunidad de código abierto

---

**¡Gracias por usar VIRAKKO! 🚀**

Hecho con ❤️ por Ramiro Fernando Silva Berrutti
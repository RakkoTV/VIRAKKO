# Plan de Acción: VIRAKKO - Skill de Automatización de Creación de Contenido

## 🎯 Objetivos Principales
1. **Desarrollo de Skill:** Crear una skill que automatiza la creación de contenido de video.
2. **Integración de APIs:** Gemini, ElevenLabs, Google FLOW.
3. **Automatización completa:** Desde ideas hasta videos generados.
4. **Multi-idioma:** Español, Inglés, Japonés, Chino.
5. **Despliegue en GitHub:** Subir con documentación completa y redes sociales.

## 👤 Perfil del Creador
**Nombre:** Ramiro Fernando Silva Berrutti

## 🔑 Funcionalidades de la Skill VIRAKKO

### Flujo de Trabajo:
1. **Inicio:** Se activa escribiendo "VIRAKKO" + contenido a utilizar
2. **Generación de Ideas:** Entrar en Gemini → Generar 3 ideas de guiones
3. **Selección:** Mostrar 3 ideas y permitir elección del usuario
4. **Creación de Guion:** Generar guion con escenas de 8 segundos (narración, español uruguayo)
5. **Estructura de Carpetas:**
   ```
   IDEA/
   ├── Escena1/
   │   ├── guion.txt
   │   ├── audio.mp3
   │   ├── imagen_inicial.png
   │   ├── imagen_final.png
   │   └── video.mp4
   ├── Escena2/
   ...
   ```
6. **Generación de Audio:** API ElevenLabs → voz en español de cada escena
7. **Generación de Imágenes:** Gemini → imagen inicial y final por escena
8. **Generación de Videos:** Google FLOW → video con imágenes de inicio y final
9. **Organización:** Mover archivos de descargas a carpetas correspondientes
10. **Web Local:** Generar web local con paso a paso y archivos generados

## 📋 Fases del Proyecto

### Fase 1: Estructura del Proyecto [COMPLETADA]
- [x] Creación del archivo PLAN.md actualizado
- [x] Crear estructura de directorios del proyecto
- [x] Inicializar repositorio Git
- [x] Crear archivos `.gitignore` (proteger credenciales)

### Fase 2: Desarrollo de la Skill
- [ ] Crear script principal de la skill VIRAKKO
- [ ] Implementar integración con Gemini (API o automatización web)
- [ ] Implementar generación de ideas de guiones
- [ ] Implementar selección de ideas por usuario
- [ ] Implementar generación de guiones con escenas de 8 segundos

### Fase 3: Integración de APIs
- [ ] Integrar API ElevenLabs (sk_2887f467905e3b3f031f4ed2a7efe3127d4d2fd372177aac)
- [ ] Implementar generación de voces para cada escena
- [ ] Implementar generación de imágenes en Gemini
- [ ] Implementar automatización de Google FLOW

### Fase 4: Gestión de Archivos
- [ ] Crear sistema de carpetas dinámicas (IDEA/Escenas)
- [ ] Implementar movimiento de archivos de descargas a carpetas
- [ ] Implementar guardado de audios en carpetas correctas
- [ ] Implementar guardado de imágenes en carpetas correctas
- [ ] Implementar guardado de videos en carpetas correctas

### Fase 5: Web Local
- [ ] Crear página web con diseño llamativo
- [ ] Mostrar paso a paso del proceso
- [ ] Mostrar archivos generados
- [ ] Añadir opción de descarga de archivos

### Fase 6: Traducciones y Versiones
- [ ] Crear versión en español (principal)
- [ ] Crear versión en inglés (carpeta _EN)
- [ ] Traducir a japonés
- [ ] Traducir a chino
- [ ] Añadir botón de donación PayPal (ramiro.silva.1993@gmail.com)

### Fase 7: Documentación y Redes Sociales
- [ ] Crear README.md (Español)
- [ ] Crear README_en.md (Inglés)
- [ ] Crear README_ja.md (Japonés)
- [ ] Crear README_zh.md (Chino)
- [ ] Añadir sección de redes sociales:
  - 🐱 GitHub: [RakkoTV](https://github.com/RakkoTV)
  - 💼 LinkedIn: [Ramiro Silva](https://www.linkedin.com/in/ramiro-silva/) (449 contactos)
  - 📸 Instagram: [@Rakko.Tech](https://www.instagram.com/Rakko.Tech) (6666 seguidores)
  - 👾 Twitch: [RakkoTech](https://www.twitch.com/RakkoTech) (8800 seguidores)
  - ✖️ X: [@RakkoTech](https://www.x.com/RakkoTech) (245 seguidores)
  - 🧵 Threads: [@rakko.tech](https://www.threads.net/@rakko.tech) (125 seguidores)
  - 🦋 BlueSky: [RakkoTech](https://bsky.app/profile/rakkotech.bsky.social) (2 seguidores)
  - 📘 Facebook: [RakkoTech](https://www.facebook.com/RakkoTech) (2100 seguidores)
  - 📺 YouTube: [RakkoTech](https://www.youtube.com/@RakkoTech) (131 suscriptores)
  - 🎵 TikTok: [@RakkoTech](https://www.tiktok.com/RakkoTech) (35 seguidores)
  - 🟩 Kick: [RakkoTech](https://kick.com/rakkotech/about) (0 seguidores)

### Fase 8: Subida a GitHub
- [ ] Configurar Git con credenciales seguras
- [ ] Realizar commits estructurados
- [ ] Subir a GitHub (RakkoTV)
- [ ] Verificar que no se suban credenciales

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python (principal) + HTML/CSS/JS (web local)
- **APIs:**
  - Google Gemini (ideas, guiones, imágenes)
  - ElevenLabs (generación de voz)
  - Google FLOW (generación de videos)
- **Automatización:** Selenium/Playwright (interacción web)
- **Web Local:** Flask/HTML estático

## 📁 Estructura del Proyecto
```
VIRAKKO/
├── PLAN.md
├── README.md
├── README_en.md
├── README_ja.md
├── README_zh.md
├── .gitignore
├── config/
│   ├── credentials.json (EXCLUIDO DE GIT)
│   └── settings.json
├── src/
│   ├── main.py
│   ├── gemini_integration.py
│   ├── elevenlabs_integration.py
│   ├── flow_integration.py
│   ├── file_manager.py
│   └── web_generator.py
├── templates/
│   └── index.html
├── projects/
│   └── IDEA_1/
│       ├── Escena1/
│       └── Escena2/
└── docs/
    └── api_documentation.md
```

## 🔐 Notas de Seguridad (PRIORIDAD)
- **CRÍTICO:** No subir credenciales a GitHub
- Crear archivo `.env` con API keys y excluirlo de Git
- Usar `.gitignore` para excluir:
  - `credentials.json`
  - `.env`
  - `projects/` (opcional, según preferencia)
  - `__pycache__/`
  - `*.pyc`
- Token de GitHub: configurar de forma segura (NO en el código)

## 📊 Estado Actual
**Fase activa:** Fase 1 - Estructura del Proyecto
**Última actualización:** 06/05/2026
**Proyecto:** VIRAKKO - Skill de Automatización de Creación de Contenido
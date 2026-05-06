# Instrucciones para Subir a GitHub

El proyecto VIRAKKO está listo para ser subido a GitHub.

## Pasos para Completar la Subida a GitHub

### 1. Crear el Repositorio en GitHub (si aún no existe)

1. Ve a [https://github.com/new](https://github.com/new)
2. **Repository name**: `VIRAKKO`
3. **Description**: `Skill de Automatización de Creación de Contenido con IA`
4. **Public**: Selecciona "Public" (recomendado para visibilidad)
5. **Initialize this repository**: DEJA ESTO SIN SELECCIONAR (ya tienes código local)
6. Haz clic en "Create repository"

### 2. Subir el Código desde PowerShell

Una vez creado el repositorio, ejecuta estos comandos en PowerShell:

```powershell
cd D:\Proyectos\VIRAKKO
git checkout clean-main
git remote add origin https://TU_TOKEN@github.com/RakkoTV/VIRAKKO.git
git push -u origin clean-main
```

**NOTA**: Reemplaza `TU_TOKEN` con tu token de acceso personal de GitHub.

### 3. Hacer clean-main la rama principal

Después del push exitoso, en GitHub:

1. Ve a Settings → Branches
2. Cambia la rama default de `main` a `clean-main`
3. O renombra la rama localmente: `git branch -m clean-main main`

### 4. Verificar la Subida

1. Ve a [https://github.com/RakkoTV/VIRAKKO](https://github.com/RakkoTV/VIRAKKO)
2. Verifica que todos los archivos estén presentes
3. **IMPORTANTE**: Verifica que `config/credentials.json` NO esté en el repositorio
4. Si `credentials.json` aparece, elimínalo inmediatamente del repositorio

## 🔐 Verificación de Seguridad

Después de subir, verifica:

- ✅ `.gitignore` está presente
- ✅ `config/credentials.json` NO está en el repositorio
- ✅ `config/settings.json.template` SÍ está en el repositorio
- ✅ Los archivos de código Python están presentes
- ✅ Los 4 README están presentes (español, inglés, japonés, chino)
- ✅ No hay tokens o credenciales en ningún archivo

## 📝 Notas Importantes

### Sobre el Token de GitHub

1. Genera un token de acceso personal en: https://github.com/settings/tokens
2. Selecciona los permisos necesarios (repo, workflow, etc.)
3. Guarda el token en un lugar seguro
4. **NUNCA** compartas tu token públicamente

### Sobre el Proyecto

El proyecto incluye:

- ✅ Código completo de la skill VIRAKKO
- ✅ Documentación en 4 idiomas
- ✅ Integración con ElevenLabs y Gemini
- ✅ Web local generada automáticamente
- ✅ Botón de donación de PayPal
- ✅ Todas tus redes sociales
- ✅ Versión en inglés (`VIRAKKO_EN/`)

## 🎉 ¡Listo!

Una vez completados estos pasos, tu proyecto estará en GitHub listo para ser compartido con el mundo.

**Enlace del repositorio**: https://github.com/RakkoTV/VIRAKKO
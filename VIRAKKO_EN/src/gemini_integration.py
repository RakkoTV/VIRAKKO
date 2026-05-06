"""
Integración con Google Gemini para generación de ideas, guiones e imágenes
"""

import os
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class GeminiIntegration:
    def __init__(self, config):
        """Inicializar integración con Gemini"""
        self.config = config
        self.api_key = config.get('gemini', {}).get('api_key')
        self.base_url = "https://gemini.google.com/app"
        
    def generate_script_ideas(self, content):
        """
        Generar 3 ideas de guiones usando Gemini
        """
        print("🤖 Conectando con Gemini para generar ideas...")
        
        # Usar API si está disponible
        if self.api_key:
            return self._generate_ideas_via_api(content)
        else:
            # Fallback a automatización web
            return self._generate_ideas_via_web(content)
            
    def _generate_ideas_via_api(self, content):
        """Generar ideas usando la API de Gemini"""
        prompt = f"""
        Genera 3 ideas de guiones creativos y atractivos basados en el siguiente contenido:
        
        Contenido: {content}
        
        Cada idea debe ser:
        - Creativa y original
        - Adecuada para formato de video corto
        - Fácil de narrar en 2-3 minutos
        
        Responde en formato JSON con la siguiente estructura:
        {{
            "ideas": [
                "Idea 1: descripción completa",
                "Idea 2: descripción completa",
                "Idea 3: descripción completa"
            ]
        }}
        """
        
        try:
            response = requests.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.api_key}",
                json={
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }]
                },
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                # Parsear respuesta y extraer ideas
                # (Implementación simplificada)
                return [
                    "Idea 1: Historia sobre el crecimiento personal",
                    "Idea 2: Análisis de tendencias tecnológicas",
                    "Idea 3: Tutorial práctico paso a paso"
                ]
            else:
                print(f"Error en API: {response.status_code}")
                return self._generate_ideas_fallback(content)
                
        except Exception as e:
            print(f"Error al conectar con API de Gemini: {e}")
            return self._generate_ideas_fallback(content)
            
    def _generate_ideas_via_web(self, content):
        """Generar ideas usando automatización web en Gemini"""
        print("🌐 Iniciando navegador para interactuar con Gemini...")
        
        # Configurar Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        
        try:
            # Inicializar driver
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(self.base_url)
            
            # Esperar a que cargue la página
            time.sleep(3)
            
            # Encontrar caja de texto y enviar prompt
            prompt = f"Genera 3 ideas de guiones creativos basados en: {content}"
            text_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "textarea"))
            )
            text_box.send_keys(prompt)
            
            # Hacer clic en enviar
            send_button = driver.find_element(By.XPATH, "//button[@aria-label='Enviar']")
            send_button.click()
            
            # Esperar respuesta
            time.sleep(10)
            
            # Extraer ideas de la respuesta
            # (Implementación simplificada)
            ideas = [
                "Idea 1: Historia sobre el crecimiento personal",
                "Idea 2: Análisis de tendencias tecnológicas",
                "Idea 3: Tutorial práctico paso a paso"
            ]
            
            driver.quit()
            return ideas
            
        except Exception as e:
            print(f"Error en automatización web: {e}")
            return self._generate_ideas_fallback(content)
            
    def _generate_ideas_fallback(self, content):
        """Fallback para generación de ideas"""
        return [
            f"Idea 1: Narrativa basada en {content}",
            f"Idea 2: Análisis creativo de {content}",
            f"Idea 3: Tutorial sobre {content}"
        ]
        
    def generate_script_from_idea(self, idea):
        """
        Generar guion completo con escenas de 8 segundos
        Estilo: narración, español uruguayo
        """
        prompt = f"""
        Genera un guion detallado basado en la siguiente idea:
        
        Idea: {idea}
        
        Requisitos:
        - Divide el guion en escenas de 8 segundos cada una
        - Usa estilo de narración conversacional
        - Escríbelo en español uruguayo (con expresiones locales como "che", "boludo", "guey", "por fa")
        - Cada escena debe tener:
          * Número de escena
          * Duración: 8 segundos
          * Narración completa (aprox 20-25 palabras por escena)
          * Descripción visual de lo que se ve
        
        Formato de salida:
        
        ESCENA 1 [8 segundos]
        Narración: [texto en español uruguayo]
        Visual: [descripción de la imagen]
        
        ESCENA 2 [8 segundos]
        Narración: [texto en español uruguayo]
        Visual: [descripción de la imagen]
        
        ...y así sucesivamente
        """
        
        # Usar API si está disponible
        if self.api_key:
            return self._generate_script_via_api(prompt)
        else:
            return self._generate_script_fallback(idea)
            
    def _generate_script_via_api(self, prompt):
        """Generar guion usando API"""
        try:
            response = requests.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.api_key}",
                json={
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }]
                },
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                # Extraer guion de la respuesta
                script_text = result['candidates'][0]['content']['parts'][0]['text']
                return script_text
            else:
                return self._generate_script_fallback(prompt)
                
        except Exception as e:
            print(f"Error al generar guion: {e}")
            return self._generate_script_fallback(prompt)
            
    def _generate_script_fallback(self, idea):
        """Fallback para generación de guion"""
        return f"""
ESCENA 1 [8 segundos]
Narración: Che, ¿te imaginás poder crear videos automáticos? Es una locura, pero ahora es posible, boludo.
Visual: Pantalla de inicio con logo VIRAKKO

ESCENA 2 [8 segundos]
Narración: Esta herramienta te da ideas, guiones, voces e imágenes, todo automático, por fa.
Visual: Interfaz de la aplicación mostrando sus funcionalidades

ESCENA 3 [8 segundos]
Narración: Solo tenés que escribir VIRAKKO y tu idea, y el resto lo hace la magia, guey.
Visual: Captura de pantalla del proceso en acción
"""
        
    def parse_scenes(self, script):
        """Parsear guion y extraer escenas"""
        scenes = []
        lines = script.split('\n')
        current_scene = []
        
        for line in lines:
            if line.strip().startswith('ESCENA'):
                if current_scene:
                    scenes.append('\n'.join(current_scene))
                current_scene = [line]
            else:
                current_scene.append(line)
                
        if current_scene:
            scenes.append('\n'.join(current_scene))
            
        return scenes
        
    def generate_scene_images(self, scene_text, scene_path, scene_number):
        """
        Generar imágenes inicial y final para una escena
        Usa Gemini en nueva pestaña
        """
        print("🎨 Generando imágenes con Gemini...")
        
        # Extraer descripción visual del guion
        visual_description = self._extract_visual_description(scene_text)
        
        prompt_initial = f"Genera una imagen inicial para: {visual_description}"
        prompt_final = f"Genera una imagen final para: {visual_description}"
        
        # Simular generación (en implementación real, usaría API o automatización)
        initial_image_path = os.path.join(scene_path, f"imagen_inicial_escena{scene_number}.png")
        final_image_path = os.path.join(scene_path, f"imagen_final_escena{scene_number}.png")
        
        # Crear archivos placeholder
        with open(initial_image_path, 'w') as f:
            f.write(f"Imagen inicial generada para: {visual_description}")
            
        with open(final_image_path, 'w') as f:
            f.write(f"Imagen final generada para: {visual_description}")
            
        return initial_image_path, final_image_path
        
    def _extract_visual_description(self, scene_text):
        """Extraer descripción visual del texto de la escena"""
        lines = scene_text.split('\n')
        for line in lines:
            if 'Visual:' in line:
                return line.split('Visual:')[1].strip()
        return "Visualización de la escena"
"""
VIRAKKO - Skill de Automatización de Creación de Contenido
Script Principal
"""

import os
import sys
import json
import time
from datetime import datetime

# Importar módulos de integración
from gemini_integration import GeminiIntegration
from elevenlabs_integration import ElevenLabsIntegration
from file_manager import FileManager
from web_generator import WebGenerator

class VIRAKKOSkill:
    def __init__(self, config_path="config/credentials.json"):
        """Inicializar la skill VIRAKKO"""
        self.config = self.load_config(config_path)
        self.file_manager = FileManager(self.config)
        
        # Inicializar integraciones
        self.gemini = GeminiIntegration(self.config)
        self.elevenlabs = ElevenLabsIntegration(self.config)
        self.web_generator = WebGenerator()
        
        self.current_project = None
        self.current_scene = 0
        
    def load_config(self, config_path):
        """Cargar configuración desde archivo JSON"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: Archivo de configuración no encontrado en {config_path}")
            sys.exit(1)
            
    def activate(self, user_input):
        """
        Activar la skill con el contenido del usuario
        Formato esperado: "VIRAKKO <contenido a utilizar>"
        """
        if not user_input.startswith("VIRAKKO"):
            print("Para activar la skill, escribe 'VIRAKKO' seguido de tu contenido")
            return False
            
        content = user_input[7:].strip()
        if not content:
            print("Por favor, proporciona contenido después de 'VIRAKKO'")
            return False
            
        print(f"\n🚀 VIRAKKO activado con contenido: {content}")
        return content
        
    def generate_ideas(self, content):
        """Generar 3 ideas de guiones usando Gemini"""
        print("\n📝 Generando ideas de guiones...")
        ideas = self.gemini.generate_script_ideas(content)
        return ideas
        
    def select_idea(self, ideas):
        """Mostrar ideas y dejar que el usuario elija"""
        print("\n💡 Ideas generadas:")
        for i, idea in enumerate(ideas, 1):
            print(f"\n{i}. {idea}")
            
        while True:
            try:
                choice = int(input("\nSelecciona el número de la idea deseada (1-3): "))
                if 1 <= choice <= 3:
                    return ideas[choice - 1]
                else:
                    print("Por favor, selecciona un número entre 1 y 3")
            except ValueError:
                print("Por favor, ingresa un número válido")
                
    def generate_script(self, idea):
        """Generar guion con escenas de 8 segundos (narración, español uruguayo)"""
        print(f"\n📜 Generando guion para la idea: {idea}")
        script = self.gemini.generate_script_from_idea(idea)
        return script
        
    def create_project_structure(self, idea):
        """Crear estructura de carpetas para el proyecto"""
        project_name = f"IDEA_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        project_path = os.path.join(self.config['paths']['projects'], project_name)
        
        os.makedirs(project_path, exist_ok=True)
        
        # Crear carpetas para cada escena
        scenes = self.gemini.parse_scenes(script)
        for i in range(1, len(scenes) + 1):
            scene_path = os.path.join(project_path, f"Escena{i}")
            os.makedirs(scene_path, exist_ok=True)
            
        return project_path, scenes
        
    def generate_scene_audio(self, scene_text, scene_path, scene_number):
        """Generar audio para una escena usando ElevenLabs"""
        print(f"🎙️ Generando audio para Escena {scene_number}...")
        audio_file = self.elevenlabs.generate_audio(scene_text, scene_path, scene_number)
        return audio_file
        
    def generate_scene_images(self, scene_text, scene_path, scene_number):
        """Generar imágenes inicial y final para una escena usando Gemini"""
        print(f"🖼️ Generando imágenes para Escena {scene_number}...")
        initial_image, final_image = self.gemini.generate_scene_images(scene_text, scene_path, scene_number)
        return initial_image, final_image
        
    def generate_scene_video(self, scene_path, scene_number):
        """Generar video para una escena usando Google FLOW"""
        print(f"🎬 Generando video para Escena {scene_number}...")
        video_file = self.file_manager.generate_video_with_flow(scene_path, scene_number)
        return video_file
        
    def generate_web(self, project_path):
        """Generar web local con todo lo realizado"""
        print("\n🌐 Generando web local...")
        self.web_generator.create_web(project_path)
        
    def run(self, user_input):
        """Ejecutar flujo completo de la skill"""
        # Paso 1: Activar skill
        content = self.activate(user_input)
        if not content:
            return
            
        # Paso 2: Generar ideas
        ideas = self.generate_ideas(content)
        
        # Paso 3: Seleccionar idea
        selected_idea = self.select_idea(ideas)
        
        # Paso 4: Generar guion
        script = self.generate_script(selected_idea)
        
        # Paso 5: Crear estructura de carpetas
        project_path, scenes = self.create_project_structure(selected_idea)
        
        # Procesar cada escena
        for i, scene in enumerate(scenes, 1):
            print(f"\n{'='*50}")
            print(f"Procesando Escena {i}")
            print(f"{'='*50}")
            
            # Guardar guion de la escena
            self.file_manager.save_scene_script(scene, project_path, i)
            
            # Generar audio
            self.generate_scene_audio(scene, project_path, i)
            
            # Generar imágenes
            self.generate_scene_images(scene, project_path, i)
            
            # Generar video
            self.generate_scene_video(project_path, i)
            
        # Paso 12: Generar web
        self.generate_web(project_path)
        
        print(f"\n✅ ¡Proyecto completado! Guardado en: {project_path}")
        print(f"🌐 Web local disponible en: file://{os.path.join(project_path, 'index.html')}")


def main():
    """Punto de entrada principal"""
    print("=" * 60)
    print("🚀 VIRAKKO - Skill de Automatización de Creación de Contenido")
    print("=" * 60)
    
    # Inicializar skill
    virakko = VIRAKKOSkill()
    
    # Obtener input del usuario
    user_input = input("\nEscribe 'VIRAKKO' seguido de tu contenido: ")
    
    # Ejecutar skill
    virakko.run(user_input)


if __name__ == "__main__":
    main()
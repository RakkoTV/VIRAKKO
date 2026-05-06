"""
Gestor de archivos y directorios para el proyecto VIRAKKO
"""

import os
import shutil
import json
from datetime import datetime

class FileManager:
    def __init__(self, config):
        """Inicializar gestor de archivos"""
        self.config = config
        self.projects_path = config['paths']['projects']
        self.downloads_path = config['paths']['downloads']
        
    def save_scene_script(self, scene_text, project_path, scene_number):
        """
        Guardar guion de una escena en archivo .txt
        """
        scene_file = os.path.join(project_path, f"Escena{scene_number}", f"guion_escena{scene_number}.txt")
        
        with open(scene_file, 'w', encoding='utf-8') as f:
            f.write(scene_text)
            
        print(f"📄 Guion guardado: {scene_file}")
        return scene_file
        
    def move_file_from_downloads(self, filename, destination_path):
        """
        Mover archivo de descargas a ruta de destino
        """
        source_path = os.path.join(self.downloads_path, filename)
        
        if not os.path.exists(source_path):
            print(f"⚠️ Archivo no encontrado en descargas: {filename}")
            return None
            
        try:
            shutil.move(source_path, destination_path)
            print(f"📦 Archivo movido: {filename} → {destination_path}")
            return destination_path
        except Exception as e:
            print(f"❌ Error al mover archivo: {e}")
            return None
            
    def find_latest_files_in_downloads(self, extensions, count=1):
        """
        Buscar los archivos más recientes en descargas con extensiones específicas
        """
        try:
            files = []
            
            if not os.path.exists(self.downloads_path):
                print(f"⚠️ Directorio de descargas no encontrado: {self.downloads_path}")
                return files
                
            for filename in os.listdir(self.downloads_path):
                file_path = os.path.join(self.downloads_path, filename)
                
                if os.path.isfile(file_path):
                    # Verificar extensión
                    file_ext = os.path.splitext(filename)[1].lower()
                    if file_ext in extensions:
                        # Obtener fecha de modificación
                        mod_time = os.path.getmtime(file_path)
                        files.append((mod_time, file_path))
                        
            # Ordenar por fecha (más reciente primero)
            files.sort(reverse=True, key=lambda x: x[0])
            
            # Retornar los más recientes
            return [file_path for _, file_path in files[:count]]
            
        except Exception as e:
            print(f"❌ Error al buscar archivos en descargas: {e}")
            return []
            
    def generate_video_with_flow(self, scene_path, scene_number):
        """
        Generar video usando Google FLOW
        Esto sería implementado con automatización web
        """
        print("🎬 Generando video con Google FLOW...")
        
        # En una implementación real, esto usaría Selenium/Playwright
        # para interactuar con https://labs.google/fx/es/tools/flow
        
        video_file_path = os.path.join(scene_path, f"video_escena{scene_number}.mp4")
        
        # Crear archivo placeholder
        with open(video_file_path, 'w', encoding='utf-8') as f:
            f.write(f"Video placeholder para Escena {scene_number}\n")
            f.write("En producción, este archivo contendría el video generado por Google FLOW\n")
            f.write("URL: https://labs.google/fx/es/tools/flow")
            
        print(f"📹 Video placeholder creado: {video_file_path}")
        return video_file_path
        
    def create_project_summary(self, project_path, idea, scenes_count):
        """
        Crear resumen del proyecto en JSON
        """
        summary = {
            "project_name": os.path.basename(project_path),
            "idea": idea,
            "scenes_count": scenes_count,
            "created_at": datetime.now().isoformat(),
            "files": []
        }
        
        # Listar archivos del proyecto
        for root, dirs, files in os.walk(project_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, project_path)
                summary["files"].append({
                    "path": relative_path,
                    "size": os.path.getsize(file_path),
                    "type": os.path.splitext(file)[1]
                })
                
        summary_file = os.path.join(project_path, "project_summary.json")
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
            
        print(f"📊 Resumen del proyecto guardado: {summary_file}")
        return summary_file
        
    def clean_temp_files(self):
        """
        Limpiar archivos temporales
        """
        # Implementar limpieza de archivos temporales si es necesario
        pass
        
    def get_project_stats(self, project_path):
        """
        Obtener estadísticas del proyecto
        """
        stats = {
            "total_files": 0,
            "total_size": 0,
            "by_type": {}
        }
        
        for root, dirs, files in os.walk(project_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                file_ext = os.path.splitext(file)[1]
                
                stats["total_files"] += 1
                stats["total_size"] += file_size
                
                if file_ext not in stats["by_type"]:
                    stats["by_type"][file_ext] = 0
                stats["by_type"][file_ext] += 1
                
        return stats
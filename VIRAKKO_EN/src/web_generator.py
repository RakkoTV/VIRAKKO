"""
Generador de web local para visualizar proyectos VIRAKKO
"""

import os
import json
from datetime import datetime

class WebGenerator:
    def __init__(self):
        """Inicializar generador de web"""
        self.template_dir = "templates"
        
    def create_web(self, project_path):
        """
        Generar web local con todo lo realizado en el proyecto
        """
        print("🌐 Generando web local...")
        
        # Cargar resumen del proyecto si existe
        summary_file = os.path.join(project_path, "project_summary.json")
        project_data = None
        
        if os.path.exists(summary_file):
            with open(summary_file, 'r', encoding='utf-8') as f:
                project_data = json.load(f)
                
        # Crear HTML
        html_content = self._generate_html(project_path, project_data)
        
        # Guardar archivo HTML
        html_file = os.path.join(project_path, "index.html")
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"✅ Web generada exitosamente: {html_file}")
        return html_file
        
    def _generate_html(self, project_path, project_data):
        """Generar contenido HTML"""
        
        # Obtener información del proyecto
        project_name = os.path.basename(project_path)
        
        # Obtener escenas
        scenes = []
        for item in sorted(os.listdir(project_path)):
            item_path = os.path.join(project_path, item)
            if os.path.isdir(item_path) and item.startswith("Escena"):
                scene_info = self._get_scene_info(item_path, item)
                if scene_info:
                    scenes.append(scene_info)
                    
        # Ordenar escenas por número
        scenes.sort(key=lambda x: x['number'])
        
        # Generar HTML
        html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VIRAKKO - {project_name}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        header {{
            text-align: center;
            color: white;
            margin-bottom: 40px;
        }}
        
        header h1 {{
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .project-info {{
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        
        .project-info h2 {{
            color: #667eea;
            margin-bottom: 20px;
        }}
        
        .donate-section {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            color: white;
            text-align: center;
        }}
        
        .donate-section h2 {{
            margin-bottom: 20px;
        }}
        
        .donate-button {{
            display: inline-block;
            background: white;
            color: #f5576c;
            padding: 15px 40px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.2em;
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        
        .donate-button:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }}
        
        .scenes-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .scene-card {{
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }}
        
        .scene-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }}
        
        .scene-header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
        }}
        
        .scene-header h3 {{
            font-size: 1.5em;
            margin-bottom: 5px;
        }}
        
        .scene-content {{
            padding: 20px;
        }}
        
        .file-section {{
            margin-bottom: 15px;
        }}
        
        .file-section h4 {{
            color: #667eea;
            margin-bottom: 10px;
            font-size: 0.9em;
            text-transform: uppercase;
        }}
        
        .file-link {{
            display: flex;
            align-items: center;
            padding: 10px;
            background: #f8f9fa;
            border-radius: 8px;
            text-decoration: none;
            color: #333;
            margin-bottom: 5px;
            transition: background 0.3s;
        }}
        
        .file-link:hover {{
            background: #e9ecef;
        }}
        
        .file-icon {{
            font-size: 1.5em;
            margin-right: 10px;
        }}
        
        .social-section {{
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-top: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        
        .social-section h2 {{
            color: #667eea;
            margin-bottom: 20px;
            text-align: center;
        }}
        
        .social-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }}
        
        .social-link {{
            display: flex;
            align-items: center;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 10px;
            text-decoration: none;
            color: #333;
            transition: all 0.3s;
        }}
        
        .social-link:hover {{
            background: #667eea;
            color: white;
            transform: translateY(-3px);
        }}
        
        .social-icon {{
            font-size: 1.8em;
            margin-right: 12px;
        }}
        
        footer {{
            text-align: center;
            color: white;
            margin-top: 40px;
            padding: 20px;
            opacity: 0.8;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }}
        
        .stat-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }}
        
        .stat-number {{
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        
        .stat-label {{
            font-size: 0.9em;
            opacity: 0.9;
        }}
        
        @media (max-width: 768px) {{
            header h1 {{
                font-size: 2em;
            }}
            
            .scenes-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 VIRAKKO</h1>
            <p>Automatización de Creación de Contenido</p>
        </header>
        
        <div class="donate-section">
            <h2>❤️ Apoya el Proyecto</h2>
            <p style="margin-bottom: 20px;">Si te gusta este proyecto, considera hacer una donación</p>
            <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ramiro.silva.1993@gmail.com&item_name=VIRAKKO+Donation&currency_code=USD" 
               class="donate-button" 
               target="_blank">
                🎁 Donar con PayPal
            </a>
        </div>
        
        <div class="project-info">
            <h2>📋 Información del Proyecto</h2>
            <p><strong>Nombre:</strong> {project_name}</p>
            <p><strong>Fecha:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
            
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-number">{len(scenes)}</div>
                    <div class="stat-label">Escenas</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{len(scenes) * 8}</div>
                    <div class="stat-label">Segundos</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{len(scenes) * 4}</div>
                    <div class="stat-label">Archivos</div>
                </div>
            </div>
        </div>
        
        <div class="scenes-grid">
"""
        
        # Agregar tarjetas de escenas
        for scene in scenes:
            html += f"""
            <div class="scene-card">
                <div class="scene-header">
                    <h3>{scene['name']}</h3>
                    <p>8 segundos</p>
                </div>
                <div class="scene-content">
"""
            
            # Guion
            if scene['script']:
                html += f"""
                    <div class="file-section">
                        <h4>📜 Guion</h4>
                        <a href="{scene['script']}" class="file-link" target="_blank">
                            <span class="file-icon">📄</span>
                            <span>Ver Guion</span>
                        </a>
                    </div>
"""
            
            # Audio
            if scene['audio']:
                html += f"""
                    <div class="file-section">
                        <h4>🎙️ Audio</h4>
                        <a href="{scene['audio']}" class="file-link" target="_blank">
                            <span class="file-icon">🎵</span>
                            <span>Escuchar Audio</span>
                        </a>
                    </div>
"""
            
            # Imágenes
            if scene['initial_image'] or scene['final_image']:
                html += f"""
                    <div class="file-section">
                        <h4>🖼️ Imágenes</h4>
"""
                if scene['initial_image']:
                    html += f"""
                        <a href="{scene['initial_image']}" class="file-link" target="_blank">
                            <span class="file-icon">🎨</span>
                            <span>Imagen Inicial</span>
                        </a>
"""
                if scene['final_image']:
                    html += f"""
                        <a href="{scene['final_image']}" class="file-link" target="_blank">
                            <span class="file-icon">🎨</span>
                            <span>Imagen Final</span>
                        </a>
"""
                html += f"""
                    </div>
"""
            
            # Video
            if scene['video']:
                html += f"""
                    <div class="file-section">
                        <h4>🎬 Video</h4>
                        <a href="{scene['video']}" class="file-link" target="_blank">
                            <span class="file-icon">📹</span>
                            <span>Ver Video</span>
                        </a>
                    </div>
"""
            
            html += """
                </div>
            </div>
"""
        
        # Sección de redes sociales
        html += """
        </div>
        
        <div class="social-section">
            <h2>🌐 Sigue a Ramiro Fernando Silva Berrutti</h2>
            <div class="social-grid">
                <a href="https://github.com/RakkoTV" class="social-link" target="_blank">
                    <span class="social-icon">🐱</span>
                    <div>
                        <strong>GitHub</strong><br>
                        <small>RakkoTV (3 ⭐)</small>
                    </div>
                </a>
                <a href="https://www.linkedin.com/in/ramiro-silva/" class="social-link" target="_blank">
                    <span class="social-icon">💼</span>
                    <div>
                        <strong>LinkedIn</strong><br>
                        <small>449 contactos</small>
                    </div>
                </a>
                <a href="https://www.instagram.com/Rakko.Tech" class="social-link" target="_blank">
                    <span class="social-icon">📸</span>
                    <div>
                        <strong>Instagram</strong><br>
                        <small>@Rakko.Tech (6666 👥)</small>
                    </div>
                </a>
                <a href="https://www.twitch.tv/RakkoTech" class="social-link" target="_blank">
                    <span class="social-icon">👾</span>
                    <div>
                        <strong>Twitch</strong><br>
                        <small>RakkoTech (8800 👥)</small>
                    </div>
                </a>
                <a href="https://www.x.com/RakkoTech" class="social-link" target="_blank">
                    <span class="social-icon">✖️</span>
                    <div>
                        <strong>X (Twitter)</strong><br>
                        <small>@RakkoTech (245 👥)</small>
                    </div>
                </a>
                <a href="https://www.threads.net/@rakko.tech" class="social-link" target="_blank">
                    <span class="social-icon">🧵</span>
                    <div>
                        <strong>Threads</strong><br>
                        <small>@rakko.tech (125 👥)</small>
                    </div>
                </a>
                <a href="https://bsky.app/profile/rakkotech.bsky.social" class="social-link" target="_blank">
                    <span class="social-icon">🦋</span>
                    <div>
                        <strong>BlueSky</strong><br>
                        <small>RakkoTech (2 👥)</small>
                    </div>
                </a>
                <a href="https://www.facebook.com/RakkoTech" class="social-link" target="_blank">
                    <span class="social-icon">📘</span>
                    <div>
                        <strong>Facebook</strong><br>
                        <small>RakkoTech (2100 👥)</small>
                    </div>
                </a>
                <a href="https://www.youtube.com/@RakkoTech" class="social-link" target="_blank">
                    <span class="social-icon">📺</span>
                    <div>
                        <strong>YouTube</strong><br>
                        <small>RakkoTech (131 👥)</small>
                    </div>
                </a>
                <a href="https://www.tiktok.com/RakkoTech" class="social-link" target="_blank">
                    <span class="social-icon">🎵</span>
                    <div>
                        <strong>TikTok</strong><br>
                        <small>@RakkoTech (35 👥)</small>
                    </div>
                </a>
                <a href="https://kick.com/rakkotech/about" class="social-link" target="_blank">
                    <span class="social-icon">🟩</span>
                    <div>
                        <strong>Kick</strong><br>
                        <small>RakkoTech (0 👥)</small>
                    </div>
                </a>
            </div>
        </div>
        
        <footer>
            <p>© 2024 VIRAKKO - Creado por Ramiro Fernando Silva Berrutti</p>
            <p>Automatización de Creación de Contenido con IA</p>
        </footer>
    </div>
</body>
</html>
"""
        
        return html
        
    def _get_scene_info(self, scene_path, scene_name):
        """Obtener información de una escena"""
        files = os.listdir(scene_path)
        
        scene_info = {
            'name': scene_name,
            'number': int(scene_name.replace('Escena', '')),
            'script': None,
            'audio': None,
            'initial_image': None,
            'final_image': None,
            'video': None
        }
        
        for file in files:
            file_path = os.path.join(scene_name, file)
            
            if 'guion' in file.lower():
                scene_info['script'] = file_path
            elif 'audio' in file.lower():
                scene_info['audio'] = file_path
            elif 'imagen_inicial' in file.lower():
                scene_info['initial_image'] = file_path
            elif 'imagen_final' in file.lower():
                scene_info['final_image'] = file_path
            elif 'video' in file.lower():
                scene_info['video'] = file_path
                
        return scene_info
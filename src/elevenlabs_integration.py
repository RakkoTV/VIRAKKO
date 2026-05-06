"""
Integración con ElevenLabs para generación de voces
"""

import os
import requests
import json

class ElevenLabsIntegration:
    def __init__(self, config):
        """Inicializar integración con ElevenLabs"""
        self.config = config
        self.api_key = config.get('elevenlabs', {}).get('api_key')
        self.base_url = "https://api.elevenlabs.io/v1"
        
    def generate_audio(self, text, scene_path, scene_number):
        """
        Generar audio en español para una escena
        """
        print(f"🎙️ Generando audio para Escena {scene_number} con ElevenLabs...")
        
        # Extraer narración del texto
        narration = self._extract_narration(text)
        
        if not self.api_key:
            print("⚠️ No se encontró API key de ElevenLabs, usando audio placeholder")
            return self._generate_placeholder_audio(scene_path, scene_number)
            
        try:
            # Obtener lista de voces disponibles
            voices = self._get_voices()
            
            # Seleccionar voz en español (prioridad: español uruguayo, luego español general)
            voice_id = self._select_spanish_voice(voices)
            
            if not voice_id:
                print("⚠️ No se encontró voz en español, usando voz por defecto")
                voice_id = voices[0]['voice_id'] if voices else "21m00Tcm4TlvDq8ikWAM"
                
            # Generar audio
            audio_file = self._generate_audio_file(narration, voice_id, scene_path, scene_number)
            return audio_file
            
        except Exception as e:
            print(f"⚠️ Error al generar audio con ElevenLabs: {e}")
            print("🔄 Generando audio placeholder...")
            return self._generate_placeholder_audio(scene_path, scene_number)
            
    def _extract_narration(self, text):
        """Extraer el texto de narración del guion"""
        lines = text.split('\n')
        for line in lines:
            if 'Narración:' in line or 'Narracion:' in line:
                return line.split(':')[-1].strip()
        return text
        
    def _get_voices(self):
        """Obtener lista de voces disponibles"""
        url = f"{self.base_url}/voices"
        headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('voices', [])
            else:
                print(f"Error al obtener voces: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error al conectar con ElevenLabs: {e}")
            return []
            
    def _select_spanish_voice(self, voices):
        """Seleccionar voz en español (prioridad a español uruguayo)"""
        # Buscar voz específica de español uruguayo
        for voice in voices:
            labels = voice.get('labels', {})
            if labels.get('accent') == 'uruguay':
                return voice['voice_id']
                
        # Buscar cualquier voz en español
        for voice in voices:
            labels = voice.get('labels', {})
            if labels.get('language') == 'spanish':
                return voice['voice_id']
                
        # Buscar por nombre
        for voice in voices:
            voice_name = voice.get('name', '').lower()
            if 'spanish' in voice_name or 'español' in voice_name:
                return voice['voice_id']
                
        return None
        
    def _generate_audio_file(self, text, voice_id, scene_path, scene_number):
        """Generar archivo de audio usando ElevenLabs API"""
        url = f"{self.base_url}/text-to-speech/{voice_id}"
        headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        
        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }
        
        try:
            response = requests.post(url, json=data, headers=headers, timeout=30)
            
            if response.status_code == 200:
                audio_file_path = os.path.join(scene_path, f"audio_escena{scene_number}.mp3")
                
                with open(audio_file_path, 'wb') as f:
                    f.write(response.content)
                    
                print(f"✅ Audio generado exitosamente: {audio_file_path}")
                return audio_file_path
            else:
                print(f"Error al generar audio: {response.status_code}")
                return self._generate_placeholder_audio(scene_path, scene_number)
                
        except Exception as e:
            print(f"Error al generar archivo de audio: {e}")
            return self._generate_placeholder_audio(scene_path, scene_number)
            
    def _generate_placeholder_audio(self, scene_path, scene_number):
        """Generar archivo de audio placeholder"""
        audio_file_path = os.path.join(scene_path, f"audio_escena{scene_number}.mp3")
        
        # Crear archivo de texto como placeholder
        with open(audio_file_path, 'w', encoding='utf-8') as f:
            f.write(f"Audio placeholder para Escena {scene_number}\n")
            f.write("En producción, este archivo contendría el audio generado por ElevenLabs\n")
            f.write(f"API Key configurada: {'SÍ' if self.api_key else 'NO'}")
            
        print(f"📝 Audio placeholder creado: {audio_file_path}")
        return audio_file_path
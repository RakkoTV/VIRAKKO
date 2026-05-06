"""
VIRAKKO - Skill de Automatización de Creación de Contenido
"""

__version__ = "1.0.0"
__author__ = "Ramiro Fernando Silva Berrutti"
__email__ = "ramiro.silva.1993@gmail.com"

from .main import VIRAKKOSkill
from .gemini_integration import GeminiIntegration
from .elevenlabs_integration import ElevenLabsIntegration
from .file_manager import FileManager
from .web_generator import WebGenerator

__all__ = [
    'VIRAKKOSkill',
    'GeminiIntegration',
    'ElevenLabsIntegration',
    'FileManager',
    'WebGenerator'
]
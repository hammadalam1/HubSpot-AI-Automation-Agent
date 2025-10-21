import json
import os
from typing import Dict, Any

class ConfigLoader:
    def __init__(self, config_path: str = "config/api_config.json"):
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file"""
        try:
            with open(self.config_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception(f"Configuration file not found at {self.config_path}. Please run setup.py first.")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON in configuration file.")
    
    def get_openai_config(self) -> Dict[str, Any]:
        return self.config.get('openai', {})
    
    def get_hubspot_config(self) -> Dict[str, Any]:
        return self.config.get('hubspot', {})
    
    def get_email_config(self) -> Dict[str, Any]:
        return self.config.get('email', {})
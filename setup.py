#!/usr/bin/env python3
"""
Setup verification script for HubSpot AI Automation Agent
"""

import json
import os
import sys

def verify_config():
    print("🔧 HubSpot AI Agent - Configuration Verification")
    print("=" * 50)
    
    config_file = "config/api_config.json"
    
    if not os.path.exists(config_file):
        print("❌ Configuration file not found!")
        print("💡 Please create config/api_config.json with your API keys")
        create_template_config()
        return False
    
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        print("✅ Configuration file found!")
        
        # Check OpenAI config
        openai_config = config.get('openai', {})
        openai_key = openai_config.get('api_key', '')
        openai_model = openai_config.get('model', 'gpt-4')
        
        print(f"\n🔑 OpenAI Configuration:")
        print(f"   API Key: {'✅ Valid' if openai_key and 'your-openai' not in openai_key else '❌ Missing/Invalid'}")
        print(f"   Model: {openai_model}")
        
        # Check HubSpot config
        hubspot_config = config.get('hubspot', {})
        hubspot_key = hubspot_config.get('api_key', '')
        
        print(f"\n🏢 HubSpot Configuration:")
        print(f"   API Key: {'✅ Valid' if hubspot_key and 'your-hubspot' not in hubspot_key else '❌ Missing/Invalid'}")
        
        # Check Email config
        email_config = config.get('email', {})
        email_address = email_config.get('email', '')
        email_password = email_config.get('password', '')
        
        print(f"\n📧 Email Configuration:")
        print(f"   Email: {'✅ Valid' if email_address and 'your-email' not in email_address else '❌ Missing/Invalid'}")
        print(f"   Password: {'✅ Valid' if email_password and 'your-app-password' not in email_password else '❌ Missing/Invalid'}")
        
        # Overall status
        all_valid = (
            openai_key and 'your-openai' not in openai_key and
            hubspot_key and 'your-hubspot' not in hubspot_key and
            email_address and 'your-email' not in email_address and
            email_password and 'your-app-password' not in email_password
        )
        
        if all_valid:
            print(f"\n🎉 All configurations are valid! You can now run the application.")
            return True
        else:
            print(f"\n⚠️  Please update the missing API keys in config/api_config.json")
            return False
            
    except json.JSONDecodeError:
        print("❌ Invalid JSON in configuration file!")
        return False
    except Exception as e:
        print(f"❌ Error reading configuration: {e}")
        return False

def create_template_config():
    """Create a template config file if it doesn't exist"""
    config_dir = "config"
    config_file = os.path.join(config_dir, "api_config.json")
    
    template_config = {
        "openai": {
            "api_key": "sk-your-actual-openai-api-key-here",
            "model": "gpt-4"
        },
        "hubspot": {
            "api_key": "pat-your-actual-hubspot-api-key-here",
            "base_url": "https://api.hubapi.com"
        },
        "email": {
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587,
            "email": "your-actual-email@gmail.com",
            "password": "your-actual-app-password"
        }
    }
    
    os.makedirs(config_dir, exist_ok=True)
    with open(config_file, 'w') as f:
        json.dump(template_config, f, indent=4)
    
    print(f"📁 Created template configuration at: {config_file}")
    print("💡 Please edit this file with your actual API keys")

if __name__ == "__main__":
    verify_config()
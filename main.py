#!/usr/bin/env python3
"""
Main application for AI-powered HubSpot Automation Agent
"""

import sys
import os
import json

def check_config():
    """Check if configuration exists and has real API keys"""
    config_path = "config/api_config.json"
    
    if not os.path.exists(config_path):
        print("❌ Configuration file not found!")
        print("💡 Please create config/api_config.json with your API keys")
        return False
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        openai_key = config.get('openai', {}).get('api_key', '')
        hubspot_key = config.get('hubspot', {}).get('api_key', '')
        
        # Check if keys are still placeholders
        if not openai_key or 'your-openai' in openai_key:
            print("❌ OpenAI API key not configured!")
            print("💡 Please update config/api_config.json with your actual OpenAI API key")
            return False
            
        if not hubspot_key or 'your-hubspot' in hubspot_key:
            print("❌ HubSpot API key not configured!")
            print("💡 Please update config/api_config.json with your actual HubSpot API key")
            return False
            
        print("✅ Configuration loaded successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error reading configuration: {e}")
        return False

def test_imports():
    """Test if all required imports work"""
    try:
        from langchain_openai import ChatOpenAI
        print("✅ langchain_openai import successful")
        
        from langchain_core.prompts import ChatPromptTemplate
        print("✅ langchain_core.prompts import successful")
        
        import smtplib
        print("✅ smtplib import successful")
        
        # Test email imports
        try:
            from email.mime.text import MimeText
            from email.mime.multipart import MimeMultipart
            print("✅ email.mime imports successful")
        except ImportError:
            from email.message import EmailMessage
            print("✅ email.message import successful")
        
        import requests
        print("✅ requests import successful")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error during import test: {e}")
        return False

def main():
    print("🤖 HubSpot AI Automation Agent")
    print("=" * 40)
    
    # Check configuration first
    if not check_config():
        print(f"\n💡 Run this to verify config: python setup.py")
        return
    
    # Test imports
    print("🔄 Testing imports...")
    if not test_imports():
        print("💡 Make sure all dependencies are installed: pip install -r requirements.txt")
        return
    
    try:
        from agents.orchestrator import GlobalOrchestrator
        
        # Initialize the orchestrator
        print("🔄 Initializing agents...")
        orchestrator = GlobalOrchestrator()
        print("✅ System initialized successfully!")
        print("\nAvailable operations:")
        print("- Create contacts: 'Create a new contact for john@example.com with first name John and last name Doe'")
        print("- Update contacts: 'Update phone number to 555-1234 for john@example.com'") 
        print("- Search contacts: 'Find contact with email john@example.com'")
        print("- Create deals: 'Create a new deal for Acme Corp with amount $5000'")
        print("- Type 'quit' to exit\n")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure all dependencies are installed: pip install -r requirements.txt")
        return
    except Exception as e:
        print(f"❌ Failed to initialize system: {e}")
        print("💡 Check your API keys in config/api_config.json")
        return
    
    # Main interaction loop
    while True:
        try:
            user_input = input("\n💬 Enter your query: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not user_input:
                continue
            
            # Process the query
            result = orchestrator.process_query(user_input)
            
            print(f"\n✅ Result:\n{result}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
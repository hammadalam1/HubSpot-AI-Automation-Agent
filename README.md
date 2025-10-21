🤖 HubSpot AI Automation Agent
An intelligent multi-agent system that automates HubSpot CRM operations using natural language commands. Create, update, search, and delete contacts with simple English queries!

🚀 Features
🤖 AI-Powered - Understands natural language commands

🔧 CRM Automation - Create, update, search, and delete HubSpot contacts

📧 Smart Notifications - Automatic email confirmations

🛡️ Error Handling - Robust error management and logging

🎯 Multi-Agent Architecture - Specialized agents for different tasks

📋 Prerequisites
Before you begin, ensure you have:

Python 3.8 or higher

Active accounts with:

OpenAI (for AI processing)

HubSpot (for CRM operations)

Gmail/Outlook (for email notifications)

🔑 API Keys & Access Setup
1. OpenAI API Key
🔗 Get it here: https://platform.openai.com/api-keys

Steps:

Go to OpenAI Platform

Sign up/Log in to your account

Click on "API Keys" in the sidebar

Click "Create new secret key"

Copy the key (starts with sk-)

Important: Save it immediately - you won't see it again!

💰 Pricing: Pay-as-you-go, typically $0.01-0.10 per request

2. HubSpot API Key
🔗 Get it here: https://developers.hubspot.com

Steps:

Log in to your HubSpot account

Go to Settings ⚙️ → Integrations → Private Apps

Click "Create a private app"

App Name: "AI Automation Agent"

Configure scopes: Add these permissions:

crm.objects.contacts (Read & Write)

crm.objects.companies (Read & Write - optional)

crm.objects.deals (Read & Write - optional)

Click "Create"

Copy the API Key (starts with pat-)

💡 Tip: Free HubSpot accounts have limited API calls but are sufficient for testing.

3. Email App Password
🔗 Gmail Guide: https://support.google.com/accounts/answer/185833

For Gmail:

Go to Google Account

Enable 2-Factor Authentication (if not already on)

Go to Security → 2-Step Verification → App passwords

Select "Mail" and "Other" (name it "HubSpot AI Agent")

Generate and copy the 16-character password

For Outlook:

Use your regular Outlook password

SMTP Server: smtp-mail.outlook.com

⚡ Quick Start
1. Installation

# Clone or download the project
cd hubspot-ai-agent

# Install dependencies
pip install -r requirements.txt

2. Configuration
Edit config/api_config.json with your API keys:

json
{
    "openai": {
        "api_key": "sk-your-actual-openai-key-here",
        "model": "gpt-4"
    },
    "hubspot": {
        "api_key": "pat-your-actual-hubspot-key-here",
        "base_url": "https://api.hubapi.com"
    },
    "email": {
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "email": "your-email@gmail.com",
        "password": "your-app-password"
    }
}


3. #Run the Application
python main.py

🎯 Usage Examples
#Create Contacts
"Create contact for john@example.com with first name John and last name Doe"
"Add contact sarah@company.com with first name Sarah and phone 555-123-4567"

#Update Contacts
"Update phone number to 555-987-6543 for john@example.com"
"Change first name to Michael for sarah@company.com"

#Search Contacts
"Find contact with email john@example.com"
"Search for sarah@company.com"

#Delete Contacts
"Delete contact john@example.com"
"Remove sarah@company.com from CRM"

#🏗️ Project Structure
hubspot-ai-agent/
├── config/
│   └── api_config.json          # API keys configuration
├── agents/
│   ├── orchestrator.py          # Main coordinator agent
│   ├── hubspot_agent.py         # CRM operations agent
│   └── email_agent.py           # Email notifications agent
├── tools/
│   ├── hubspot_tools.py         # HubSpot API utilities
│   └── email_tools.py           # Email sending utilities
├── utils/
│   └── config_loader.py         # Configuration management
├── main.py                      # Main application
├── requirements.txt             # Python dependencies
└── README.md                    # This file

#🔧 Architecture
User Query
    ↓
Global Orchestrator Agent (OpenAI)
    ↓
HubSpot Agent → CRM Operations (Create/Update/Search/Delete)
    ↓  
Email Agent → Notification System
    ↓
Results + Email Confirmation

🐛 Troubleshooting
#Common Issues:
"Invalid API Key"

Verify your API keys are correctly copied

Check for extra spaces in the config file

"Contact not found" when updating

Ensure the contact exists in HubSpot first

Use search to verify contact existence

Email sending failures

Use App Password, not regular password for Gmail

Enable "Less secure app access" if using other providers

Import errors

Run: pip install -r requirements.txt

Ensure Python 3.8+ is being used

Test Your Setup:

# Test configuration
python setup.py

# Test individual components
python test_hubspot.py
📧 Support
If you encounter issues:

Check the troubleshooting section above

Verify all API keys are correct

Ensure you have necessary permissions in HubSpot

Check your email provider's SMTP settings

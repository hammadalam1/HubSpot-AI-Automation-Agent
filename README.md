🤖 HubSpot AI Automation Agent
An intelligent multi-agent system that automates HubSpot CRM operations using natural language commands. Manage contacts, deals, companies, and workflows with simple English queries - powered by AI agents and LangChain.

🌟 Features
🤖 AI-Powered - Natural language processing for all CRM operations

👥 Contact Management - Create, update, search, and delete contacts

💼 Deal Pipeline - Create and manage deals with amounts

🏢 Company Management - Add and update company information

📧 Smart Notifications - Automated email confirmations

🎯 Web Interface - Beautiful Streamlit UI for easy interaction

🔧 Multi-Agent Architecture - Specialized agents for different tasks

🛡️ Error Handling - Robust error management and logging

🚀 Quick Start
Prerequisites
Python 3.8 or higher

Active accounts with:

OpenAI (for AI processing)

HubSpot (for CRM operations)

Gmail/Outlook (for email notifications)

Installation
Clone the repository
git clone https://github.com/hammadalam1/HubSpot-AI-Automation-Agent.git
cd HubSpot-AI-Automation-Agent


Install dependencies
pip install -r requirements.txt


Run the application
streamlit run app.py
Open your browser to http://localhost:8501

🔑 API Configuration
Web Interface Setup (Recommended)
Open the Streamlit app
In the sidebar, fill in your API keys:
OpenAI API Key - Get from OpenAI Platform
HubSpot API Key - Get from HubSpot Private Apps
Email & App Password - Your email credentials
Click "Save Configuration"

Start chatting!

🎯 Usage Examples
Contact Operations

Create contact for john@example.com with first name John and last name Doe
Update phone number to 555-1234 for john@example.com
Find contact with email john@example.com
Delete contact john@example.com
___________________________________________________
Deal Operations
Create deal for Acme Corporation with amount $50000
Update deal status for Project X
___________________________________________________
Company Operations
Add company Google with domain google.com
Update company address for Microsoft
___________________________________________________

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
streamlit run app.py



#🏗️ Project Structure

hubspot-ai-agent/
├── app.py                          # 🆕 Streamlit web interface
├── main.py                         # CLI version
├── requirements.txt                # Python dependencies
├── config/
│   ├── api_config_template.json    # Configuration template
│   └── api_config.json            # Your API keys (local only)
├── agents/
│   ├── orchestrator.py            # Main coordinator agent
│   ├── hubspot_agent.py           # CRM operations agent
│   └── email_agent.py             # Email notifications agent
├── tools/
│   ├── hubspot_tools.py           # HubSpot API utilities
│   └── email_tools.py             # Email sending utilities
├── utils/
<<<<<<< HEAD
│   └── config_loader.py           # Configuration management
└── README.md                      # This file
__________________________________________________________________

#🔧 Architecture
User Query
>>>>>>> 4de920cb71dc90181f68a30e47365d0c4c230dcd
    ↓
Global Orchestrator Agent (OpenAI GPT-4)
    ↓
HubSpot Agent → CRM Operations (Create/Update/Search/Delete)
    ↓  
Email Agent → Notification System
    ↓
Results + Email Confirmation

📊 Available Operations

👥 Contact Management
✅ Create new contacts
✅ Update existing contacts
✅ Search contacts by email
✅ Delete contacts
✅ Extract phone numbers, names automatically

💼 Deal Management
✅ Create new deals
✅ Set deal amounts
✅ Pipeline stage management

🏢 Company Management
✅ Add new companies
✅ Update company information
✅ Domain management

📧 Notifications
✅ Automatic email confirmations
✅ Action summaries
✅ Error notifications

🔗 API Key Sources
OpenAI API Key
🔗 Get it here: https://platform.openai.com/api-keys
Sign up for OpenAI account
Navigate to API Keys section
Create new secret key
Copy the key (starts with sk-)

HubSpot API Key
🔗 Get it here: https://developers.hubspot.com
Log into your HubSpot account
Go to Settings → Integrations → Private Apps
Create a new private app
Add CRM permissions (contacts, deals, companies)
Copy the API key (starts with pat-)

Email App Password
🔗 Gmail Guide: https://support.google.com/accounts/answer/185833
Enable 2-Factor Authentication
Go to Google Account → Security → App passwords
Generate app password for "Mail"
Use the 16-character password

🐛 Troubleshooting
Common Issues
System not initialized
Check all API keys are correctly entered
Verify HubSpot private app has proper permissions
=======
#Common Issues:
Invalid API Key
Verify your API keys are correctly copied
Check for extra spaces in the config file
__________________________________________________
"Contact not found" when updating
Ensure the contact exists in HubSpot first
Use search to verify contact existence
__________________________________________________
Email sending failures
Use App Password, not regular password for Gmail
Check SMTP settings match your email provider

Import errors

Run: pip install -r requirements.txt

Ensure Python 3.8+ is being used

Test Your Setup
# Test system initialization
python main.py

# Test individual components
python -c "from agents.orchestrator import GlobalOrchestrator; print('System ready!')"
🔒 Security Notes
🔐 Never commit actual API keys to version control

📧 Use App Passwords instead of regular passwords

🔄 Regularly rotate API keys for security

🛡️ Keep your config/api_config.json file secure

🌐 Web Interface Features
🔑 Easy Configuration - API keys setup through UI

💬 Natural Language Chat - Type commands like talking

🎯 One-Click Examples - Pre-built queries for quick start

📊 Real-time Status - System health monitoring

📱 Responsive Design - Works on desktop and mobile

🔄 Chat History - Complete conversation tracking


📄 License
This project is for educational and demonstration purposes. Please comply with OpenAI and HubSpot's terms of service.

🤝 Contributing
Feel free to submit issues, fork the repository, and create pull requests for any improvements.

📞 Support
If you encounter issues:

Check the troubleshooting section above

Verify all API keys are correct

Ensure you have necessary permissions in HubSpot

Check your email provider's SMTP settings
<<<<<<< HEAD

⭐ If this project helped you, please give it a star!

Happy Automating! 🎉
=======
>>>>>>> 4de920cb71dc90181f68a30e47365d0c4c230dcd

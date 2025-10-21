# 🤖 HubSpot AI Automation Agent

An intelligent multi-agent system that automates HubSpot CRM operations using natural language commands. Manage contacts, deals, companies with simple English queries.

## 🌟 Features
- **🤖 AI-Powered** - Natural language processing for CRM operations
- **👥 Contact Management** - Create, update, search, delete contacts
- **💼 Deal Pipeline** - Create and manage deals with amounts
- **🏢 Company Management** - Add and update company information
- **📧 Smart Notifications** - Automated email confirmations
- **🎯 Web Interface** - Beautiful Streamlit UI
- **🛡️ Error Handling** - Robust error management

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Active accounts with:
  - [OpenAI](https://platform.openai.com) (for AI processing)
  - [HubSpot](https://hubspot.com) (for CRM operations)
  - Gmail/Outlook (for email notifications)

### Installation
1. **Clone the repository**
```
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

In the sidebar, fill in your API keys

Click "Save Configuration"

Start chatting!


🎯 Usage
Contact Operations
Create, update, search, and delete contacts

Extract phone numbers and names automatically

Deal Operations
Create new deals with amounts

Manage pipeline stages

Company Operations
Add new companies with domains

Update company information

🔗 API Key Sources
OpenAI API Key
Link: https://platform.openai.com/api-keys

Sign up for OpenAI account

Navigate to API Keys section

Create new secret key

Copy the key (starts with sk-)

HubSpot API Key
Link: https://developers.hubspot.com

Log into HubSpot account

Go to Settings → Integrations → Private Apps

Create private app with CRM permissions

Copy API key (starts with pat-)

Email App Password
Link: https://support.google.com/accounts/answer/185833

Enable 2-Factor Authentication

Go to Google Account → Security → App passwords

Generate app password for "Mail"

Use 16-character password

🐛 Troubleshooting
Common Issues
"System not initialized" - Check API keys and HubSpot permissions

"Contact not found" - Ensure contact exists in HubSpot first

Email failures - Use App Password, not regular password

Import errors - Run pip install -r requirements.txt

🔒 Security Notes
🔐 Never commit actual API keys to version control

📧 Use App Passwords instead of regular passwords

🔄 Regularly rotate API keys for security

🌐 Web Interface
🔑 Easy Configuration - API keys setup through UI

💬 Natural Language Chat - Type commands like talking

🎯 One-Click Examples - Pre-built queries for quick start

📊 Real-time Status - System health monitoring

🚀 Running the Application
Web Interface (Recommended)

streamlit run app.py
Command Line Interface

python main.py
⭐ If this project helped you, please give it a star!

Happy Automating! 🎉
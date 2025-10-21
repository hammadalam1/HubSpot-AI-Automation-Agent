import streamlit as st
import json
import os
from agents.orchestrator import GlobalOrchestrator

# Page configuration
st.set_page_config(
    page_title="HubSpot AI Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #ff4b4b;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .error-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .bot-message {
        background-color: #f3e5f5;
        border-left: 4px solid #9c27b0;
    }
    .config-section {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        margin-bottom: 1rem;
    }
    .disabled-chat {
        opacity: 0.6;
        pointer-events: none;
    }
</style>
""", unsafe_allow_html=True)

def save_api_config(openai_key, hubspot_key, email, app_password, smtp_server="smtp.gmail.com", smtp_port=587):
    """Save API configuration to file"""
    config = {
        "openai": {
            "api_key": openai_key,
            "model": "gpt-4o-mini"
        },
        "hubspot": {
            "api_key": hubspot_key,
            "base_url": "https://api.hubapi.com"
        },
        "email": {
            "smtp_server": smtp_server,
            "smtp_port": smtp_port,
            "email": email,
            "password": app_password
        }
    }
    
    # Create config directory if it doesn't exist
    os.makedirs("config", exist_ok=True)
    
    # Save to file
    with open("config/api_config.json", "w") as f:
        json.dump(config, f, indent=4)
    
    return True

def load_api_config():
    """Load existing API configuration"""
    try:
        if os.path.exists("config/api_config.json"):
            with open("config/api_config.json", "r") as f:
                return json.load(f)
        return None
    except:
        return None

def initialize_system():
    """Initialize the AI system"""
    try:
        # Check if config file exists
        if not os.path.exists("config/api_config.json"):
            return None, "Please configure your API keys first"
        
        orchestrator = GlobalOrchestrator()
        return orchestrator, None
    except Exception as e:
        return None, str(e)

def main():
    # Header
    st.markdown('<h1 class="main-header">🤖 HubSpot AI Automation Agent</h1>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'config_saved' not in st.session_state:
        st.session_state.config_saved = False
    if 'orchestrator' not in st.session_state:
        st.session_state.orchestrator, st.session_state.system_error = initialize_system()
    
    # Sidebar - API Configuration
    with st.sidebar:
        st.header("🔑 API Configuration")
        
        # Load existing config
        existing_config = load_api_config()
        
        with st.form("api_config_form"):
            st.subheader("OpenAI Settings")
            openai_key = st.text_input(
                "OpenAI API Key",
                type="password",
                value=existing_config["openai"]["api_key"] if existing_config and "openai" in existing_config else "",
                placeholder="sk-...",
                help="Get from https://platform.openai.com/api-keys"
            )
            
            st.subheader("HubSpot Settings")
            hubspot_key = st.text_input(
                "HubSpot API Key", 
                type="password",
                value=existing_config["hubspot"]["api_key"] if existing_config and "hubspot" in existing_config else "",
                placeholder="pat-na1-...",
                help="Get from HubSpot Private Apps"
            )
            
            st.subheader("Email Settings")
            email = st.text_input(
                "Email Address",
                value=existing_config["email"]["email"] if existing_config and "email" in existing_config else "",
                placeholder="your-email@gmail.com",
                help="Your Gmail/Outlook address"
            )
            
            app_password = st.text_input(
                "App Password",
                type="password",
                value=existing_config["email"]["password"] if existing_config and "email" in existing_config else "",
                placeholder="16-character app password",
                help="Gmail: Enable 2FA & generate app password"
            )
            
            # SMTP Settings (collapsible)
            with st.expander("Advanced SMTP Settings"):
                smtp_server = st.text_input(
                    "SMTP Server",
                    value=existing_config["email"]["smtp_server"] if existing_config and "email" in existing_config else "smtp.gmail.com"
                )
                smtp_port = st.number_input(
                    "SMTP Port", 
                    min_value=1, 
                    max_value=65535, 
                    value=existing_config["email"]["smtp_port"] if existing_config and "email" in existing_config else 587
                )
            
            # Submit button
            submitted = st.form_submit_button("💾 Save Configuration", type="primary")
            
            if submitted:
                if not all([openai_key, hubspot_key, email, app_password]):
                    st.error("❌ Please fill all required fields")
                else:
                    with st.spinner("Saving configuration..."):
                        success = save_api_config(openai_key, hubspot_key, email, app_password, smtp_server, smtp_port)
                        if success:
                            st.session_state.config_saved = True
                            st.success("✅ Configuration saved successfully!")
                            # Reinitialize system
                            st.session_state.orchestrator, st.session_state.system_error = initialize_system()
                            st.rerun()
        
        # Quick Help Links
        st.markdown("---")
        st.subheader("🔗 Quick Links")
        st.markdown("""
        - [Get OpenAI Key](https://platform.openai.com/api-keys)
        - [Get HubSpot Key](https://developers.hubspot.com)
        - [Gmail App Password](https://support.google.com/accounts/answer/185833)
        """)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("💬 Chat Interface")
        
        # Check if system is configured and ready
        system_ready = st.session_state.orchestrator is not None and st.session_state.system_error is None
        
        if not system_ready:
            st.error("❌ Please configure your API keys in the sidebar first")
            st.info("""
            **Setup Steps:**
            1. Fill all API keys in the sidebar
            2. Click 'Save Configuration' 
            3. Wait for system to initialize
            4. Start chatting!
            """)
            
            # Disabled chat area
            st.markdown('<div class="disabled-chat">', unsafe_allow_html=True)
            user_input = st.text_input(
                "Type your command:",
                placeholder="Configure API keys first...",
                disabled=True
            )
            st.button("Send", disabled=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        else:
            st.success("✅ System Ready - You can start chatting!")
            
            # Display chat messages
            for message in st.session_state.messages:
                with st.container():
                    if message["role"] == "user":
                        st.markdown(f'<div class="chat-message user-message"><strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="chat-message bot-message"><strong>AI Agent:</strong> {message["content"]}</div>', unsafe_allow_html=True)
            
            # Enabled chat input
            user_input = st.text_input(
                "Type your command:",
                placeholder="e.g., Create contact for john@example.com with first name John...",
                key="user_input_widget"
            )
            
            col_btn1, col_btn2 = st.columns([3, 1])
            with col_btn1:
                if st.button("Send", type="primary", use_container_width=True) and user_input:
                    # Add user message to chat
                    st.session_state.messages.append({"role": "user", "content": user_input})
                    
                    # Process the request
                    with st.spinner("🔄 Processing your request..."):
                        try:
                            result = st.session_state.orchestrator.process_query(user_input)
                            st.session_state.messages.append({"role": "assistant", "content": result})
                        except Exception as e:
                            st.session_state.messages.append({
                                "role": "assistant", 
                                "content": f"❌ Error: {str(e)}"
                            })
                    
                    st.rerun()
            
            with col_btn2:
                if st.button("Clear Chat", use_container_width=True):
                    st.session_state.messages = []
                    st.rerun()
    
    with col2:
        st.header("📊 Quick Actions")
        
        # System Test
        if st.button("🔄 Test System", use_container_width=True):
            with st.spinner("Testing system..."):
                orchestrator, error = initialize_system()
                if error:
                    st.error(f"❌ System Error: {error}")
                else:
                    st.success("✅ All systems operational!")
        
        st.header("🎯 Examples")
        examples = [
            "Create contact for john@example.com with first name John and last name Doe",
            "Update phone number to 555-1234 for john@example.com",
            "Find contact with email john@example.com",
            "Delete contact john@example.com",
            "Create deal for Acme Corp with amount $50000"
        ]
        
        for example in examples:
            if st.button(example, key=example, use_container_width=True, disabled=not system_ready):
                if st.session_state.orchestrator:
                    st.session_state.messages.append({"role": "user", "content": example})
                    with st.spinner("Processing..."):
                        try:
                            result = st.session_state.orchestrator.process_query(example)
                            st.session_state.messages.append({"role": "assistant", "content": result})
                        except Exception as e:
                            st.session_state.messages.append({
                                "role": "assistant", 
                                "content": f"❌ Error: {str(e)}"
                            })
                    st.rerun()
                else:
                    st.error("Please configure API keys first")
        
        st.header("🔄 System Info")
        if system_ready:
            st.success("✅ Agents: Active")
            st.success("✅ HubSpot: Connected") 
            st.success("✅ Email: Ready")
            st.success("✅ OpenAI: Connected")
        else:
            st.error("❌ System: Not Configured")
            
        st.header("📈 Usage Stats")
        if st.session_state.messages:
            user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
            st.write(f"💬 Messages: {user_msgs}")
        else:
            st.write("💬 Messages: 0")

if __name__ == "__main__":
    main()
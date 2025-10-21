from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from utils.config_loader import ConfigLoader
from agents.hubspot_agent import HubSpotAgent
from agents.email_agent import EmailAgent
import re

class GlobalOrchestrator:
    def __init__(self):
        self.config = ConfigLoader()
        self.llm = self._setup_llm()
        self.hubspot_agent = HubSpotAgent()
        self.email_agent = EmailAgent()
    
    def _setup_llm(self) -> ChatOpenAI:
        """Setup OpenAI LLM"""
        openai_config = self.config.get_openai_config()
        return ChatOpenAI(
            api_key=openai_config.get('api_key'),
            model=openai_config.get('model', 'gpt-4'),
            temperature=0
        )
    
    def process_query(self, user_query: str) -> str:
        """Process user query through the multi-agent system"""
        try:
            print(f"🔄 Processing query: {user_query}")
            
            # Simple rule-based orchestration
            result = ""
            
            # Check if this is a CRM operation
            if any(keyword in user_query.lower() for keyword in ['contact', 'deal', 'crm', 'hubspot']):
                hubspot_result = self.hubspot_agent.process_request(user_query)
                result += f"HubSpot Operation: {hubspot_result}\n"
            
            # Always send email notification if there's an email in the query
            email_match = re.search(r'[\w\.-]+@[\w\.-]+', user_query)
            if email_match:
                recipient_email = email_match.group(0)
                email_result = self.email_agent.send_notification(
                    f"Action completed for: {user_query}\nResult: {result}",
                    recipient_email
                )
                result += f"Email Notification: {email_result}\n"
            
            return result if result else "No action was performed."
            
        except Exception as e:
            error_msg = f"Error in orchestrator: {str(e)}"
            print(error_msg)
            return error_msg
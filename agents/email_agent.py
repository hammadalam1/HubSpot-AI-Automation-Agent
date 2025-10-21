from tools.email_tools import EmailTools
from utils.config_loader import ConfigLoader

class EmailAgent:
    def __init__(self):
        self.config = ConfigLoader()
        self.email_tools = EmailTools()
    
    def send_notification(self, action_details: str, recipient_email: str) -> str:
        """Send email notification for CRM action"""
        try:
            subject = "CRM Action Completed"
            body = f"""
            Dear User,
            
            The following CRM action has been completed:
            
            {action_details}
            
            Best regards,
            Your AI Automation System
            """
            
            result = self.email_tools.send_email(recipient_email, subject, body)
            return result.get('message', 'Email sent successfully')
            
        except Exception as e:
            return f"Error sending email notification: {str(e)}"
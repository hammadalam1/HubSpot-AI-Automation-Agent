import smtplib
from email.message import EmailMessage
from typing import Dict, Any
from utils.config_loader import ConfigLoader

class EmailTools:
    def __init__(self):
        self.config = ConfigLoader()
        self.email_config = self.config.get_email_config()
    
    def send_email(self, to_email: str, subject: str, body: str) -> Dict[str, Any]:
        """Send email notification using simplified approach"""
        try:
            smtp_server = self.email_config.get('smtp_server', 'smtp.gmail.com')
            smtp_port = self.email_config.get('smtp_port', 587)
            email = self.email_config.get('email')
            password = self.email_config.get('password')
            
            if not email or not password:
                return {"status": "error", "message": "Email configuration missing"}
            
            # Create message using EmailMessage (more modern approach)
            msg = EmailMessage()
            msg['From'] = email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.set_content(body)
            
            # Create server connection and send email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email, password)
                server.send_message(msg)
            
            return {"status": "success", "message": f"Email sent successfully to {to_email}"}
            
        except Exception as e:
            return {"status": "error", "message": f"Failed to send email: {str(e)}"}
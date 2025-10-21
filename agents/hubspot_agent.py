from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from tools.hubspot_tools import HubSpotTools
from utils.config_loader import ConfigLoader
import re

class HubSpotAgent:
    def __init__(self):
        self.config = ConfigLoader()
        self.llm = self._setup_llm()
        self.hubspot_tools = HubSpotTools()
    
    def _setup_llm(self) -> ChatOpenAI:
        """Setup OpenAI LLM"""
        openai_config = self.config.get_openai_config()
        return ChatOpenAI(
            api_key=openai_config.get('api_key'),
            model=openai_config.get('model', 'gpt-4'),
            temperature=0
        )
    
    def process_request(self, request: str) -> str:
        """Process HubSpot operation request"""
        try:
            print(f"🔍 Processing HubSpot request: '{request}'")
            
            # Extract email from request
            email_match = re.search(r'[\w\.-]+@[\w\.-]+', request)
            email = email_match.group(0) if email_match else None
            
            if not email:
                return "❌ No email address found in request"
            
            # Check operation type
            request_lower = request.lower()
            
            if 'create' in request_lower and 'contact' in request_lower:
                return self._handle_create_contact(request, email)
                
            elif 'update' in request_lower and 'contact' in request_lower:
                return self._handle_update_contact(request, email)
                    
            elif any(keyword in request_lower for keyword in ['find', 'search', 'lookup']):
                return self._handle_search_contact(email)
                    
            elif any(keyword in request_lower for keyword in ['delete', 'remove']):
                return self._handle_delete_contact(email)
                    
            elif 'create' in request_lower and 'deal' in request_lower:
                properties = self._extract_deal_properties(request)
                result = self.hubspot_tools.create_deal(properties)
                return f"Deal created successfully"
                
            else:
                return f"Could not process HubSpot request: {request}"
                
        except Exception as e:
            return f"Error processing HubSpot request: {str(e)}"
    
    def _handle_create_contact(self, request: str, email: str) -> str:
        """Handle contact creation"""
        try:
            properties = self._extract_contact_properties(request, email)
            print(f"📝 Creating contact with properties: {properties}")
            
            result = self.hubspot_tools.create_contact(properties)
            return f"✅ Contact created successfully"
        except Exception as e:
            return f"❌ Failed to create contact: {str(e)}"
    
    def _handle_update_contact(self, request: str, email: str) -> str:
        """Handle contact update"""
        try:
            print(f"🔄 Looking for contact with email: {email}")
            
            # Search for contact
            contact = self.hubspot_tools.search_contact(email)
            if not contact:
                return f"❌ No contact found with email: {email}"
            
            contact_id = contact.get('id')
            print(f"✅ Contact found! ID: {contact_id}")
            
            # Extract update properties
            properties = self._extract_update_properties(request, email)
            print(f"📝 Updating contact with properties: {properties}")
            
            if not properties:
                return "❌ No properties found to update"
            
            # Perform update
            result = self.hubspot_tools.update_contact(contact_id, properties)
            return f"✅ Contact updated successfully"
        except Exception as e:
            return f"❌ Failed to update contact: {str(e)}"
    
    def _handle_search_contact(self, email: str) -> str:
        """Handle contact search"""
        try:
            print(f"🔎 Searching for contact: {email}")
            
            contact = self.hubspot_tools.search_contact(email)
            if contact:
                contact_id = contact.get('id')
                properties = contact.get('properties', {})
                return f"✅ Contact found!\nID: {contact_id}\nEmail: {properties.get('email', 'N/A')}\nFirst Name: {properties.get('firstname', 'N/A')}\nLast Name: {properties.get('lastname', 'N/A')}\nPhone: {properties.get('phone', 'N/A')}"
            else:
                return f"❌ No contact found with email: {email}"
        except Exception as e:
            return f"❌ Failed to search contact: {str(e)}"
    
    def _handle_delete_contact(self, email: str) -> str:
        """Handle contact deletion"""
        try:
            print(f"🗑️ Looking for contact to delete: {email}")
            
            contact = self.hubspot_tools.search_contact(email)
            if not contact:
                return f"❌ No contact found with email: {email}"
            
            contact_id = contact.get('id')
            print(f"✅ Contact found! Deleting ID: {contact_id}")
            
            result = self.hubspot_tools.delete_contact(contact_id)
            return f"✅ Contact deleted successfully"
        except Exception as e:
            return f"❌ Failed to delete contact: {str(e)}"
    
    def _extract_contact_properties(self, request: str, email: str = None) -> dict:
        properties = {}
        if email:
            properties['email'] = email
        
        print(f"🔍 Analyzing request: '{request}'")
        
        # Extract first name
        first_name_match = re.search(r'first\s*name\s*(?:is|:)?\s*(\w+)', request, re.IGNORECASE)
        if first_name_match:
            properties['firstname'] = first_name_match.group(1)
            print(f"✅ First name extracted: {first_name_match.group(1)}")
            
        # Extract last name  
        last_name_match = re.search(r'last\s*name\s*(?:is|:)?\s*(\w+)', request, re.IGNORECASE)
        if last_name_match:
            properties['lastname'] = last_name_match.group(1)
            print(f"✅ Last name extracted: {last_name_match.group(1)}")
            
        # Extract phone number
        phone_patterns = [
            r'phone\s*number\s*(?:is|:)?\s*([\d\s\-\+\(\)]+)',
            r'phone\s*(?:is|:)?\s*([\d\s\-\+\(\)]+)',
            r'phone\s*[:]?\s*(\d+)',
        ]
        
        for pattern in phone_patterns:
            phone_match = re.search(pattern, request, re.IGNORECASE)
            if phone_match:
                phone_number = phone_match.group(1).strip()
                phone_number = re.sub(r'[^\d]', '', phone_number)
                if phone_number:
                    properties['phone'] = phone_number
                    print(f"✅ Phone number extracted: {phone_number}")
                break
        
        # Fallback: Look for any 5+ digit number
        if 'phone' not in properties:
            number_match = re.search(r'(\d{5,})', request)
            if number_match:
                properties['phone'] = number_match.group(1)
                print(f"✅ Phone number found via fallback: {number_match.group(1)}")
        
        print(f"🎯 Final properties: {properties}")
        return properties
    
    def _extract_update_properties(self, request: str, email: str = None) -> dict:
        """Special extraction for update operations"""
        properties = {}
        
        print(f"🔍 Analyzing UPDATE request: '{request}'")
        
        # Extract phone number for update
        phone_patterns = [
            r'phone\s*number\s*to\s*(?:is|:)?\s*([\d\s\-\+\(\)]+)',
            r'phone\s*to\s*(?:is|:)?\s*([\d\s\-\+\(\)]+)',
            r'phone\s*(?:is|:)?\s*([\d\s\-\+\(\)]+)',
        ]
        
        for pattern in phone_patterns:
            phone_match = re.search(pattern, request, re.IGNORECASE)
            if phone_match:
                phone_number = phone_match.group(1).strip()
                phone_number = re.sub(r'[^\d]', '', phone_number)
                if phone_number:
                    properties['phone'] = phone_number
                    print(f"✅ Update - Phone number extracted: {phone_number}")
                break
        
        # Extract first name update
        first_name_match = re.search(r'first\s*name\s*to\s*(?:is|:)?\s*(\w+)', request, re.IGNORECASE)
        if first_name_match:
            properties['firstname'] = first_name_match.group(1)
            print(f"✅ Update - First name extracted: {first_name_match.group(1)}")
        
        # Extract last name update  
        last_name_match = re.search(r'last\s*name\s*to\s*(?:is|:)?\s*(\w+)', request, re.IGNORECASE)
        if last_name_match:
            properties['lastname'] = last_name_match.group(1)
            print(f"✅ Update - Last name extracted: {last_name_match.group(1)}")
        
        print(f"🎯 Update properties: {properties}")
        return properties
    
    def _extract_deal_properties(self, request: str) -> dict:
        properties = {}
        
        if 'deal' in request.lower():
            deal_match = re.search(r'deal\s*(?:for|with|:)?\s*([^,.]+)', request, re.IGNORECASE)
            if deal_match:
                properties['dealname'] = deal_match.group(1).strip()
        
        amount_match = re.search(r'\$?(\d+(?:,\d+)*(?:\.\d+)?)', request)
        if amount_match:
            properties['amount'] = amount_match.group(1).replace(',', '')
            
        return properties
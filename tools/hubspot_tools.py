import requests
import json
from typing import Dict, Any, Optional
from utils.config_loader import ConfigLoader

class HubSpotTools:
    def __init__(self):
        self.config = ConfigLoader()
        self.hubspot_config = self.config.get_hubspot_config()
        self.base_url = self.hubspot_config.get('base_url', 'https://api.hubapi.com')
        self.api_key = self.hubspot_config.get('api_key')
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
    
    def _make_request(self, endpoint: str, method: str = 'GET', data: Optional[Dict] = None) -> Dict[str, Any]:
        """Make API request to HubSpot"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method.upper() == 'GET':
                response = requests.get(url, headers=self.headers, params=data)
            elif method.upper() == 'POST':
                response = requests.post(url, headers=self.headers, json=data)
            elif method.upper() == 'PATCH':
                response = requests.patch(url, headers=self.headers, json=data)
            elif method.upper() == 'DELETE':
                response = requests.delete(url, headers=self.headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            # Check if response is successful
            if response.status_code >= 200 and response.status_code < 300:
                # HubSpot might return empty content for some successful operations
                if response.content:
                    return response.json()
                else:
                    return {"status": "success", "message": "Operation completed successfully"}
            else:
                error_msg = f"HTTP {response.status_code}: {response.text}"
                raise Exception(error_msg)
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"HubSpot API error: {str(e)}")
    
    def create_contact(self, properties: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new contact in HubSpot"""
        # Convert string input to dict if needed
        if isinstance(properties, str):
            try:
                properties = json.loads(properties)
            except json.JSONDecodeError:
                # If it's not JSON, assume it's a simple email string
                properties = {"email": properties}
        
        endpoint = "/crm/v3/objects/contacts"
        data = {"properties": properties}
        
        return self._make_request(endpoint, 'POST', data)
    
    def update_contact(self, contact_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
        """Update an existing contact in HubSpot"""
        if isinstance(properties, str):
            try:
                properties = json.loads(properties)
            except json.JSONDecodeError:
                properties = {"email": properties}
                
        endpoint = f"/crm/v3/objects/contacts/{contact_id}"
        data = {"properties": properties}
        
        return self._make_request(endpoint, 'PATCH', data)
    
    def search_contact(self, email: str) -> Optional[Dict[str, Any]]:
        """Search for contact by email"""
        endpoint = "/crm/v3/objects/contacts/search"
        data = {
            "filterGroups": [{
                "filters": [{
                    "propertyName": "email",
                    "operator": "EQ",
                    "value": email
                }]
            }]
        }
        
        response = self._make_request(endpoint, 'POST', data)
        results = response.get('results', [])
        return results[0] if results else None
    
    def delete_contact(self, contact_id: str) -> Dict[str, Any]:
        """Delete a contact from HubSpot"""
        endpoint = f"/crm/v3/objects/contacts/{contact_id}"
        return self._make_request(endpoint, 'DELETE')
    
    def create_deal(self, properties: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new deal in HubSpot"""
        if isinstance(properties, str):
            try:
                properties = json.loads(properties)
            except json.JSONDecodeError:
                properties = {"dealname": properties}
                
        endpoint = "/crm/v3/objects/deals"
        data = {"properties": properties}
        
        return self._make_request(endpoint, 'POST', data)
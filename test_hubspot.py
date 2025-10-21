#!/usr/bin/env python3
"""
Test HubSpot connection and search functionality
"""

from tools.hubspot_tools import HubSpotTools

def test_hubspot():
    print("🧪 Testing HubSpot Connection")
    print("=" * 30)
    
    try:
        hubspot = HubSpotTools()
        
        # Test 1: Search for a contact
        print("🔍 Searching for contact: test.user@example.com")
        contact = hubspot.search_contact("test.user@example.com")
        
        if contact:
            print("✅ Contact FOUND!")
            print(f"Contact ID: {contact.get('id')}")
            print(f"Properties: {contact.get('properties', {})}")
        else:
            print("❌ Contact NOT FOUND")
            print("The contact doesn't exist in HubSpot yet")
            
        # Test 2: Create a test contact
        print("\n📝 Creating test contact...")
        result = hubspot.create_contact({
            "email": "debug.test@example.com",
            "firstname": "Debug",
            "lastname": "Test"
        })
        print(f"Create result: {result}")
        
        # Test 3: Search for the new contact
        print("\n🔍 Searching for new contact...")
        new_contact = hubspot.search_contact("debug.test@example.com")
        if new_contact:
            print("✅ New contact FOUND!")
            print(f"New Contact ID: {new_contact.get('id')}")
        else:
            print("❌ New contact NOT FOUND - There might be an API issue")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_hubspot()
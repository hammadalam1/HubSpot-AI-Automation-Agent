#!/usr/bin/env python3
"""
Test/Demo version that shows how the system works
"""

def test_mode():
    print("🧪 HubSpot AI Agent - DEMO MODE")
    print("=" * 40)
    print("This shows how the system would work with real API keys.\n")
    
    examples = [
        "Create a new contact for john@example.com with first name John and last name Doe",
        "Update phone number to 555-1234 for john@example.com",
        "Find contact with email john@example.com", 
        "Create a new deal for Acme Corp with amount $5000"
    ]
    
    print("📝 Example workflows:")
    for i, example in enumerate(examples, 1):
        print(f"\n{i}. User query: '{example}'")
        print("   System workflow:")
        print("   └─ Global Orchestrator → Determines action type")
        print("      └─ HubSpot Agent → Performs CRM operation") 
        print("      └─ Email Agent → Sends confirmation")
    
    print(f"\n🔧 To use the real system:")
    print("1. Run: pip install -r requirements.txt")
    print("2. Run: python setup.py") 
    print("3. Add your real API keys")
    print("4. Run: python main.py")
    
    print(f"\n🔑 Required API keys:")
    print("- OpenAI API key (for AI processing)")
    print("- HubSpot API key (for CRM operations)") 
    print("- Email SMTP credentials (for notifications)")

if __name__ == "__main__":
    test_mode()
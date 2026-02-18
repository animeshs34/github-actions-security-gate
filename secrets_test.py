# INTENTIONAL SECRETS: These are for testing secret scanning detection.
# In a real app, these should NEVER be committed to source control.
STRIPE_API_KEY = "sk_test_this_is_a_very_fake_key_12345" 
AWS_ACCESS_KEY = "AKIA_FAKE_KEY_123456789"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def connect_to_aws():
    print(f"Connecting with {AWS_ACCESS_KEY}")

import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Find all matches using re.findall()
    emails = re.findall(email_pattern, text)

    return emails


text = """
Hello, you can reach me at user@example.com or support@company.com.
Feel free to contact us for any queries.
"""

result = extract_emails(text)

print("Extracted email addresses:")
for email in result:
    print(email)

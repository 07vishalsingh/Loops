'''
You are given a list of email addresses. Write a Python function to find and return the domain names of all the email addresses in the list. The domain name of an email address is the part after the "@" symbol. Return the domain names as a set to avoid duplicates.
'''

def extract_domain(emails):
    domains = set()
    for email in emails:
        # Split the email address at the "@" symbol
        parts = email.split("@")
        if len(parts) == 2:
            # Add the domain name to the set
            domains.add(parts[1])
    return domains

# Example usage
email_list = [
    "user1@example.com",
    "user2@gmail.com",
    "user3@yahoo.com",
    "user4@example.com",
    "user5@hotmail.com"
]
print("Domain Names:", extract_domain(email_list))  # Output: {'example.com', 'gmail.com', 'yahoo.com', 'hotmail.com'}

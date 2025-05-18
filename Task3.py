import re

# (a) Read text from a file
with open('sample_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# (b) Extract email addresses
# Matches typical email formats
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)

# Extract phone numbers
# Matches formats like: 123-456-7890, (123) 456-7890, 1234567890, +1 123 456 7890
phone_pattern = r'(\+?\d{1,3}[\s-]?)?(\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{4}'
phones = re.findall(phone_pattern, text)
# re.findall with groups returns tuples, we join the matches into full strings
phones = [''.join(match) for match in phones if ''.join(match).strip() != '']

# (c) Replace all dates with the format [DATE]
# Match formats like: dd-mm-yyyy or yyyy/mm/dd
date_pattern = r'(\d{2}-\d{2}-\d{4}|\d{4}/\d{2}/\d{2})'
text_with_dates_replaced = re.sub(date_pattern, '2025/05/18', text)

# Output the results
print("Extracted Emails:")
for email in emails:
    print(f" - {email}")

print("\nExtracted Phone Numbers:")
for phone in phones:
    print(f" - {phone}")

print("\nText with Dates Replaced:\n")
print(text_with_dates_replaced)

# Optionally, write the updated text to a new file
with open('processed_text.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(text_with_dates_replaced)

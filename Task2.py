import re

# (a) Valid Email Addresses
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email_tests = [
    "test@example.com",
    "john.doe99@sub.domain.org",
    "invalid_email@.com",
    "@no-local.com"
]

print("Email Address Matches:")
for email in email_tests:
    if re.match(email_pattern, email):
        print(f"✅ {email}")
    else:
        print(f"❌ {email}")
print()

# (b) IP Addresses (IPv4)
ip_pattern = r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$'
ip_tests = [
    "192.168.0.1",
    "255.255.255.255",
    "300.1.1.1",
    "10.10.10"
]

print("IP Address Matches:")
for ip in ip_tests:
    if re.match(ip_pattern, ip):
        print(f"✅ {ip}")
    else:
        print(f"❌ {ip}")
print()

# (c) Dates in multiple formats: dd-mm-yyyy or yyyy/mm/dd
date_pattern = r'^(\d{2}-\d{2}-\d{4}|\d{4}/\d{2}/\d{2})$'
date_tests = [
    "31-12-2023",
    "2023/01/01",
    "01/01/2023",
    "2023-12-31"
]

print("Date Format Matches:")
for date in date_tests:
    if re.match(date_pattern, date):
        print(f"✅ {date}")
    else:
        print(f"❌ {date}")
print()

# (d) URLs
url_pattern = r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/\S*)?$'
url_tests = [
    "https://example.com",
    "http://www.example.org/foo",
    "example.com",
    "htp://wrong.com"
]

print("URL Matches:")
for url in url_tests:
    if re.match(url_pattern, url):
        print(f"✅ {url}")
    else:
        print(f"❌ {url}")

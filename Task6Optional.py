import re
import time


# 1. Flawed Pattern Example

# This pattern causes catastrophic backtracking on long input of "a"s followed by "b"
flawed_pattern = re.compile(r"(a|aa)+")  # Inefficient due to multiple overlapping paths
test_string = "a" * 25 + "b"

# Measure performance time of flawed pattern
start_time = time.time()
match = flawed_pattern.match(test_string)
end_time = time.time()

print("Flawed Pattern:")
print("Matched:", bool(match))
print("Time Taken:", round(end_time - start_time, 4), "seconds\n")



# 2. Refactored Pattern
# Simplified and optimized pattern that avoids overlapping sub-patterns
optimized_pattern = re.compile(r"a+")

# Measure performance time of optimized pattern
start_time = time.time()
match = optimized_pattern.match(test_string)
end_time = time.time()

print("Optimized Pattern:")
print("Matched:", bool(match))
print("Time Taken:", round(end_time - start_time, 4), "seconds\n")


# -----------------------------
# 3. Example of Clear and Efficient Regex
# -----------------------------
# Extract valid IP addresses using a clear and bounded pattern
ip_pattern = re.compile(
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
)
sample_text = "Ping 192.168.0.1 and 10.0.0.256 and 172.16.254.3"

ips = ip_pattern.findall(sample_text)
print("Extracted IPs:", ips)


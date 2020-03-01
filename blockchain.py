import requests

url = 'http://localhost:9090/api/enrolluser'
query = "{\n \"userId\": \"Vidit\",\n \"secret\": \"123\",\n \"role\": \"CARMAKER\"\n}"
res = requests.post(url, data=query)
print(res.text)
import requests

res = requests.post("http://localhost:8000/chat", json={
    "query": "What are our engineering principles according to the handbook and what is the current year and 8+5?, "
})
print(res.json())

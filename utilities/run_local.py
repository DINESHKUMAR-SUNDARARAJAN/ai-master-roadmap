import requests

res = requests.post("http://localhost:8000/chat", json={
    "user_id":"dinesh", "query": "What is our engineering principle?"
})
print(res.json())

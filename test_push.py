import json
import requests
import urllib.request

def test_push():
    url = "http://127.0.0.1:8091/push"
    payload = {"message": "test message"}
    headers = {'Content-Type': 'application/json'}

    req = urllib.request.Request(url=url, data=json.dumps(payload).encode(), headers=headers, method="POST")
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body)

if __name__ == "__main__":
    test_push()

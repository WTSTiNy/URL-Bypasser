import requests, os

def bypass():
  os.system("clear")
  print("[1] Bypass One URL") 
  print("[2] Bypass Multiple URLs")
  print("[3] Exit")
  o = input("[+] Enter > ")
  if o == "1":
    url = input("[+] Enter URL to Bypass: ")
    payload = {"url": url}
    url_bypass = requests.post("https://api.bypass.vip/", data=payload)
    bypassed = url_bypass.json()
    print("Bypassed URL: " + bypassed["destination"])
  elif o == "2":
    print("[!] Example File Input:")
    print("[+] Enter The File with URLs: urls.txt")
    urls_file = input("[+] Enter The File with URLs: ")
    urls = open(f"{str(urls_file)}", "r")
    for i in urls:
      url_bypass = {"url": i}
      bypass = requests.post("https://api.bypass.vip/", data=url_bypass)
      bypassed = bypass.json()
      try:
        open("bypassed.txt", "x")
      except FileExistsError:
        pass
      bypassed_url = open("bypassed.txt", "a")
      try:
        print("[+] Bypassed URL")
        bypassed_url.write(bypassed["destination"] + "\n")
      except KeyError:
        print("[-] Invalid URL Found")
        pass
  elif o == "3":
    os.system("exit")


if __name__ == "__main__":
  bypass()

# Original: https://github.com/bypass-vip/bypass.vip/blob/main/python-requests.py

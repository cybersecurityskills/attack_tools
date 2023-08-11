import requests

uris = ["/admin","/test","/admin1","/drupal","/CHANGELOG.txt","/test/c99.php","/","/administrator","/webmin","/finance","/backup","/production","/uat","/prod","/logs","/robots.txt"]
target = "http://10.0.1.2"

for uri in uris:
   url = target+uri
   res = requests.get(url)
   sc = res.status_code
   if int(sc) >= 400:
      print("[%s] returned -> \x1b[31m%s\x1b[0m" % (uri,sc))
   elif int(sc) >= 200:
      print("[%s] returned -> \x1b[32m%s\x1b[0m" % (uri,sc))

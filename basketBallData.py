import urllib.request
x = urllib.request.urlopen('https://www.basketball-reference.com/')
print(x.read())
print(status_code(x))
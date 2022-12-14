import requests

def check_xss(url):
  payloads = ['<script>alert(1)</script>', '"><script>alert(1)</script>']
  for payload in payloads:
    r = requests.get(url, params={'q': payload})
    if payload in r.text:
      return True
  return False

if __name__ == '__main__':
  url = input('Enter the URL to check: ')
  if check_xss(url):
    print('XSS vulnerability found!')
  else:
    print('No XSS vulnerability found.')
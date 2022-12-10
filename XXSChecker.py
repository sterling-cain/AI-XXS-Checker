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

def check_sqli(url):
  payloads = ["' OR 1=1--", '" OR 1=1--', "') OR 1=1--", '") OR 1=1--']
  for payload in payloads:
    r = requests.get(url, params={'q': payload})
    if 'error' not in r.text.lower() and 'syntax' not in r.text.lower():
      return (True, payload)

  return (False, '')

def check_bac(url):
  payloads = ['admin', 'administrator', 'root']
  for payload in payloads:
    r = requests.get(url, params={'username': payload, 'password': payload})
    if 'logged in' in r.text.lower() or 'access granted' in r.text.lower():
      return (True, payload)

  return (False, '')

if __name__ == '__main__':
  while True:
    url = input('Enter the URL to check (or enter "q" to quit): ')
    if url == 'q':
      break

    xss_result = check_xss(url)
    if xss_result[0]:
      print('XSS vulnerability found! Payload:', xss_result[1])

    sqli_result = check_sqli(url)
    if sqli_result[0]:
      print('SQL injection vulnerability found! Payload:', sqli_result[1])

    bac_result = check_bac(url)
    if bac_result[0]:
      print('Broken access control vulnerability found! Payload:', bac_result[1])

    if not xss_result[0] and not sqli_result[0] and not bac_result[0]:
      print('No vulnerabilities found.')

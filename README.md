# ISPManager API Interface

## About
ISPManager is web server control panel. It allows you to manage your entire web-server through a user friendly and comprehensive multi-language web interface. With the click of a mouse you can manage users, hosting packages, mail boxes, databases and much more from one centralized location in a simple and intuitive way.

URL: http://ispsystem.com/en/

## API documentation
http://en.ispdoc.com/index.php/ISPmanager_API

## Examples:

### Authorization:

```python
from ispmgr import Auth

url = "https://example.com/manager/ispmgr"
username = "your-username"
password = "your-password"

auth = Auth(url, username, password)

#logout
auth.logout()
```

### List www domains:

```python
from ispmgr import WWWDomain

d = WWWDomain(auth)

# list all domains
# returns list of dicts
domains = d.list()
for domain in domains:
    print domain['ip'], domain['name']

# list specific domain details
# returns dict
domain = d.list('example.com')

for key,value in domain.items():
    print "%s: %s" % (key,value)
```

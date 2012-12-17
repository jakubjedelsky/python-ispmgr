# ISPManager API Interface for Server Administrator

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

### WWW domains:

Use class WWWDomain.
```python
from ispmgr import WWWDomain

www = WWWDomain(auth)
```

#### add www domain

```python
www.add(
    domain='example.com',
    owner='bigboss',
    admin='webmaster@example.com.
    ip='192.168.0.23')
```

#### list domains
```python
# returns list of dicts
domains = www.list()
for domain in domains:
    print domain['ip'], domain['name']

# list specific domain details
# returns dict
domain = www.list('example.com')

for key,value in domain.items():
    print "%s: %s" % (key,value)
```

#### delete domain(s)
```python
# delete some domains
www.delete(['example.com', 'google.com'])
```

import urllib, urllib2
import json

class Auth(object):
    """Authorize user against ISPManager instance."""

    def __init__(self, url, username, password,):
        self.url = url
        self.sessid = self.authorize(username, password)

    def authorize(self, username, password):
        params = urllib.urlencode({
            'func': 'auth',
            'out': 'json',
            'username': username,
            'password': password,
        })
        data = urllib2.urlopen("%s?%s" % (self.url, params))
        out = json.load(data)

        if out.has_key('authfail'):
            raise RuntimeError('Authorization error, check your credentials')

        return out['auth']

    def logout(self):
        params = urllib.urlencode({
            'auth' : self.sessid,
            'func' : 'session.delete',
            'out' : 'json',
            'elid' : self.sessid,
        })

        data = urllib2.urlopen('%s?%s' % (self.url, params))
        out = json.load(data)

        if out["result"] == "OK":
            return True
        else:
            raise RuntimeError('Logout failed!')

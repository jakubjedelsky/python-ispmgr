import urllib
import urllib2
import json
import api

class WWWDomain(api.API):

    def __init__(self, auth_handler):
        self.url = auth_handler.url
        self.sessid = auth_handler.sessid
        self.func = 'wwwdomain.edit'
        self.out = 'json'
        self.params = {
            'auth' : self.sessid,
            'out'  : self.out,
            'func' : self.func,
        }

    def list(self, domains=None):
        if domains:
            raise NotImplementedError

        self.params['func'] = 'wwwdomain'
        data = self.process_api(self.url, self.params)
        out = json.load(data)
        return out['elem']


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

    def list(self, domain=None):
        """List all www domains. If domains is used, list details about this one."""
        if domain:
            self.params['elid'] = domain
        else:
            self.params['func'] = 'wwwdomain'
        data = self.process_api(self.url, self.params)
        out = json.load(data)
        try:
            return out['elem']
        except KeyError:
            return out

    def add(self, domain,  owner, admin, ip, **kwargs):
        """Add a new wwwdomain to configuration. If a DNS server is configurated, API adds
        domain there too."""
        self.params['sok']    = 'yes'
        self.params['domain'] = domain
        self.params['owner']  = owner
        self.params['admin']  = admin
        self.params['ip']     = ip
        for key in kwargs:
            self.params[key] = kwargs[key]

        data = self.process_api(self.url, self.params)
        out = json.load(data)
        return out


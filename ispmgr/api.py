import urllib
import urllib2

class API(object):
    """Common class for other, specific, classes."""

    def process_api(self, url, params):
        return urllib2.urlopen("%s?%s" % (url, urllib.urlencode(params)))

import pyshorteners as ps

def shorten(url=None):
    type_tiny = ps.Shortener()
    short_url = type_tiny.tinyurl.short(url)
    print("The shortened url is : " + short_url)
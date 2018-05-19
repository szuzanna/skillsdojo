import pycurl
import certifi

url = 'https://eu.udacity.com/courses/all'

with open('out.html', 'wb') as writer:
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, writer)
    c.setopt(c.CAINFO, certifi.where())
    c.perform()
    c.close()
#!/usr/bin/env python

import pycurl

c = pycurl.Curl()
c.setopt(c.URL, 'https://www.coursera.org/featured/top_specializations_locale_en_os_web')
with open('pc.out', 'wb') as writer:
    c.setopt(c.WRITEDATA, writer)
    c.perform()
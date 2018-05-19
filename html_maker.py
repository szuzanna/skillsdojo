import pycurl
import certifi


class HtmlMaker:
    def __init__(self, address, file):
        self.site_url = address
        self.destination_file_name = file

    def copy_to_html(self):
        with open(self.destination_file_name, 'wb') as writer:
            c = pycurl.Curl()
            c.setopt(c.URL, self.site_url)
            c.setopt(c.WRITEDATA, writer)
            c.setopt(c.CAINFO, certifi.where())
            c.perform()
            c.close()


test_case = HtmlMaker('https://google.com', 'out.html')
test_case.copy_to_html()

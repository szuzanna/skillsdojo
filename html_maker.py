from urllib.parse import urlparse
import pycurl
import certifi

class HtmlMaker:
    def __init__(self, address, file):
        self.site_url = address
        self.destination_file_name = file
        self.base = self.make_it_shorter()
        self.liks_directory = self.make_courses_direcotry()
        
#
#      ____________
#     /-----------\
#    |_____________|
#   [-----[(O)]-[(o)]
#    |          \ |
#    |         o_\
#    |    ________|
#     \__________/
#       |      |
#--------\_____/---------
#
░░░░░░░░░░░░░▄▄▀▀▀▀▀▀▄▄
░░░░░░░░░░▄▄▀▄▄▄█████▄▄▀▄
░░░░░░░░▄█▀▒▀▀▀█████████▄█▄
░░░░░░▄██▒▒▒▒▒▒▒▒▀▒▀▒▀▄▒▀▒▀▄
░░░░▄██▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▄
░░░░██▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▌
░░░▐██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐█
░▄▄███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
▐▒▄▀██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▌
▌▒▒▌▒▀▒▒▒▒▒▒▄▀▀▄▄▒▒▒▒▒▒▒▒▒▒▒▒█▌
▐▒▀▒▌▒▒▒▒▒▒▒▄▄▄▄▒▒▒▒▒▒▒▀▀▀▀▄▒▐
░█▒▒▌▒▒▒▒▒▒▒▒▀▀▒▀▒▒▐▒▄▀██▀▒▒▒▌
░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▒▒█
░░░▀▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▒▄▀
░░░▐▒▒▒▒▒▒▒▒▒▄▀▐▒▒▒▒▒▐▒▒▒▒▄▀
░░▄▌▒▒▒▒▒▒▒▄▀▒▒▒▀▄▄▒▒▒▌▒▒▒▐▀▀▀▄▄▄
▄▀░▀▄▒▒▒▒▒▒▒▒▀▀▄▄▄▒▄▄▀▌▒▒▒▌░░░░░░
▐▌░░░▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▀░░░░░░░
░█░░░░░▀▄▄▒▒▒▒▒▒▒▒▒▒▒▒▄▀░█░░░░░░░
░░█░░░░░░░▀▄▄▄▒▒▒▒▒▒▄▀░░░░█░░░░░░
░░░█░░░░░░░░░▌▀▀▀▀▀▀▐░░░░░▐▌░░░░░
        
        

    def copy_to_html(self):
        with open(self.destination_file_name, 'wb') as writer:
            c = pycurl.Curl()
            c.setopt(c.URL, self.site_url)
            c.setopt(c.WRITEDATA, writer)
            c.setopt(c.CAINFO, certifi.where())
            c.perform()
            c.close()

    def make_it_shorter(self):
        tmp = urlparse(self.site_url)
        return tmp.scheme + '://' + tmp.netloc

    def make_courses_direcotry(self):
        text = open(self.destination_file_name).read()
        text = text.split("<div")
        linki = {}
        for a in text:
            if (a.__contains__("class=\"search-result__title\"><a href=")):
                # print(a)
                link = a[39:]
                nazwa = link
                link = link[:link.index("\"")]
                nazwa = nazwa[nazwa.index(">") + 1:nazwa.index("<")]
                linki[nazwa] = self.base + link
        return linki

    def __str__(self):
        return 'hyhy kursiki'


test_case = HtmlMaker('https://www.pluralsight.com/browse/it-ops', 'out.html')
test_case.copy_to_html()
print(test_case.base)
print(test_case.liks_directory)
print(test_case)

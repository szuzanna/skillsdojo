import re
text = open('t.txt').read()
#print(text)
#result = re.findall(r'([^\w]|^)(\w{3})([^\w]|$)', "I like my cat, but my cat does't like me.")
text = text.split("<div")
linki = {}
for a in text:
    if (a.__contains__("class=\"search-result__title\"><a href=")):
        print(a)
        link = a[39:]
        nazwa = link
        print(nazwa)
        link=link[:link.index("\"")]
        print(link)
        nazwa = nazwa[nazwa.index(">")+1:nazwa.index("<")]
        print(nazwa)
        linki[nazwa]=link

print(linki)
# to działa tylko dla pluralsight.com

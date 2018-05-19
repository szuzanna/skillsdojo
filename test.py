import re
text = open('t.txt').read()
#print(text)
#result = re.findall(r'([^\w]|^)(\w{3})([^\w]|$)', "I like my cat, but my cat does't like me.")



output = re.findall(r'(?s)item-image"><img alt="(.*?)" src="', text, flags=re.IGNORECASE)
if output is not None:
    #output = output.group(0)
    #assert isinstance(output, object)
    print(output)
print(len(output))
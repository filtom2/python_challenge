import re
import urllib.request


value = '12345'

while True:

    link = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={value}"

    open_link = urllib.request.urlopen(link)
    contents = str(open_link.read())
    print(contents)
    
    show_order = re.findall("[0-9]",contents)
    value = ''.join(show_order)




'''
f'sasfa{contents:05}'
'''
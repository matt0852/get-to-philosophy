import requests
import wiki_parser

title = 'soap'
# url = 'https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvslots=*&rvprop=content&format=json&formatversion=2&titles='
# content = data['query']['pages'][0]['revisions'][0]['slots']['main']['content']
url = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&prop=wikitext&page='

data = requests.get(url + title).json()
content = data['parse']['wikitext']['*']

# remove curly brackets
content = wiki_parser.remove_brackets(content)

# find all links enclosed in [[]]
content = wiki_parser.find_links(content)

# find first non-file link
found = False
index = 0
valid_link = ''
while not found:
    link = content[index][0:5]
    if link != 'File:':
        found = True
        valid_link = content[index]
    else:
        index += 1

print(valid_link)

# modify the first link
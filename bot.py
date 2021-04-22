from wiki_parser import get_all_links
from link_crawler import generate_links

title = 'Philosophy'

for _ in range(20):
    output = generate_links(title)[0]
    print(output)
    title = output
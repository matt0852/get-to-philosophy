from wiki_parser import get_all_links
import link_crawler

title = 'Outline_of_philosophy'
links = get_all_links(title)
links = link_crawler.find_valid(links)
links = link_crawler.first_word(links, '|')
links = link_crawler.first_word(links, '#')
links = link_crawler.add_underscores(links)

print(links)
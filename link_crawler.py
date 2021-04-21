from wiki_parser import get_all_links

# method to filter out links that are files or pictures
def find_valid(links):
    output = []
    for link in links:
        if link.find(':') == -1:
            output.append(link)
    return(output)

# method to grab only the first word 'Government' from 'Government|governance' or 'History_of_China#Ancient_China'
def first_word(links, sep):
    output = []
    for link in links:
        index = link.find(sep)
        if index != -1:
            newlink = link[0:index]
            output.append(newlink)
        else:
            output.append(link)
    return(output)

# method to add underscores
def add_underscores(links):
    output = []
    for link in links:
        newlink = link.replace(' ', '_')
        output.append(newlink)
    return(output)

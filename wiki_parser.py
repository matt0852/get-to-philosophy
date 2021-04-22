import requests


def grab_content(title):
    url = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&prop=wikitext&page='
    data = requests.get(url + title).json()
    content = data['parse']['wikitext']['*']
    return(content)


def remove_brackets(string):
    to_add = True
    letter_counter = 2
    open_bracket_counter = 0
    output = ''
    for c in enumerate(string):
        try:
            first_char = c[1]
            next_char = string[c[0] + 1]
        except:
            first_char = c[1]
            next_char = ''

        letter_counter += 1
        # if the char is '{' and the subsequent char also '{'
        if first_char == '{' and next_char == '{':
            if open_bracket_counter == 0:
                to_add = False
            open_bracket_counter += 1

        # if the char is '}' and subsequent char also '}'
        if first_char == '}' and next_char == '}':
            if open_bracket_counter == 1:
                to_add = True
                letter_counter = 0
            open_bracket_counter -= 1

        if to_add == True and letter_counter >= 2:
            output += c[1]

    return(output)


def find_links(string):
    inside_rbracket = False # check if currently we are inside ()
    inside_bracket = False # check if currently we are inside []
    to_add = False # decides whether to add to output array
    open_rbracket_counter = 0 # counts number of open ()
    open_bracket_counter = 0 # counts number of open []
    output = [''] # output array
    index = 0 # index for output array
    skip = False
    for c in enumerate(string):
        try:
            first_char = c[1]
            next_char = string[c[0] + 1]
        except:
            first_char = c[1]
            next_char = ''
        
        # first check if the link is surrounded with ()
        if first_char == '(' and inside_bracket == False:
            if open_rbracket_counter == 0:
                inside_rbracket = True
            open_rbracket_counter += 1
        
        elif first_char == ')' and inside_bracket == False:
            if open_rbracket_counter == 1:
                inside_rbracket = False
            open_rbracket_counter -= 1
        
        elif inside_rbracket == False:
            # skip is so that '[[[[' is recognised as 2 instances of '[[' instead of 3
            if skip == False:
                if first_char == '[' and next_char == '[':
                    inside_bracket = True
                    if open_bracket_counter == 0:
                        to_add = True
                    open_bracket_counter += 1
                    skip = True

                if first_char == ']' and next_char == ']':
                    inside_bracket = False
                    if open_bracket_counter == 1:
                        to_add = False
                        output[index] = output[index][1:]
                        index += 1
                        output.append('')
                    open_bracket_counter -= 1
                    skip = True

                if to_add == True:
                    output[index] += c[1]

            else:
                skip = False
        
    return(output)


def get_all_links(title):
    content = grab_content(title)
    parsed = remove_brackets(content)
    links = find_links(parsed)
    return(links)

def remove_brackets(string):
    to_add = True
    letter_counter = 2
    open_bracket_counter = 0
    output = ''
    for c in enumerate(string):
        letter_counter += 1
        # if the char is '{' and the subsequent char also '{'
        if c[1] == '{' and string[c[0] + 1] == '{':
            if open_bracket_counter == 0:
                to_add = False
            open_bracket_counter += 1

        # if the char is '}' and subsequent char also '}'
        if c[1] == '}' and string[c[0] + 1] == '}':
            if open_bracket_counter == 1:
                to_add = True
                letter_counter = 0
            open_bracket_counter -= 1

        if to_add == True and letter_counter >= 2:
            output += c[1]

    return(output)


def find_links(string):
    to_add = False
    open_bracket_counter = 0
    output = ['']
    index = 0
    for c in enumerate(string):
        try:
            first_char = c[1]
            next_char = string[c[0] + 1]
        except:
            first_char = c[1]
            next_char = ''

        if first_char == '[' and next_char == '[':
            if open_bracket_counter == 0:
                to_add = True
            open_bracket_counter += 1

        if first_char == ']' and next_char == ']':
            if open_bracket_counter == 1:
                to_add = False
                output[index] = output[index][2:]
                index += 1
                output.append('')
            open_bracket_counter -= 1

        if to_add == True:
            output[index] += c[1]

    return(output)
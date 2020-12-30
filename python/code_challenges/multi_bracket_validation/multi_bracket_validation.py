def multi_bracket_validation(input_string):
    brackets = ['()', '{}', '[]']
    while any(x in input_string for x in brackets):
        for y in brackets:
            input_string = input_string.replace(y, '')
    return not input_string

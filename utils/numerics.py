def is_number(x):
    return x.isdigit()

def is_valid_char(char):
    return(char in ['*', '-', '+', '/', '^', '(', ')'] or is_number(char)) 
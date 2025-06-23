def functional_filter(f, s: str, to: str = '') -> str: 
    result = ''
    for iter in s:
        result += to if f(iter) else iter
    return result

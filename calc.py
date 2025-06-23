from utils import is_valid_char, functional_filter

class Calculator: 
    def __init__(self): 
        self.expression = ""
        self.result = 0
        self.tokens = []
    
    def calculate(self, expression: str):
        self.expression = functional_filter(lambda x: not is_valid_char(x), expression) + '#'
        self.expression = functional_filter(lambda x: x == '^', expression, '**')
        self.result = 0
        # Add history later

        self.result = eval(self.expression)

    def get_result(self):
        return self.result

if __name__ == '__main__':
    s = input('Enter the expression (every invalid character will be ignored): ')
    calc = Calculator()
    calc.calculate(s)
    print('The result is: ', calc.get_result()) 
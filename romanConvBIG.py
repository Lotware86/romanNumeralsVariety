#  Author: Bosco Lo, dated 30 September 2018 4:45 AM
#  Program Description: Roman Numeral Converter © ™. Expanded from basic converter that handles only numbers 1-3999
#  included Try-Except error handling
#  09 May 2020 - replaced is not operator with == operator with
#    turned Line 46 accordingly to read as concatenation of string
#   Line 46 ---- if char is not '(' and char is not ')':
#    and
#   Line 76 ---- if char is '(' or char is ')':

num_Tuple = [(1000000, '((M))'), (900000, '((C))'), (500000, '((D))'), (400000, '((CD))'), (100000, '(C)'),
             (90000, '(XC)'), (50000, '(L)'), (40000, '(XL)'), (10000, '(X)'), (9000, '(IX)'), (5000, '(V)'),
             (4000, '(IV)'), (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
             (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


#  extended the tuple list beyond 1,000 so that the program is able to handle values from 4,000 up to 3,999,999
class NumberConverter:
    resultNum = 0

    def to_roman(self, num):
        roman = ''
        try:
            num = int(num)
            if num == 0:
                print('\nRoman Numerals has no zero')
                quit()
            elif num < 0:
                print('\nRoman Numerals have no Negative numbers')
                if num == -1:
                    print('\n-1 is used to quit. Exiting program...')
                quit()
        except ValueError:
            if num.isalpha():
                print("\nYou should have entered an integer! We are converting numbers to roman numerals! Exiting...")
            elif num is not int:
                print('\nCannot convert from values with precision or floating points, only enter integers. Exiting...')
                quit()

        while num > 0:
            for key, val in num_Tuple:
                while num >= key:
                    #  to represent number that is 4000 or more, so that it will add a bar on topside of the letter
                    if key >= 4000:
                        temp_list = list(val)
                        for char in temp_list:
                            if char != str('(') and char != str(')'):
                                char += u'\u0304'
                            roman += char
                            # print(roman)
                        num -= key
                    #  end of additional script for displaying representation for numbers 4000 or more
                    else:
                        roman += val
                        num -= key
        return roman

    def from_roman(self, r):
        index = 0
        # print(r[index:index + len(r)])
        r = (r.encode('ascii', 'ignore')).decode('utf-8')
        for value, symbol in num_Tuple:
            symbolLength = len(symbol)
            while r[index:index + symbolLength] == symbol:
                if index > symbolLength - 1:
                    print('+')
                self.resultNum += value
                index += symbolLength
                # print(value, symbol, index)
                print(value, symbol)
        print('=')
        return self.resultNum

    def print_roman(self, r):
        r = convert.to_roman(r)
        for char in r:
            if char == '(' or char == ')':
                r = r.replace('(', '')
                r = r.replace(')', '')
        return r


convert = NumberConverter()
numInput = input('Enter a number to be converted to Roman Numerals, -1 to quit: ')
while numInput != -1:
    print('\nNumber to Roman Numeral representation is:', convert.print_roman(numInput))
    print(convert.from_roman(convert.to_roman(numInput)))
    print('\n')
    convert = NumberConverter()  # "re-instantiation", prevents incrementing from previous number
    numInput = input('Enter a number to be converted to Roman Numerals, -1 to quit: ')

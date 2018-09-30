#  Author: Bosco Lo, dated 24 September 2018 11:07 PM
#  Program Description: Roman Numeral Converter © ™

num_Tuple = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
             (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


class NumberConverter:

	resultNum = 0

	def convertToRoman(self, num):
		roman = ''
		while num > 0:
			for key, val in num_Tuple:
				while num >= key:
					roman += val
					num -= key
		return roman

	def convertFromRoman(self, r):
		index = 0
		for value, symbol in num_Tuple:
			symbolLength = len(symbol)
			while r[index:index + symbolLength] == symbol:
				self.resultNum += value
				index += symbolLength
				print(value, symbol, index)
		return self.resultNum


conv = NumberConverter()
numInput = int(input('Enter a number to be converted to Roman Numerals: '))
print('Number to Roman Numeral representation is:', conv.convertToRoman(numInput))
print('The number from Roman:', conv.convertFromRoman(conv.convertToRoman(numInput)))

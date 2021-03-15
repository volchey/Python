# Python program to implement Morse Code Translator

'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'1011', 'B':'11010101',
					'C':'110101101', 'D':'110101', 'E':'1',
					'F':'10101101', 'G':'1101101', 'H':'1010101',
					'I':'101', 'J':'1011011011', 'K':'1101011',
					'L':'10110101', 'M':'11011', 'N':'1101',
					'O':'11011011', 'P':'101101101', 'Q':'1101101011',
					'R':'101101', 'S':'10101', 'T':'11',
					'U':'101011', 'V':'10101011', 'W':'1011011',
					'X':'110101011', 'Y':'1101011011', 'Z':'110110101',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':

			# Looks up the dictionary and adds the
			# correspponding morse code
			# along with a space to separate
			# morse codes for different characters
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			# 1 space indicates different characters
			# and 2 indicates different words
			cipher += ' '

	return cipher

# Function to decrypt the string
# from morse to english
def decrypt(message):

	# extra space added at the end to access the
	# last morse code
	message += ' '

	decipher = ''
	citext = ''
	for letter in message:

		# checks for space
		if (letter != ' '):

			# counter to keep track of space
			i = 0

			# storing morse code of a single character
			citext += letter

		# in case of space
		else:
			# if i = 1 that indicates a new character
			i += 1

			# if i = 2 that indicates a new word
			if i == 2 :

				# adding space to separate words
				decipher += ' '
			else:

				# accessing the keys using their values (reverse of encryption)
				# print(decipher)
				for char, code in MORSE_CODE_DICT.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
					if code == citext:
						decipher += char
				# decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
				# .values()).index(citext)]
				citext = ''

	return decipher

# Hard-coded driver function to run the program
def main():
	message = "DO NOT GO GENTLE INTO THAT GOOD"

	result = encrypt(message.upper())
	print (result)

	f = open("Inputcode.dat", "r")
	text = f.read()
	text = text.replace('000000', '  ')
	text = text.replace('00', ' ')
	text = text.replace('\n', ' ')
	print(text)

	# message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "
	# result = decrypt(text)
	# print (result)

# Executes the main function
if __name__ == '__main__':
	main()

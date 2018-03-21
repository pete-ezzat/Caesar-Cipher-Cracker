def letter_converter(mode, input_char):
	abc123 = "abcdefghijklmnopqrstuvwxyz"
	
	# Letter to Code
	if mode == 1	: 
		found = abc123.find(input_char)
		if found > -1: return found
		else		 : return 23
		
	# Code to Letter
	elif mode == 2	: return abc123[int(input_char)]

###-----------------------------------------------------------------

def crack(cipher):
	plaintext = ''
	
	for key in range(1, 26):
		plaintext += '[' + str(key) + '] '
		for char in cipher:
			ascii_letter = letter_converter(1, char)
			ascii_letter = (ascii_letter + key) % 26
			plaintext += letter_converter(2, ascii_letter)
		plaintext += '\n'

	print(plaintext)

###-----------------------------------------------------------------

while True:
	cipher = input("Cipher: ").lower()
	crack(cipher)

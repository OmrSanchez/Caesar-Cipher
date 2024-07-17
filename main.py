from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(t, s, d):
	end_text = ""
	if d == "decode":
		s *= -1
	for char in t:
		if char in alphabet:
			index = alphabet.index(char)
			new_index = index + (s)
			end_text += alphabet[new_index]
		else:
			end_text += char
	print(f"The {d}d text is: {end_text}\n")


run_again = False
while not run_again:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'close' to end:\n").lower()
	en = True
	if direction == "close":
		print("Goodbye!")
		break
	while en:
		if direction == "encode":
			en = False
		elif direction == "decode":
			en = False
		elif direction == "close":
			print("Goodbye!")
			en = False
		else:
			direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'close' to end:\n").lower()
	if direction == "close":
		print("Goodbye!")
		break
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	while shift >= 26:
		shift = int(
			input("Value is too high. Select a value in range(0 - 25):\n"))
	caesar(t=text, s=shift, d=direction)
	run_again = input(
		"Would you like to run the program again? Type 'yes' or 'no' \n")
	if run_again == "yes":
		run_again = False
	else:
		run_again = True
		print("Goodbye!")

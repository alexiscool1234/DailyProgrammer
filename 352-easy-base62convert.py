# CHALLENGE #352 Easy
# https://www.reddit.com/r/dailyprogrammer/comments/7yyt8e/20180220_challenge_352_easy_making_imgurstyle/

def main():
	input = int(raw_input("Please enter the number to convert: "))
	print base62convert(input)

def base62convert(input):
	alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	output = ''
	while input > 0:
		base62number = input % 62
		base62character = alphabet[base62number]
		output += base62character
		input = input / 62
	return output
		
main()

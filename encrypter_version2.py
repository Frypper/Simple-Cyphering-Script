#cypher_script

ALPHABET_CHARS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
CAPITAL_APHABET = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
CYPHER_CHARS = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","m","n","b","v","c","x","z"]

					#Cypher Part of the script
def cypher_message(users_input):

#Defines two variables, The one that we are gonna use for the result and the list
	resulting_message = ""
	
#Creates loop that's gonna last as much as the lenght of the whole message
#And is gonna replace each letter with a letter in the chyphered list
	for j in range(len(users_input)):


		if users_input[j] in ALPHABET_CHARS:
			obj = users_input[j]
			resulting_message += CYPHER_CHARS[ALPHABET_CHARS.index(obj)]

		elif users_input[j] in CAPITAL_APHABET:
			obj = users_input[j]
			resulting_message += CYPHER_CHARS[CAPITAL_APHABET.index(obj)]

		else:
			resulting_message += " "

	print(resulting_message)



					#Decyphering part of the script
def decypher_message(users_input):

#Defines two variables, The one that we are gonna use for the result and the list
	resulting_message = ""
	
#Creates loop that's gonna last as much as the lenght of the whole message
	for j in range(len(users_input)):

		if users_input[j] in CYPHER_CHARS:

			obj = CYPHER_CHARS.index(users_input[j])
			resulting_message += ALPHABET_CHARS[obj]

		else:
			resulting_message += " "

#prints out the result
	print(resulting_message)


					# getInput Part of the program

def get_information():

	print("Encritper Version 2.0\n")
	usr_option = input("Press 1 to Encrypt\nPress 2 to Decrypt\n: ")

	if usr_option == "1":

		raw_message = str(input("Write your message: "))
		cypher_message(raw_message)


	elif usr_option == "2":

		raw_message = str(input("Write your message: "))
		decypher_message(raw_message)

	else:
		print("Try again, with a number this time!")
		get_information()



					#Main Part of the Script
get_information()
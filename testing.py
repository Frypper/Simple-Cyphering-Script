#"Cypher"

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
capitalAlphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
cyphered = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","m","n","b","v","c","x","z"]



					#Cypher Part of the script
def cypher(users):

#Defines two variables, The one that we are gonna use for the result and the list
	resultMessage = ""
	
#Creates loop that's gonna last as much as the lenght of the whole message
#And is gonna replace each letter with a letter in the chyphered list
	for j in range(len(users)):

		if users[j] in alphabet or users[j] in capitalAlphabet:
			obj = users[j]
			resultMessage += cyphered[alphabet.index(obj)]

		else:
			resultMessage += " "

	print(resultMessage)



					#Decyphering part of the script
def decypher(users):

#Defines two variables, The one that we are gonna use for the result and the list
	resultMessage = ""
	
#Creates loop that's gonna last as much as the lenght of the whole message
	for j in range(len(users)):
		if users[j] in cyphered:
#			resultMessage += alphabet[j]
			whereAT = cyphered.index(users[j])
			resultMessage += alphabet[whereAT]
		else:
			resultMessage += " "

#prints out the result
	print(resultMessage)



					# getInput Part of the program

def getInformation():

	print("Encritper Version 2.0\n")
	usrOption = int(input("Press 1 to Encrypt\nPress 2 to Decrypt\n: "))

	if usrOption == 1:

		rawMessage = str(input("Write your message: "))
		cypher(rawMessage)


	elif usrOption == 2:

		rawMessage = str(input("Write your message: "))
		decypher(rawMessage)


	else:
		getInformation()



					#Main Part of the Script
getInformation()

#! /usr/bin/env python
from colorama import Fore,init
init()
G = Fore.GREEN
R = Fore.RESET
Red = Fore.RED
letters = "abcdefghijklmnopqrstuvwxyz"
def encrypt(text,key):
	final = ""
	for sym in text:
		if sym in letters:
			ind = letters.find(sym)
			ind += key
			ind %= 26
			final += letters[ind]
		else:
			final += sym
	print(f"{G}{final}{R}")
def decrypt(text):
	print("All posible variant:\n")
	for i in range (26):
		variant = ""
		for sym in text:
			if sym in letters:
				ind = letters.find(sym)
				ind += i
				ind %= 26
				variant += letters[ind] 
			else:
				variant += sym
		print(f"{Red}{variant}{R}")
while True:
	choose  = input("E for encrypt and D for decrypt ('exit' for exit):\n")
	if choose != "E" and choose != "D" and choose != "exit":
		print("I dont understand, try again")
		continue
	elif choose == "exit":
		break
	else:
		message = input("Enter message\n")
		message = message.lower()
		if choose == "D":
			decrypt(message)
		elif choose == "E":
			key = int(input("Enter key\n"))
			encrypt(message,key)

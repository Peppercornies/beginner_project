import random

def dice_roll():
	dice = random.randint(1,6)
	print(dice)
#	user_input = raw_input("Some input please: ")

dice_roll()

input1 = input('Roll again?')

while input1 == "y":
	dice_roll()
	input1 = input('Roll again?')

#while user_input == "y":
#	dice_roll(n)
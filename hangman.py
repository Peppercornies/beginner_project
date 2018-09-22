from graphics import *
import getpass

def initiate_game():
	word = getpass.getpass('Player 1, enter your word:')
	word = word.lower()
	return(word)

def start_game(word):
	known_word = list(len(word)*'_')
	possible_letters = 'abcdefghijklmnopqrstuvwxyz'
	guesses = 10;

	win = GraphWin()
	return(known_word,possible_letters,guesses,win)

def guess(word,possible_letters,guesses,known_word,win):
	guess = input('Known word: ' + ' '.join(known_word) + '\n' + 'Possible letters: ' + possible_letters + '\n' + 'Guess a letter:')
	if guess in possible_letters:
		possible_letters = possible_letters.replace(guess,'')
		if guess in word:
			print('That letter is in the word!')
			for i in range(len(word)):
				if  word[i] == guess:
					known_word[i] = word[i]

		else:
			print('Guess again.')
			guesses = guesses - 1
			if guesses == 9:
				base = Line(Point(0,200),Point(100,200))
				base.setWidth(5)
				base.draw(win)

			elif guesses == 8:
				support = Rectangle(Point(50,0),Point(50,200))
				support.draw(win)

			elif guesses == 7:
				crane = Rectangle(Point(50,0),Point(150,0))
				crane.draw(win)

			elif guesses == 6:
				chain = Rectangle(Point(150,0),Point(150,20))
				chain.draw(win)

			elif guesses == 5:
				head = Circle(Point(150,35),15)
				head.draw(win)

			elif guesses == 4:
				body = Rectangle(Point(150,50),Point(150,130))
				body.draw(win)

			elif guesses == 3:
				arm1 = Line(Point(150,60),Point(120,100))
				arm1.setWidth(3)
				arm1.draw(win)

			elif guesses == 2:
				arm2 = Line(Point(150,60),Point(180,100))
				arm2.setWidth(3)
				arm2.draw(win)

			elif guesses == 1:
				leg1 = Line(Point(150,130),Point(120,180))
				leg1.setWidth(3)
				leg1.draw(win)

			elif guesses == 0:
				leg2 = Line(Point(150,130),Point(180,180))
				leg2.setWidth(3)
				leg2.draw(win)

	else:
		print('Already tried that letter! Try again:')

	return(known_word,possible_letters,guesses,win)

word = initiate_game()

[known_word,possible_letters,guesses,win] = start_game(word)

while guesses > 0:
	(known_word,possible_letters,guesses,win) = guess(word,possible_letters,guesses,known_word,win)
	if ('_' in known_word) == False:
		input('You guessed the word! Congratulations!!!\nPress any key to exit')
		break
		
if guesses == 0:
	input('Better luck next time.\nThe correct word was: ' + word + '\nPress any key to exit')
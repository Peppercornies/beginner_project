def initiate_game():
	word = input('Player 1, enter your word:')
	word = word.lower()
	return(word)

def start_game(word):
	known_word = list(len(word)*'_')
	possible_letters = 'abcdefghijklmnopqrstuvwxyz'
	guesses = 10;
	return(known_word,possible_letters,guesses)

def guess(word,possible_letters,guesses,known_word):
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
	else:
		print('Already tried that letter! Try again:')

	return(known_word,possible_letters,guesses)

word = initiate_game()

[known_word,possible_letters,guesses] = start_game(word)

while guesses > 0:
	(known_word,possible_letters,guesses) = guess(word,possible_letters,guesses,known_word)
	if ('_' in known_word) == False:
		print('You guessed the word! Congratulations!!!')

print('Better luck next time')
print(word)
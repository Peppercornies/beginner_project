import numpy as np

def initiate_game():
	game = np.array([1,1,1,1])
	player = 1
	return(player,game)

def play(player,game):
	options = []
	opstats = []

	# Options from swapping
	new_option = np.array([0,0,0,0])
	new_option[2*player-2] = -1
	new_option[2*player-1] = 1
	for i in range( -min(game[2*player-1], 4-game[2*player - 2]), min(game[2*player-2], 4-game[2*player-1])+1):
		if i != 0:
			if i != game[2*player-2] - game[2*player-1]:
				options.append(game + i*new_option)


				new_opstats = sum(new_option[[0,1]]) - sum(new_option[[2,3]])
				opstats.append(new_opstats)


	# Options from attacking
	new_option = np.array([0,0,0,0])
	for i in set((game[2*player-2],game[2*player-1])):
		for j in range(4 - 2*player,6 - 2*player):
			new_option = np.array([0,0,0,0])
			new_option[j] = 1
			new_option	= game + i*new_option
			new_option[new_option > 4] = 0
			options.append(new_option)
			
			new_opstats = sum(new_option[[0,1]]) - sum(new_option[[2,3]])
			opstats.append(new_opstats)
			

	print(options)
	print(opstats)

	move = int(input('Player ' + str(player) + ', Pick an option:'))
	print('You picked' + str(options[move]))
	game = options[move]
	return(game)

[player,game] = initiate_game()
while (sum(game[[0,1]] > 0)*sum(game[[2,3]] > 0) > 0):
	game = play(player,game)
	if player == 1:
		player = 2
	else:
		player = 1

if sum(game[[2,3]] == 0) == 2:
	print('Player 1 wins!')
else:
	print('Player 2 wins!')
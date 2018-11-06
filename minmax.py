import numpy as np 

def initiate_game():
	game = np.zeros([3,3])
	player = 1
	return(game,player)

def make_move(game,player):
	moves = range(len(np.where(game == 0)[0]))
	print(game)
	while True:
		move = int(input('Pick a move:'))
		if move in moves:
			break
		else:
			print('Not a valid move, try again:')

	move = [np.where(game == 0)[0][move],np.where(game == 0)[1][move]]

	game[move[0],move[1]] = (-1)**(player - 1)

	return(game,move)

def win_check(game,move,player):
	win = 0
	play = (-1)**(player - 1)

	if move == [[0],[0]]:
		if np.all(game[[0,0],[1,2]] == play) or np.all(game[[1,2],[1,2]] == play) or np.all(game[[1,2],[0,0]] == play):
			win = play

	elif move == [[0],[1]]:
		if np.all(game[[0,0],[0,2]] == play) or np.all(game[[1,2],[1,1]] == play):
			win = play

	elif move == [[0],[2]]:
		if np.all(game[[0,0],[0,1]] == play) or np.all(game[[2,1],[0,1]] == play) or np.all(game[[2,1],[2,2]] == play):
			win = play

	elif move == [[1],[0]]:
		if np.all(game[[0,0],[2,0]] == play) or np.all(game[[1,1],[1,2]] == play):
			win = play

	elif move == [[1],[1]]:
		if np.all(game[[0,2],[1,1]] == play) or np.all(game[[0,2],[2,0]] == play) or np.all(game[[1,1],[0,2]] == play) or np.all(game[[0,2],[0,2]] == play):
			win = play

	elif move == [[1],[2]]:
		if np.all(game[[0,2],[2,2]] == play) or np.all(game[[1,1],[0,1]] == play):
			win = play

	elif move == [[2],[0]]:
		if np.all(game[[0,1],[0,0]] == play) or np.all(game[[1,0],[1,2]] == play) or np.all(game[[2,2],[1,2]] == play):
			win = play

	elif move == [[2],[1]]:
		if np.all(game[[2,2],[0,2]] == play) or np.all(game[[0,1],[1,1]] == play):
			win = play

	elif move == [[2],[2]]:
		if np.all(game[[0,1],[2,2]] == play) or np.all(game[[0,1],[0,1]] == play) or np.all(game[[2,2],[0,1]] == play):
			win = play

	return(win)

[game,player] = initiate_game()

turns = 0
win = 0

while win == 0 and turns < 9:
	turns += 1
	[game,move] = make_move(game,player)
	win = win_check(game,move,player)
	player = 3 - player


if win == 0:
	print('Draw')
elif win == 1:
	print('Player 1 won!!')
elif win == -1:
	print('Player 2 won!!')
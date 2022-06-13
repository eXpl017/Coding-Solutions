print('Enter the number of queens: ')
n = int(input())
board = [[0]*n for _ in range(n)]

def isattack(i,j):
	for k in range(n):
		if board[i][k]==1 or board[k][j]==1:
			return True
	for k in range(n):
		for l in range(n):
			if (k+l==i+j) or (k-l==i-j):
				if board[k][l]==1:
					return True
	return False

def nqueens(n):
	if n == 0:
		return True
	for i in range(n):
		for j in range(n):
			if (not(isattack(i,j))) and (board[i][j]!=1):
				board[i][j] = 1
				if nqueens(n-1) == True:
					return True
				board[i][j] = 0
	return False

nqueens(n)
print(board)
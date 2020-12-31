

def sum_2048(board, action='Right'):
    
    if type(action) != str:
        print('ERROR: "action" should be string')
        return
    
    def indx(action):
        
        if action in ('Right', 'Down'):
            ind = [[j for j in range(len(board))] for i in range(len(board))]
        else:
            ind = [[j for j in range(len(board)-1, -1, -1)] for i in range(len(board))]
        
        indx = []
        for i in range(len(ind)):
            for j in ind[i]:
                if action in ('Down', 'Up'):
                    indx.append([j,i])
                else:
                    indx.append([i,j])       
        return indx
    
    def calculate(board, action):
        change = 0
        ind = indx(action)    
        for k in range(len(ind)):
            i = ind[k][0]
            j = ind[k][1]
            i_l = i
            j_l = j
            if k > 0:
                i_l = ind[k-1][0]
                j_l = ind[k-1][1]
            if board[i_l][j_l] != 0 and ((i != i_l and j == j_l) or (i == i_l and j != j_l)):
                if board[i][j] == board[i_l][j_l]:
                    board[i][j] += board[i_l][j_l]
                    board[i_l][j_l] = 0
                    change = 1
                if board[i][j] == 0:
                    board[i][j] = board[i_l][j_l]
                    board[i_l][j_l] = 0
                    change = 1
        if change == 1:
            board = calculate(board, action)
        return board
    
    board = calculate(board, action)
    return board

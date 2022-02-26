
import math



def draw_board(board):
    result = ''
    for row in board:
        for cell in row:
            if len(cell) == 1:
                cell = f'0{cell}' if cell.isdigit() else f' {cell}'
            result += f'| {cell} |'
        result += '\n'
    print(result)
def create_basic_board(dimensions):
    board = []
    n = 1
    for i in range(dimensions):
        row = []
        for j in range(dimensions):
            row.append(str(n))
            n += 1
        board.append(row)
    return board
def get_index_from_number(dimensions,number):
    if number <= dimensions : return (0,number - 1)
    row = math.floor(number / dimensions) if number % dimensions != 0 else math.floor(number / dimensions) - 1
    column = (number % dimensions) - 1 if number % dimensions != 0 else dimensions - 1
    return (row,column)
def validate_input(dimensions,board,number):
    if not(number.isdigit()) : return False
    number = int(number)
    if number > dimensions ** 2:
        return False
    if number <= 0 : return False
    row,column = get_index_from_number(dimensions,number)
    cell = board[row][column]
    if cell.lower() in ['s','o'] : return False
    return True


def take_input(dimensions,board,msg):
    number = input(msg)
    while not(validate_input(dimensions,board,number)):
        print('Invalid Input')
        number = input(msg)
    return get_index_from_number(dimensions,int(number))
def check_point_o(dimensions,board,row,column):
    can_check_horizontal = column not in [0,dimensions - 1] 
    can_check_vertical = row not in [0,dimensions - 1]
    can_check_diagonal = can_check_horizontal and can_check_vertical

    strings = []
    if can_check_diagonal:
        strings.append(board[row - 1][column - 1] + board[row][column] + board[row + 1][column + 1]) 
        strings.append(board[row - 1][column + 1] + board[row][column] + board[row + 1][column - 1])
    if can_check_horizontal:
        strings.append(board[row][column - 1] + board[row][column] + board[row][column + 1]) 
    if can_check_vertical:
        strings.append(board[row - 1][column] + board[row][column] + board[row + 1][column]) 
    return len([sos for sos in strings if sos == 'SOS'])
def check_point_s(dimensions,board,row,column):
    can_check_up = row > 1
    can_check_right = column < dimensions - 2
    can_check_left = column > 1
    can_check_down = row < dimensions - 2
    strings = []
    if can_check_up:
        strings.append(board[row - 2][column] + board[row - 1][column] + board[row][column]) # up
        if can_check_right:
            strings.append(board[row - 2][column + 2] + board[row - 1][column + 1] + board[row][column]) # up right
        if can_check_left:
            strings.append(board[row - 2][column - 2] + board[row - 1][column - 1] + board[row][column]) # up left
    if can_check_down:
        strings.append(board[row + 2][column] + board[row + 1][column] + board[row][column]) # down
        if can_check_right:
            strings.append(board[row + 2][column + 2] + board[row + 1][column + 1] + board[row][column]) # down right
        if can_check_left:
            strings.append(board[row + 2][column - 2] + board[row + 1][column - 1] + board[row][column]) # down left
    if can_check_left:
        strings.append(board[row][column - 2] + board[row][column - 1] + board[row][column]) # left
    if can_check_right:
        strings.append(board[row][column + 2] + board[row][column + 1] + board[row][column]) # left
    return len([sos for sos in strings if sos == 'SOS'])




def game(dimensions):
    board = create_basic_board(dimensions)
    available_blocks = dimensions ** 2
    draw_board(board)
    turn = 1
    scores = [0,0]
    while available_blocks != 0:
        row,column = take_input(dimensions,board,f'Player {turn} Enter Number : ')
        answere = input('Enter S or O : ').lower()
        while answere not in ['s','o']:
            print('Invalid Input')
            answere = input('Enter S or O : ').lower()
        board[row][column] = answere.upper()
        draw_board(board)
        score = check_point_s(dimensions,board,row,column) if answere.lower() == 's' else check_point_o(dimensions,board,row,column)
        scores[turn - 1] += score
        if not(score):
            turn = 2 if turn == 1 else 1 # change player
        
        print(f'Score Player 1 is  : {scores[0]}')
        print(f'Score Player 2 is  : {scores[1]}')
        available_blocks -= 1
    if scores[0] > scores[1] : print('Player 1 Win!!!!')
    elif scores[0] < scores[1] : print('Player 2 Win!!!!')
    else:print('Draw!!!')
    

def  main():
    dimensions = int(input('dimensions of the board [3-9] : '))
    while dimensions < 3 or dimensions > 9:
        dimensions = int(input('dimensions of the board [3-9] : '))
    game(dimensions)

if __name__ == '__main__':
    main()
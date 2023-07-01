import keyboard

grid = [[' - ', ' - ', ' - '], [' - ', ' - ', ' - '], [' - ', ' - ', ' - ']]
move = False

def print_grid(position) :
    for i in range(3) :
        print(position[i][0], position[i][1], position[i][2])

def on_key(event) :
    global move
    global grid
    n = int(event.name)
    row = 2 - (n - 1) // 3
    col = (n - 1) % 3
    if grid[row][col] == ' - ':
        grid[row][col] = ' O '
        move = True
        return
    
    move = False
    
def check_end(position):
    #checks end horizontally:
    for i in range(3):
        o = 0
        x = 0
        for j in range(3):
            if(position[i][j] == ' O '):
                o += 1
            elif(position[i][j] == ' X '):
                x += 1
        if o == 3 : return -1
        if x == 3 : return 1
            
    #checks end vertically:
    for i in range(3):
        o = 0
        x = 0
        for j in range(3):
            if(position[j][i] == ' O '):
                o += 1
            elif(position[j][i] == ' X '):
                x += 1
        if o == 3 : return -1
        if x == 3 : return 1
        
    #checks end diagonally:
    o = 0
    x = 0
    for i in range(3):
        if(position[i][i] == ' O '):
            o += 1
        elif(position[i][i] == ' X '):
            x += 1
        if o == 3 : return -1
        if x == 3 : return 1
        
    o = 0
    x = 0
    for i in range(3):
        if(position[i][2 - i] == ' O '):
            o += 1
        elif(position[i][2 - i] == ' X '):
            x += 1
            
        if o == 3 : return -1
        if x == 3 : return 1
        
    return 0
    
def possible_positions(position, player):
    possible_positions = []
    for r in range(3):
        for c in range(3):
            if position[r][c] == ' - ' and player:
                next_pos = [row[:] for row in position]
                next_pos[r][c] = ' X '
                possible_positions.append(next_pos)
            elif position[r][c] == ' - ' and not player:
                next_pos = [row[:] for row in position]
                next_pos[r][c] = ' O '
                possible_positions.append(next_pos)
    return possible_positions
    
def minimax(position, depth, maximizing_player):
    possible_moves = possible_positions(position, maximizing_player)
    if depth == 0 or check_end(position) != 0 or len(possible_moves) == 0:
        return check_end(position)

    if maximizing_player:
        best_move = None
        max_eval = -10
        for i in range (len(possible_moves)):
            eval = minimax(possible_moves[i], depth - 1, False)
            if eval > max_eval:
                max_eval = eval
                best_move = possible_moves[i]
                
        if depth == 5:  
            return best_move
        else:
            return max_eval
    else:
        min_eval = 10
        for i in range (len(possible_moves)):
            eval = minimax(possible_moves[i], depth - 1, True)
            min_eval = min(min_eval, eval)

        return min_eval
        
keyboard.on_press(on_key)

while(1):
    move = False
        
    print("Make a move. Current board:")
    print_grid(grid)
    
    while not move:
        pass

    print("Move made")
    
    #if the game is over, it breaks the loop
    if check_end(grid) != 0 or len(possible_positions(grid, 1)) == 0:
        print("GAME OVER!")
        print_grid(grid)
        break
    
    #makes the computer perfect move
    best_move = minimax(grid, 5 , 1)
    grid = best_move
    
    #if the game is over, it breaks the loop
    if check_end(grid) != 0 or len(possible_positions(grid, 0)) == 0:
        print("GAME OVER!")
        print_grid(grid)
        break
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
        if o == 3 : return 1
        if x == 3 : return -1
            
    #checks end vertically:
    for i in range(3):
        o = 0
        x = 0
        for j in range(3):
            if(position[j][i] == ' O '):
                o += 1
            elif(position[j][i] == ' X '):
                x += 1
        if o == 3 : return 1
        if x == 3 : return -1
        
    #checks end diagonally:
    for i in range(3):
        o = 0
        x = 0
        if(position[i][i] == ' O '):
            o += 1
        elif(position[i][i] == ' X '):
            x += 1
        if o == 3 :  return 1
        if x == 3 : return -1
        
    for i in range(3):
        o = 0
        x = 0
        if(position[i][2 - i] == ' O '):
            o += 1
        elif(position[i][2 - i] == ' X '):
            x += 1
        if o == 3 :  return 1
        if x == 3 : return -1
        
    return 0
    
def possible_positions(position, maximizing_player):
    possible_positions = []
    for r in range(3):
        for c in range(3):
            if position[r][c] == ' - ' and maximizing_player:
                next_pos = [row[:] for row in position]
                next_pos[r][c] = ' O '
                possible_positions.append(next_pos)
            elif position[r][c] == ' - ' and not maximizing_player:
                next_pos = [row[:] for row in position]
                next_pos[r][c] = ' X '
                possible_positions.append(next_pos)
    return possible_positions
    
def minimax(position, depth, maximizing_player):
    if depth == 0 or check_end(position) != 0:
        return check_end(position)
    
    if maximizing_player:
        max_eval = -1
        

keyboard.on_press(on_key)

while(1):
    move = False
    
    for position in possible_positions(grid, True):
        print_grid(position)
        print("")
        
    print("Make a move:")
    print_grid(grid)
    
    while not move:
        pass

    print("Move made")
    
    if check_end(grid) != 0:
        break


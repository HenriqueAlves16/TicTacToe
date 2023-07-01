import keyboard

grid = [[' - ', ' - ', ' - '], [' - ', ' - ', ' - '], [' - ', ' - ', ' - ']]
move = False

def print_grid() :
    for i in range(3) :
        print(grid[i][0], grid[i][1], grid[i][2])

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

def check_end():
    global grid
    #checks end horizontally:
    for i in range(3):
        o = 0
        x = 0
        for j in range(3):
            if(grid[i][j] == ' O '):
                o += 1
            elif(grid[i][j] == ' X '):
                x += 1
        print(o)
        if o == 3 :  return 1
        if x == 3 : return -1
            
    #checks end vertically:
    for i in range(3):
        o = 0
        x = 0
        for j in range(3):
            if(grid[j][i] == ' O '):
                o += 1
            elif(grid[j][i] == ' X '):
                x += 1
        if o == 3 :  return 1
        if x == 3 : return -1
        
    #checks end diagonally:
    for i in range(3):
        o = 0
        x = 0
        if(grid[i][i] == ' O '):
            o += 1
        elif(grid[i][i] == ' X '):
            x += 1
        if o == 3 :  return 1
        if x == 3 : return -1
        
    for i in range(3):
        o = 0
        x = 0
        if(grid[i][2 - i] == ' O '):
            o += 1
        elif(grid[i][2 - i] == ' X '):
            x += 1
        if o == 3 :  return 1
        if x == 3 : return -1
        
    return 0
    

keyboard.on_press(on_key)

while(check_end() == 0):
    print(check_end())
    move = False
    print("Make a move:")
    print_grid()

    while not move:
        pass

    print("Move made:")

        
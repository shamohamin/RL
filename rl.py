import random
import sys
import tkinter
from rl_ui import RlUI

class State:
    def __init__(self):
        self._left = 0.0
        self._right = 0.0
        self._up = 0.0
        self._down = 0.0
        self._value = 0.0
    
    def __repr__(self):
        return "left is :{0} right is:{1} up is:{2} down is:{3} value is:{4} "\
                    .format(self._left, self._right, self._up, self._down, self._value)
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value

    @property
    def left(self):
        return self._left
    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, right):
        self._right = right

    @property
    def up(self):
        return self._up
    @up.setter
    def up(self, up):
        self._up = up

    @property
    def down(self):
        return self._down
    @down.setter
    def down(self, down):
        self._down = down
    
map = [[' ','#',' ','#',' '],
       [' ',' ',' ',' ','#'],
       [' ',' ','#',' ',' '],
       [' ',' ',' ',' ',' '],
       [' ',' ',' ','#','G']]

state_map = [list(),list(),list(),list(),list()]

myX = 0
myY = 0

def init_state():
    global state_map
    counter = 0
    for index_x, x in enumerate(map):
        for index_y, y in enumerate(x):
            state_map[index_x].append(State())
        
def _print():
    for x in state_map:
        for y in x:
            print(y,)
        print
        
def main():
    global myX , myY
    init_state()
    # _print()
    # sys.exit(0)
    for x in range(0, 1000):
        while is_game_over() == False:
            rand = random.randint(1, 10)
            if rand < 5:
                action = random_mov()
                move(action)
                update_values()
            else:
                action = best_move()
                move(action)
                update_values()
        myX = 0
        myY = 0
    _print()
    
def best_move():
    moves = []
    global state_map
    max_value = state_map[myX][myY].value
    if max_value == state_map[myX][myY].right:
        moves.append("right")
    if max_value == state_map[myX][myY].left:
        moves.append("left")
    if max_value == state_map[myX][myY].down:
        moves.append("down")
    if max_value == state_map[myX][myY].up:
        moves.append("up")
    return moves[random.randint(0, len(moves) - 1)]
    
def update_values():
    global state_map
    for index_x, x in enumerate(state_map):
        for index_y, y in enumerate(x):
            state_map[index_x][index_y].value = max(state_map[index_x][index_y].up, state_map[index_x][index_y].right, state_map[index_x][index_y].left, state_map[index_x][index_y].down)
            
def move(action):
    global myX
    global myY
    global state_map
    if action == "up":
        print("hello")
        myX -= 1
        if myX < 0:
            state_map[myX+1][myY].up = -10.0
        else:
            state_map[myX+1][myY].up = state_map[myX][myY].value + get_state_reward(myX, myY) - 0.04
    if action == "down":
        myX += 1
        if myX > 4:
            state_map[myX-1][myY].down = -10.0
        else:
            state_map[myX-1][myY].down = state_map[myX][myY].value + get_state_reward(myX, myY) - 0.04        
    if action == "right":
        myY += 1
        if myY > 4:
            state_map[myX][myY-1].right = -10.0
        else:
            state_map[myX][myY-1].right = state_map[myX][myY].value + get_state_reward(myX, myY) - 0.04
    if action == "left":
        myY -= 1
        if myY < 0:
            state_map[myX][myY+1].left = -10.0
        else:
            state_map[myX][myY+1].left = state_map[myX][myY].value + get_state_reward(myX, myY) - 0.04
    
def random_mov():
    map = ["up", "down", "right", "left"]
    return map[random.randint(0,len(map) - 1)]

def get_state_reward(x, y):
    global map
    if map[x][y] == '#':
        return -10.0
    if map[x][y] == 'G':
        return 10.0
    return 0.0
        
def is_game_over():
    global map
    
    if myX < 0 or myY < 0:
        return True
    elif myX > 4 or myY > 4:
        return True
    elif map[myX][myY] == '#' or map[myX][myY] == 'G':
        return True
    else:
        return False
    
if __name__ == '__main__':
    main()
    root = tkinter.Tk()
    rl = RlUI(root)
    rl.make(state_map, map)
    rl.mainloop()
from tkinter import *
# from rl import State

class RlUI(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.canvase = Canvas(self, width=250, height=300)
        self.lable = Label(self)
        
    def make(self, board , map):
        python_green = "#476042"
        x ,y = 0, 0 
        for (index_x, i) in enumerate(board):
            for (index_y, j) in enumerate(i):
                if map[index_x][index_y] == ' ':
                    if index_x == 0 and index_y == 0:
                        option = {
                            'start' : 0,
                            'extend' : 150,
                            'fill' : "black"
                        }
                        self.canvase.create_arc((0,0, 50, 40) ,start=0,extent=270,fill="blue")
                    color = self.get_color(j)
                    self.canvase.create_polygon((x, y, x, y+50, x+25, y+25),outline=python_green ,fill=color.get("left"))
                    self.canvase.create_polygon((x, y, x+50, y, x+25, y+25),outline=python_green ,fill=color.get("up"))
                    self.canvase.create_polygon((x+50, y, x+50, y+50, x+25, y+25),outline=python_green ,fill=color.get("right"))
                    self.canvase.create_polygon((x, y+50, x+50, y+50, x+25, y+25),outline=python_green ,fill=color["down"])
                else:
                    if map[index_x][index_y] == '#':
                        self.canvase.create_rectangle(x, y, x+50, y+50, fill="red")
                    else:
                        self.canvase.create_rectangle(x, y, x+50, y+50, fill="blue")
                x += 51
            x = 0
            y += 51
        self.canvase.pack(padx=10)
        self.pack(padx=10)
    
    def get_color(self, state):
        green_color = ["#e6ffe6", "#98ff98", "#0eff0e", "#005d00"]
        color = {}
        colors = [state.up , state.down, state.right, state.left]
        colors.sort()
        for (i, x) in enumerate(colors):
            if x == state.up:
                color["up"] = green_color[i]
            if x == state.down:
                color["down"] = green_color[i]
            if x == state.right:
                color["right"] = green_color[i]
            if x == state.left:
                color["left"] = green_color[i]
        return color    
    
        
        
                
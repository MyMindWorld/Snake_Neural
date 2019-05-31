from tkinter import *
import time
import random
# Globals
WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True
points = 0


class Game:

    # Helper functions
    def create_block(self=0):
        print('Created Apple')
        """ Creates an apple to be eaten """
        global WIDTH, HEIGHT, SEG_SIZE, IN_GAME, BLOCK, points
        posx = SEG_SIZE * random.randint(1, (WIDTH - SEG_SIZE) / SEG_SIZE)
        posy = SEG_SIZE * random.randint(1, (HEIGHT - SEG_SIZE) / SEG_SIZE)
        BLOCK = c.create_oval(posx, posy,
                              posx + SEG_SIZE, posy + SEG_SIZE,
                              fill="red")
        # return BLOCK

    def main(self=0):
        """ Handles game process """
        global WIDTH, HEIGHT, SEG_SIZE, IN_GAME, points
        if IN_GAME:
            s.move()
            # s.vector = s.mapping['Down']
            head_coords = c.coords(s.segments[-1].instance)
            x1, y1, x2, y2 = head_coords
            #print(x1, x2, y1, y2)
            # Check for collision with gamefield edges
            if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
                print('You exited gamefield')
                IN_GAME = False
            # Eating apples
            elif head_coords == c.coords(BLOCK):
                print('Apple has been eaten')
                points += 10
                print('Points:%s' % points)
                s.add_segment()
                c.delete(BLOCK)
                Game.create_block()
            # Self-eating
            else:
                for index in range(len(s.segments) - 1):
                    if head_coords == c.coords(s.segments[index].instance):
                        print('You SHIT yourself')
                        IN_GAME = False
            root.after(100, Game.main)
        # Not IN_GAME -> stop game and print message
        else:
            c.create_text(WIDTH / 2, HEIGHT / 2,
                          text="GAME OVER!",
                          font="Arial 20",
                          fill="red")
            print('Game over!')


    def start(self=0):
        global WIDTH, HEIGHT, SEG_SIZE, IN_GAME, root,c,s,points
        # Setting up window

        root = Tk()
        root.title("Ai Snake")

        c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
        c.grid()
        # catch keypressing
        c.focus_set()
        # creating segments and snake
        segments = [Segment(SEG_SIZE, SEG_SIZE),
                    Segment(SEG_SIZE * 2, SEG_SIZE),
                    Segment(SEG_SIZE * 3, SEG_SIZE)]
        s = Snake(segments)
        # Reaction on keypress
        c.bind("<KeyPress>", s.change_direction)
        # s.vector = s.mapping['Down']
        Game.create_block()
        Game.main()
        root.mainloop()
        return 0


class Segment(object):
    """ Single snake segment """

    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x + SEG_SIZE, y + SEG_SIZE,
                                           fill="white")


class Snake(object):
    """ Simple Snake class """

    def __init__(self, segments):
        self.segments = segments
        # possible moves
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # initial movement direction
        self.vector = self.mapping["Down"]

    def move(self):
        """ Moves the snake with the specified vector"""

        for index in range(len(self.segments) - 1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                 x1 + self.vector[0] * SEG_SIZE, y1 + self.vector[1] * SEG_SIZE,
                 x2 + self.vector[0] * SEG_SIZE, y2 + self.vector[1] * SEG_SIZE)

    def add_segment(self):
        """ Adds segment to the snake """
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Segment(x, y))

    def change_direction(self, event):
        """ Changes direction of snake """
        if event.keysym in self.mapping:
            if event.keysym == "Down" and self.vector == self.mapping['Up']:
                print('You tried to shit youself')
            elif event.keysym == "Up" and self.vector == self.mapping['Down']:
                print('You tried to shit youself')
            elif event.keysym == "Left" and self.vector == self.mapping['Right']:
                print('You tried to shit youself')
            elif event.keysym == "Right" and self.vector == self.mapping['Left']:
                print('You tried to shit youself')
            else:
                self.vector = self.mapping[event.keysym]

def start():
    Game.start()

if __name__ == "__main__":
    Game.start()
